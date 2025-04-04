import unittest
from textnode import TextNode, TextType
from text_func import markdown_to_blocks  # replace with your actual module name

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    
    def test_basic_markdown_blocks(self):
        md = """# Heading

Paragraph with **bold** text.

- List item 1
- List item 2"""
        
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "# Heading",
                "Paragraph with **bold** text.",
                "- List item 1\n- List item 2"
            ]
        )

    def test_markdown_with_excessive_newlines(self):
        md = """First paragraph


Second paragraph



Third paragraph"""
        
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "First paragraph",
                "Second paragraph",
                "Third paragraph"
            ]
        )
  


if __name__ == "__main__":
    unittest.main()