import unittest

from textnode import TextNode


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


if __name__ == "__main__":
    unittest.main()
