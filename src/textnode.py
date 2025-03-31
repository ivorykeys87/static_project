from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic" 
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None, alt=None):
        self.text = text
        self.text_type = text_type
        self.url = url
        self.alt = alt

    def __eq__(self, tnode2):
        return self.text == tnode2.text and self.text_type == tnode2.text_type and self.url == tnode2.url and self.alt == tnode2.alt
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url}, {self.alt})"
    



