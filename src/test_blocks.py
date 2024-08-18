import unittest

from htmlnode import LeafNode, ParentNode

from blocks import (
    markdown_to_blocks,
    markdown_to_html_node,
    block_to_block_type,
    block_type_heading1,
    block_type_heading2,
    block_type_heading3,
    block_type_heading4,
    block_type_heading5,
    block_type_heading6,
    block_type_paragraph,
    block_type_code,
    block_type_quote,
    block_type_unordered_list,
    block_type_ordered_list,
)

class TestBlocks(unittest.TestCase):
    def test_blocks_single(self):
        text = "testing"
        result = markdown_to_blocks(text)
        solution = ["testing"]
        self.assertEqual(result, solution)

    def test_blocks_single_whitespace(self):
        text = "   testing      "
        result = markdown_to_blocks(text)
        solution = ["testing"]
        self.assertEqual(result, solution)

    def test_blocks_multiple(self):
        text = """
1
1

2
2

3
3
"""
        result = markdown_to_blocks(text)
        solution = ["1\n1", "2\n2", "3\n3"]
        self.assertEqual(result, solution)


    
    def test_blocks_multiple_extrablank_lines(self):
        text = """
1
1


2
2



3
3

"""
        result = markdown_to_blocks(text)
        solution = ["1\n1", "2\n2", "3\n3"]
        self.assertEqual(result, solution)

class TestBlockType(unittest.TestCase):
    def test_block_headings(self):
        text1 = "# test"
        text2 = "## test"
        text3 = "### test"
        text4 = "#### test"
        text5 = "##### test"
        text6 = "###### test"
        solution1 = block_type_heading1
        solution2 = block_type_heading2
        solution3 = block_type_heading3
        solution4 = block_type_heading4
        solution5 = block_type_heading5
        solution6 = block_type_heading6
        result1 = block_to_block_type(text1)
        result2 = block_to_block_type(text2)
        result3 = block_to_block_type(text3)
        result4 = block_to_block_type(text4)
        result5 = block_to_block_type(text5)
        result6 = block_to_block_type(text6)
        self.assertEqual(result1, solution1)
        self.assertEqual(result2, solution2)
        self.assertEqual(result3, solution3)
        self.assertEqual(result4, solution4)
        self.assertEqual(result5, solution5)
        self.assertEqual(result6, solution6)

    def test_block_code(self):
        text = """```this is a test of
code blocks
last line```"""
        result = block_to_block_type(text)
        solution = block_type_code
        self.assertEqual(result, solution)

    def test_block_quote(self):
        text = """>line1
>line2
>line3"""
        result = block_to_block_type(text)
        solution = block_type_quote
        self.assertEqual(result, solution)

    def test_block_unordered_list(self):
        text = """- item 1
- item 2
- item 3"""
        result = block_to_block_type(text)
        solution = block_type_unordered_list
        self.assertEqual(result, solution)

    def test_block_ordered_list(self):
        text = """1. item 1
33.  item 2
1000. item 3"""
        result = block_to_block_type(text)
        solution = block_type_ordered_list
        self.assertEqual(result, solution)

    def test_block_paragraph(self):
        text = "this is plain text"
        result = block_to_block_type(text)
        solution = block_type_paragraph
        self.assertEqual(result, solution)

class TestBlockToHTML(unittest.TestCase):

    def test_paragraph(self):
        markdown = """
Example **bold** line
line 2

"""
        node = markdown_to_html_node(markdown)
        result = node.to_html()
        solution = "<div><p>Example <b>bold</b> line line 2</p></div>"
        self.assertEqual(result, solution)

    def test_paragraph_multi(self):
        markdown = """
Example **bold** line
line 2

Paragraph 2: *Italics text*
"""
        node = markdown_to_html_node(markdown)
        result = node.to_html()
        solution = "<div><p>Example <b>bold</b> line line 2</p><p>Paragraph 2: <i>Italics text</i></p></div>"
        print(result)
        print(solution)
        self.assertEqual(result, solution)

    def test_headings(self):
        markdown = "# heading1 test"
        node = markdown_to_html_node(markdown)
        result = node.to_html()
        solution = "<div><h1>heading1 test</h1></div>"
        self.assertEqual(result, solution)
        
    def test_code_block(self):
        markdown = """```code block test```

normal paragraph"""
        node = markdown_to_html_node(markdown)
        result = node.to_html()
        solution = "<div><pre><code>code block test</code></pre><p>normal paragraph</p></div>"
        self.assertEqual(result, solution)

    def test_unordered_list(self):
        markdown = """- list item 1
- list item 2
- third list item"""
        node = markdown_to_html_node(markdown)
        result = node.to_html()
        solution = "<div><ul><li>list item 1</li><li>list item 2</li><li>third list item</li></ul></div>"
        self.assertEqual(result, solution)
    
    def test_ordered_list(self):
        markdown = """1. list item 1
2. list item 2
200. third list item"""
        node = markdown_to_html_node(markdown)
        result = node.to_html()
        solution = "<div><ol><li>list item 1</li><li>list item 2</li><li>third list item</li></ol></div>"
        self.assertEqual(result, solution)

    def test_blockquote(self):
        markdown = """>blockquote line 1
>two"""

        node = markdown_to_html_node(markdown)
        result = node.to_html()
        solution = "<div><blockquote>blockquote line 1 two</blockquote></div>"
        self.assertEqual(result, solution) 
