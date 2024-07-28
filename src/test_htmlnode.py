import unittest

from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode("p",
                        "para-value",
                        None,
                        {"href": "test.com"})
        self.assertEqual(node.props_to_html(), " href=\"test.com\"")
        
    def test_repr(self):
        empty_node = HTMLNode()
        node1 = HTMLNode("",
                        "raw_text",
                        empty_node,
                        )
        node2 = HTMLNode("a",
                        "a-val",
                        node1,
                        )
        node3 = HTMLNode("a",
                        "a-text",
                        node2,
                        {"href": "test.com"})
        self.assertEqual(str(node1), ", raw_text, None, None, None, None, None")
        self.assertEqual(str(node2), "a, a-val, , raw_text, None, None, None, None, None, None")
        self.assertEqual(str(node3), "a, a-text, a, a-val, , raw_text, None, None, None, None, None, None, {'href': 'test.com'}")

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        leaf1 = LeafNode("p", "This is a paragraph", None)
        leaf2 = LeafNode("a", "Click me", {"href": "test.com"})
        solution1 = "<p>This is a paragraph</p>"
        solution2 = "<a href=\"test.com\">Click me</a>"
        self.assertEqual(leaf1.to_html(), solution1)
        self.assertEqual(leaf2.to_html(), solution2)

class TestParentNode(unittest.TestCase):
    def test_to_html(self):

        solution1 = "<p><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p>"
        node1 = (ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "Italic text"),
                LeafNode(None, "Normal text"),
            ],)
        )
        self.assertEqual(node1.to_html(), solution1)
        
        solution2 = "<div><p><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p></div>"
        node2 = ParentNode(
            "div",
            [ParentNode(
                "p",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "Italic text"),
                    LeafNode(None, "Normal text"),
                ],)]
        )
        self.assertEqual(node2.to_html(), solution2)
        
        solution3 = "<div><p><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p><div>Normal text</div></div>"
        node3 = ParentNode(
            "div",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "Italic text"),
                        LeafNode(None, "Normal text"),
                    ],),
                ParentNode(
                    "div",
                    [
                        LeafNode(None, "Normal text"),
                    ]
                )
             ]
        )
        self.assertEqual(node3.to_html(), solution3)
        
        node4 = (ParentNode(
            "p",
            [])
        )
        self.assertRaises(ValueError, node4.to_html)

        node5 = (ParentNode(
            "p",
            [
                LeafNode("b", None),
            ])
        )
        self.assertRaises(ValueError, node5.to_html)
        
if __name__ == "__main__":
    unittest.main()
