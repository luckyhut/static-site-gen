import unittest
from blocks import markdown_to_blocks

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
