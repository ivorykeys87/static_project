from textnode import *

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


def main():
        def text_node_to_html_node(self):
        if self.text_type not in TextType:
            raise Exception("No Such Text Type")
        elif self.text_type == TextType.TEXT:
            return LeafNode(None, self.text, None)
        elif self.text_type == TextType.BOLD:
            return LeafNode("b", self.text, None)
        elif self.text_type == TextType.ITALIC:
            return LeafNode("i", self.text, None)
        elif self.text_type == TextType.CODE:
            return LeafNode("code", self.text, None)
        elif self.text_type == TextType.LINK:
            return LeafNode("a", self.text, ({"href": self.url} if self.url else None))
        elif self.text_type == TextType.IMAGE:
            return LeafNode("img", None, ("serc":self.url, "alt":??) )














main()