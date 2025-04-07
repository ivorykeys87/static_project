from enum import Enum
import unittest

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