import unittest

from textnode import TextNode, TextType

def test_text_type_text():
    node = TextNode("Example text", TextType.TEXT)
    html_node = text_node_to_html_node(node)
    assert html_node.tag is None
    assert html_node.value == "Example text"
    assert html_node.props is None

def test_text_type_bold():
    node = TextNode("Bold text", TextType.BOLD)
    html_node = text_node_to_html_node(node)
    assert html_node.tag == "b"
    assert html_node.value == "Bold text"
    assert html_node.props is None

def test_text_type_link():
    node = TextNode("Link text", TextType.LINK, url="http://example.com")
    html_node = text_node_to_html_node(node)
    assert html_node.tag == "a"
    assert html_node.value == "Link text"
    assert html_node.props == {"href": "http://example.com"}

def test_link_with_missing_url():
    node = TextNode("Link with no URL", TextType.LINK)
    html_node = text_node_to_html_node(node)
    assert html_node.tag == "a"
    assert html_node.value == "Link with no URL"
    assert html_node.props is None

def test_image_with_missing_alt():
    node = TextNode("Unimportant")


if __name__ == "__main__":
    unittest.main()