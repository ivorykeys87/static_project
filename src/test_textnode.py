import unittest
from textnode import TextNode, TextType
from main import extract_markdown_images  # replace with your actual module name

def test_extract_markdown_images(self):
    matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
    )
    self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
        


if __name__ == "__main__":
    unittest.main()