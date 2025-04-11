import unittest
import re
import os
import shutil
from blocknode import markdown_to_html_node
import sys



def copy_static_to_public(source_dir=None, dest_dir=None):
    # Initialize default paths if not provided
    if source_dir is None or dest_dir is None:
        # Get the directory where main.py is located
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Go up one level to reach static_project
        project_dir = os.path.dirname(script_dir)
        
        # Use default paths only if not provided
        if source_dir is None:
            source_dir = os.path.join(project_dir, "static")
        if dest_dir is None:
            dest_dir = os.path.join(project_dir, "public")
            
        # Check if destination exists and remove it (only for the initial call)
        if os.path.exists(dest_dir):
            print(f"Removing existing directory: {dest_dir}")
            shutil.rmtree(dest_dir)
        
        # Create the destination directory
        print(f"Creating directory: {dest_dir}")
        os.mkdir(dest_dir)
    
    print(f"Processing: {source_dir} -> {dest_dir}")
    
    # List all items in source directory
    items = os.listdir(source_dir)
    
    # Process each item
    for item in items:
        # Get full paths
        source_item = os.path.join(source_dir, item)
        dest_item = os.path.join(dest_dir, item)
        
        # Check if it's a file or directory
        if os.path.isfile(source_item):
            # Copy the file
            shutil.copy(source_item, dest_item)
            print(f"Copied file: {source_item} to {dest_item}")
        else:
    # It's a directory - create it if it doesn't exist
            if not os.path.exists(dest_item):
                os.mkdir(dest_item)
                print(f"Created directory: {dest_item}")
    
    # Recursive call with new source and destination
            copy_static_to_public(source_item, dest_item)

def extract_title(markdown):
    lines = markdown.split("\n")
    result = None
    for line in lines:
        if line.startswith("# "):
            result = line.strip("#").strip()
            return result
    raise Exception("No Header Found")

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, 'r') as file:
        from_data = file.read()
    with open(template_path, 'r') as file:
        template_data = file.read()
    html_string = markdown_to_html_node(from_data).to_html()
    title = extract_title(from_data)
    new_content = template_data.replace("{{ Title }}", title).replace("{{ Content }}", html_string )
    new_content = new_content.replace('href="/', f'href="{basepath}')
    new_content = new_content.replace('src="/', f'src="{basepath}')
    os.makedirs(os.path.dirname(dest_path), exist_ok= True)
    with open(dest_path, "w") as file:
        file.write(new_content)

def generate_pages_recursive(dir_path, template_path, dest_dir_path, basepath):
    for file in os.listdir(dir_path):
        full_path = os.path.join(dir_path, file)
        if os.path.isfile(full_path):
            if full_path.endswith(".md"):
                dest_file_path = os.path.join(dest_dir_path, file.replace(".md", ".html"))
                os.makedirs(os.path.dirname(dest_file_path), exist_ok=True)
                generate_page(full_path, template_path, dest_file_path, basepath)
        elif os.path.isdir(full_path):
            new_dest_dir = os.path.join(dest_dir_path, file)
            os.makedirs(new_dest_dir, exist_ok=True)
            generate_pages_recursive(full_path, template_path, new_dest_dir, basepath)
 

    

def main():

    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

    if os.path.exists("docs"):
        shutil.rmtree("docs")
    
    copy_static_to_public()

    generate_pages_recursive("content", "template.html","docs", basepath)


if __name__ == "__main__":
    main()