import unittest
from textnode import TextNode, TextType
from main import split_nodes_delimiter  # replace with your actual module name

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_no_delimiter(self):
        node = TextNode("This is plain text", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text, "This is plain text")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        
    def test_one_delimiter_pair(self):
        node = TextNode("This is text with `code` in it", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "This is text with ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "code")
        self.assertEqual(result[1].text_type, TextType.CODE)
        self.assertEqual(result[2].text, " in it")
        self.assertEqual(result[2].text_type, TextType.TEXT)
        


if __name__ == "__main__":
    unittest.main()