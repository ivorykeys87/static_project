import unittest
from textnode import TextNode, TextType
from main import extract_title  # replace with your actual module name

class TestExtractTitle(unittest.TestCase):
    
    def test_basic_title(self):
        markdown = "# This is a title"
        self.assertEqual(extract_title(markdown), "This is a title")
    
    def test_title_with_extra_space(self):
        markdown = "#     Extra spaces around title    "
        self.assertEqual(extract_title(markdown), "Extra spaces around title")
    
    def test_title_in_middle_of_document(self):
        markdown = "Some text before\n# The Real Title\nSome text after"
        self.assertEqual(extract_title(markdown), "The Real Title")
    
    def test_no_title_raises_exception(self):
        markdown = "No title here\nJust some regular text"
        with self.assertRaises(Exception):
            extract_title(markdown)
    
    def test_header_without_space_not_detected(self):
        markdown = "#This has no space after hash"
        with self.assertRaises(Exception):
            extract_title(markdown)

if __name__ == "__main__":
    unittest.main()