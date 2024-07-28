import unittest

from inline import split_nodes_delimiter
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


class TestInline(unittest.TestCase):
    
    def test_bold(self):
        bold_node = TextNode("sample text and **bold text** and **test**", text_type_text)
        new_nodes = split_nodes_delimiter([bold_node], "**", text_type_bold)
        soln = [
            TextNode("sample text and ", text_type_text),
            TextNode("bold text", text_type_bold),
            TextNode(" and", text_type_text),
            TextNode("test", text_type_bold),
        ]

    def test_italic(self):
        italic_node = TextNode("sample text and *italic text* and", text_type_text)
        new_nodes = split_nodes_delimiter([italic_node], "*", text_type_italic)
        soln = [
            TextNode("sample text and ", text_type_text),
            TextNode("italic text", text_type_italic),
            TextNode(" and", text_type_text),
        ]

    def test_code(self):
        code_node = TextNode("`code text` the rest of the text", text_type_text)
        new_nodes = split_nodes_delimiter([code_node], "`", text_type_code)
        soln = [
            TextNode("code text", text_type_code),
            TextNode(" the rest of the text", text_type_text),
        ]

    def test_single_delim(self):
        code_node = TextNode("**error text the rest of the text", text_type_text)
        self.assertRaises(Exception, split_nodes_delimiter, [code_node], "**", text_type_code)
