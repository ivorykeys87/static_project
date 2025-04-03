import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType

from main import text_to_textnodes  # replace with your actual module name

class TestMarkdownParser(unittest.TestCase):
    def test_text_to_textnodes(text):
        # Test simple text (no special formatting)
        result = text_to_textnodes("This is plain text.")
        assert len(result) == 1
        assert result[0].text == "This is plain text."
        assert result[0].text_type == TextType.TEXT

        # Test bold text
        result = text_to_textnodes("This is **bold** text.")
        assert len(result) == 3
        assert result[1].text == "bold"
        assert result[1].text_type == TextType.BOLD

        # Test italic text
        result = text_to_textnodes("This is _italic_ text.")
        assert len(result) == 3
        assert result[1].text == "italic"
        assert result[1].text_type == TextType.ITALIC

        # Test a mix of types at once
        result = text_to_textnodes("This is **bold** and _italic_ and a [link](https://boot.dev).")
        assert len(result) == 7
        # Check a few nodes for correctness
        assert result[1].text == "bold"
        assert result[1].text_type == TextType.BOLD
        assert result[3].text == "italic"
        assert result[3].text_type == TextType.ITALIC
        assert result[5].text == "link"
        assert result[5].text_type == TextType.LINK
        assert result[5].url == "https://boot.dev"

        # Test edge cases, like empty text
        result = text_to_textnodes("")
        assert len(result) == 0  # Should handle empty input gracefully

if __name__ == "__main__":
    unittest.main()