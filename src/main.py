from textnode import *
import unittest
import re

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

def main():
    pass


main()