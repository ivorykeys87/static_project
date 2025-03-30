import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestParentNode(unittest.TestCase):
    def test_parent_node_constructor(self):
        # Basic construction
        children = [LeafNode("span", "child")]
        node = ParentNode("div", children)
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.children, children)
        self.assertIsNone(node.props)
        self.assertIsNone(node.value)
        
        # With props
        props = {"class": "container"}
        node_with_props = ParentNode("div", children, props)
        self.assertEqual(node_with_props.props, props)
    
    def test_to_html_basic(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
    
    def test_to_html_with_multiple_children(self):
        children = [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text")
        ]
        parent_node = ParentNode("p", children)
        self.assertEqual(
            parent_node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )
    
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>"
        )



if __name__ == "__main__":
    unittest.main()