from textnode import *
from htmlnode import *
import re
import unittest


def text_node_to_html_node(text_node):
    if not isinstance(text_node.text_type, TextType):
        raise Exception("No Such Text Type")
    elif text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text, None)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text, None)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text, None)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text, None)
    elif text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, ({"href": text_node.url} if text_node.url else None))
    elif text_node.text_type == TextType.IMAGE:
        if not text_node.url or not text_node.alt:
            raise Exception("Image type requires both 'url' and 'alt'")
        return LeafNode("img", None, {"src":text_node.url, "alt":text_node.alt} )
    
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    found_delimeter = False
    for node in old_nodes:
        if not node.text_type == TextType.TEXT:
            new_nodes.append(node)
            continue
        text = node.text
        opening_index = text.find(delimiter)
        if opening_index == -1:
            new_nodes.append(node)
            continue
        found_delimeter = True
        closing_index = text.find(delimiter, opening_index + len(delimiter))
        if closing_index == -1:
            raise ValueError(f"Opening delimeter '{delimiter}' found, but no closing delimeter")
        if opening_index > 0:
            new_nodes.append(TextNode(text[0:opening_index], TextType.TEXT))
        new_nodes.append(TextNode(text[opening_index + len(delimiter):closing_index], text_type))
        after_text = text[closing_index + len(delimiter):]
        if after_text:
            new_nodes.append(TextNode(after_text, TextType.TEXT))
    if found_delimeter:
        return split_nodes_delimiter(new_nodes, delimiter, text_type)
    return new_nodes

def extract_markdown_images(text):
    return list(re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",text))

def extract_markdown_links(text):
    return list(re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text))

def split_nodes_image(old_nodes):
    result = []
    for old_node in old_nodes:
        # If no images or wrong type, just add the original node
        if old_node.text_type != TextType.TEXT or not extract_markdown_images(old_node.text):
            result.append(old_node)
            continue
            
        # Start with the current text
        curr_text = old_node.text
        
        # Process all images in this node
        while True:
            # Find an image in the current text
            images = extract_markdown_images(curr_text)
            if not images:
                # No more images, add remaining text if any
                if curr_text:
                    result.append(TextNode(curr_text, TextType.TEXT))
                break
                
            # Process the first image
            alt, url = images[0]
            image_markdown = f"![{alt}]({url})"
            
            # Split into "before image" and "after image"
            parts = curr_text.split(image_markdown, 1)
            
            # Add "before image" text node if not empty
            if parts[0]:
                result.append(TextNode(parts[0], TextType.TEXT))
                
            # Add the image node
            result.append(TextNode(alt, TextType.IMAGE, url))
            
            # Update current text to be the "after image" part
            curr_text = parts[1] if len(parts) > 1 else ""
    return result

def split_nodes_link(old_nodes):
    result = []
    for old_node in old_nodes:
        # If no images or wrong type, just add the original node
        if old_node.text_type != TextType.TEXT or not extract_markdown_links(old_node.text):
            result.append(old_node)
            continue
            
        # Start with the current text
        curr_text = old_node.text
        
        # Process all images in this node
        while True:
            # Find an image in the current text
            links = extract_markdown_links(curr_text)
            if not links:
                # No more images, add remaining text if any
                if curr_text:
                    result.append(TextNode(curr_text, TextType.TEXT))
                break
                
            # Process the first image
            alt, url = links[0]
            link_markdown = f"[{alt}]({url})"
            
            # Split into "before image" and "after image"
            parts = curr_text.split(link_markdown, 1)
            
            # Add "before image" text node if not empty
            if parts[0]:
                result.append(TextNode(parts[0], TextType.TEXT))
                
            # Add the image node
            result.append(TextNode(alt, TextType.LINK, url))
            
            # Update current text to be the "after image" part
            curr_text = parts[1] if len(parts) > 1 else ""
    return result

def text_to_textnodes(text):
    if not text:
        return []
    else:
        nodes = [TextNode(text, TextType.TEXT)]  # Start as a list of one TextNode
        nodes = split_nodes_image(nodes)
        nodes = split_nodes_link(nodes)
        nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
        nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    return nodes

def markdown_to_blocks(markdown):
    result_1 = list(markdown.split("\n\n"))
    result_2 = []
    for i in result_1:
        new_block = i.strip()
        if new_block:
            result_2.append(new_block)
        else:
            continue
    return result_2
