import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "This is a paragraph")
        node2 = HTMLNode("p", "This is a paragraph")
        #self.assertEqual(node, node2)
        print(node, node2)
    def test_not_eq(self):
        node = HTMLNode("p", "This is a paragraph")
        node2 = HTMLNode("p", "This is a ")
        #self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()