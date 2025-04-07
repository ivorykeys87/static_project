from enum import Enum
from text_func import *
import unittest
from htmlnode import *

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def block_to_block_type(text):
    if is_heading(text):
        return BlockType.HEADING
    elif is_code(text):
        return BlockType.CODE
    elif is_quote(text):
        return BlockType.QUOTE
    elif is_unordered_list(text):
        return BlockType.UNORDERED_LIST
    elif is_ordered_list(text):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH

def is_heading(text):
    count = 0
    for i in text:
        if i == "#":
            count = count + 1
        else:
            break
    return 1 <= count <= 6 and text[count] == " "

def is_code(text):
    return text.startswith("```") and text.endswith("```")

def is_quote(text):
    lines = text.split("\n")
    for line in lines:
        if not line.startswith(">"):
            return False
        continue
    return True

def is_unordered_list(text):
    lines = text.split("\n")
    for line in lines:
        if not line.startswith("- "):
            return False
        continue
    return True    

def is_ordered_list(text):
    lines = text.split("\n")
    num = 1
    for line in lines:
        if not line.startswith(f"{num}. "):
            return False
        else:
            num = num + 1
    return True

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        html_nodes.append(html_node)
    return html_nodes

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
            block_text = block.replace("\n", " ")
            children.append(HTMLNode("p",None, text_to_children(block_text)))
        elif block_type == BlockType.CODE:
            code_content = block.strip()
            code_lines = code_content.split("\n")[1:-1]
            code_text = "\n".join(code_lines) + "\n"
            text_node = TextNode(code_text, TextType.TEXT)
            code_node = text_node_to_html_node(text_node)
            pre_node = HTMLNode("pre", None, [HTMLNode("code", None, [code_node])])
            children.append(pre_node)
        elif block_type == BlockType.HEADING:
            count = 0
            for i in block:
                if not i == "#":
                    break
                else:
                    count = count + 1
            content = block[count:].strip()                
            children.append(HTMLNode(f"h{count}",None, text_to_children(content)))
        elif block_type == BlockType.UNORDERED_LIST:
            list = []
            for item in block.split("\n"):
                item = item.strip()
                if item and (item.startswith("- ") or item.startswith("* ")):
                    content = item[2:].strip()
                    list.append(HTMLNode("li", None, text_to_children(content)))
            children.append(HTMLNode("ul", None, list))
        elif block_type == BlockType.QUOTE:
            content_lines = []
            for line in block.split("\n"):
                if line.startswith(">"):
                    content_lines.append(line[1:].lstrip())
                else:
                    content_lines.append(line)
            content = "\n".join(content_lines)
            children.append(HTMLNode("blockquote", None, text_to_children(content)))
        else: 
            list = []
            for item in block.split("\n"):
                item = item.strip()
                for i, char in enumerate(item):
                    if char == "." and i > 0 and item[:i].isdigit():
                        content = item[i+1:].lstrip()                        
                        list.append(HTMLNode("li", None, text_to_children(content)))
                        break
            children.append(HTMLNode("ol", None, list))

    return HTMLNode("div", None, children)
