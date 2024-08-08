import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
    text_node_to_html_node,
)

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", "bold", "test.net")
        node2 = TextNode("This is a text node", "bold", "test.net")
        node3 = TextNode("This is a text node", "italic", "test.net")
        node4 = TextNode("Node", "underline", "test.net")
        node5 = TextNode("Node", "underline", None)
        node6 = TextNode("node", "underline", None)
        self.assertEqual(node1, node2)
        self.assertNotEqual(node2, node3)
        self.assertNotEqual(node4, node5)
        self.assertNotEqual(node5, node6)        
        
class TestTextNodeToHTML(unittest.TestCase):
    def test_text_node(self):
        text_node = TextNode("plain text", "text")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "plain text")

    def test_text_bold(self):
        text_node = TextNode("bold text", text_type_bold)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "bold text")

    def test_text_italic(self):
        text_node = TextNode("italic text", text_type_italic)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "italic text")

    def test_text_link(self):
        text_node = TextNode("link text", text_type_link, "test.com")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "link text")
        self.assertEqual(html_node.props, {"href": "test.com"})

        
if __name__ == "__main__":
    unittest.main()
