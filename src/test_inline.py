import unittest

from inline import (
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
    extract_markdown_links,
    extract_markdown_images,
)
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

    def test_extract_markdown_images(self):
        text = "this is the alt text ![pic text](img.jpg)"
        solution = [("pic text", "img.jpg")]
        self.assertEqual(extract_markdown_images(text), solution)

    def test_extract_markdown_images_multiple(self):
        text = "text ![pic text](img.jpg) text2 ![pic2 text](img2.jpg)"
        solution = [("pic text", "img.jpg"), ("pic2 text", "img2.jpg")]
        self.assertEqual(extract_markdown_images(text), solution)
        
    def test_extract_markdown_links(self):
        text = "this is a link to [gnu](gnu.org)"
        solution = [("gnu", "gnu.org")]
        self.assertEqual(extract_markdown_links(text), solution)

    def test_extract_markdown_links_multiple(self):
        text = "text ![link 1](gnu.org) text2 ![link 2](mozilla.org)"
        solution = [("link 1", "gnu.org"), ("link 2", "mozilla.org")]
        self.assertEqual(extract_markdown_images(text), solution)

    def test_split_nodes_image_single(self):
        node = TextNode(
            "Text with an image ![alt text](img.png) text after image",
            text_type_text)
        solution = [
            TextNode("Text with an image ", text_type_text),
            TextNode("alt text", text_type_image, "img.png"),
            TextNode(" text after image", text_type_text),
        ]
        test_node = split_nodes_image([node])
        self.assertEqual(test_node, solution)

    def test_split_nodes_image_multiple(self):        
        node = TextNode(
            "Text with an image ![alt text](img.png) text ![alt2](png2.png) after image",
            text_type_text)
        solution = [
            TextNode("Text with an image ", text_type_text),
            TextNode("alt text", text_type_image, "img.png"),
            TextNode(" text ", text_type_text),
            TextNode("alt2", text_type_image, "png2.png"),
            TextNode(" after image", text_type_text),
        ]
        test_node = split_nodes_image([node])
        self.assertEqual(test_node, solution)
    
    def test_split_nodes_image_wrong_markdown(self):
        node = TextNode(
            "Text with an image ![alt text](img.pngtext after image",
            text_type_text)
        wrong_answer = [
            TextNode("Text with an image ![alt text](img.pngtext after image", text_type_text)
        ]
        test_node = split_nodes_image([node])
        self.assertEqual(test_node, wrong_answer)

    def test_split_nodes_link_single(self):
        node = TextNode(
            "Text with a link [link name](test.com) text after link",
            text_type_text)
        solution = [
            TextNode("Text with a link ", text_type_text),
            TextNode("link name", text_type_link, "test.com"),
            TextNode(" text after link", text_type_text),
        ]
        test_node = split_nodes_link([node])
        self.assertEqual(test_node, solution)
    
    def test_split_nodes_link_multiple(self):
        node = TextNode(
            "Text with a link [link name](test.com) text [link2](test2.com) after link",
            text_type_text)
        solution = [
            TextNode("Text with a link ", text_type_text),
            TextNode("link name", text_type_link, "test.com"),
            TextNode(" text ", text_type_text),
            TextNode("link2", text_type_link, "test2.com"),
            TextNode(" after link", text_type_text),
        ]
        test_node = split_nodes_link([node])
        self.assertEqual(test_node, solution)    
        
    def test_split_nodes_link_wrong_markdown(self):
        node = TextNode(
            "Text with a link [link name](test.com text after link",
            text_type_text)
        solution = [
            TextNode("Text with a link [link name](test.com text after link", text_type_text),
        ]
        test_node = split_nodes_link([node])
        self.assertEqual(test_node, solution)
