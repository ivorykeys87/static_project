import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

from main import extract_markdown_images, extract_markdown_links  # replace with your actual module name

class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_single_image(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        matches = extract_markdown_images(text)
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    def test_extract_multiple_images(self):
        text = "Here are two images: ![first](https://example.com/1.jpg) and ![second](https://example.com/2.jpg)"
        matches = extract_markdown_images(text)
        expected = [
            ("first", "https://example.com/1.jpg"),
            ("second", "https://example.com/2.jpg")
        ]
        self.assertListEqual(expected, matches)
    
    def test_extract_image_with_empty_alt(self):
        text = "This is an image with no alt text: ![](https://example.com/image.png)"
        matches = extract_markdown_images(text)
        self.assertListEqual([("", "https://example.com/image.png")], matches)
    
    def test_extract_single_link(self):
        text = "Check out [Boot.dev](https://www.boot.dev)"
        matches = extract_markdown_links(text)
        self.assertListEqual([("Boot.dev", "https://www.boot.dev")], matches)
    
    def test_extract_multiple_links(self):
        text = "Visit [Google](https://google.com) or [GitHub](https://github.com)"
        matches = extract_markdown_links(text)
        expected = [
            ("Google", "https://google.com"),
            ("GitHub", "https://github.com")
        ]
        self.assertListEqual(expected, matches)

if __name__ == "__main__":
    unittest.main()