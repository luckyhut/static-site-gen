import re

block_type_heading1 = "heading1"
block_type_heading2 = "heading2"
block_type_heading3 = "heading3"
block_type_heading4 = "heading4"
block_type_heading5 = "heading5"
block_type_heading6 = "heading6"
block_type_paragraph = "paragraph"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered list"
block_type_ordered_list = "ordered list"

from htmlnode import HTMLNode, ParentNode, LeafNode
from inline import text_to_textnodes
from textnode import TextNode, text_node_to_html_node

def markdown_to_blocks(markdown):
    strings = markdown.split("\n\n")
    result = []
    for string in strings:
        if string != '':
            result.append(string.strip())
    return result

def block_to_block_type(block):
    words = block.split(" ")
    lines = block.split("\n")
    if is_heading(words[0]):
        return get_header_number(words[0])
    elif is_code(words):
        return block_type_code
    elif is_quote(lines):
        return block_type_quote
    elif is_unordered_list(lines):
        return block_type_unordered_list
    elif is_ordered_list(lines):
        return block_type_ordered_list
    else:
        return block_type_paragraph
    
def is_heading(word):
    if word == "#":
        return True
    if word == "##":
        return True
    if word == "###":
        return True
    if word == "####":
        return True
    if word == "#####":
        return True
    if word == "######":
        return True
    return False

def get_header_number(header):
    if header == "#":
        return block_type_heading1
    if header == "##":
        return block_type_heading2
    if header == "###":
        return block_type_heading3
    if header == "####":
        return block_type_heading4
    if header == "#####":
        return block_type_heading5
    if header == "######":
        return block_type_heading6
    raise Error("Something wrong with get_header_number")

def is_code(words):
    if words[0][0] != "`":
        return False
    if words[0][1] != "`":
        return False
    if words[0][2] != "`":
        return False
    if words[-1][-1] != "`":
        return False
    if words[-1][-2] != "`":
        return False
    if words[-1][-3] != "`":
        return False
    return True

def is_quote(lines):
    for line in lines:
        if line[0] != ">":
            return False
    return True
        
def is_unordered_list(lines):
    result = True
    for line in lines:
        if line.startswith("* "):
            continue
        if line.startswith("- "):
            continue
        else:
            return False
    return True
    
def is_ordered_list(lines):
    regex = r"^[0-9]*\.\ "
    for line in lines:
        found = re.findall(regex, line)
        if found == []:
            return False
    return True

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        new_node = block_to_html_node(block)
        nodes.append(new_node)
    parent = ParentNode("div", nodes, None)
    return parent

def block_to_html_node(block):
    type = block_to_block_type(block)
    if type == block_type_heading1:
        return heading1_to_html_node(block)
    if type == block_type_heading2:
        return heading2_to_html_node(block)
    if type == block_type_heading3:
        return heading3_to_html_node(block)
    if type == block_type_heading4:
        return heading4_to_html_node(block)
    if type == block_type_heading5:
        return heading5_to_html_node(block)
    if type == block_type_heading6:
        return heading6_to_html_node(block)
    if type == block_type_code:
        return code_to_html_node(block)
    if type == block_type_unordered_list:
        return unordered_list_to_html_node(block)
    if type == block_type_ordered_list:
        return ordered_list_to_html_node(block)
    if type == block_type_quote:
        return quote_to_html_node(block)
    if type == block_type_paragraph:
        return paragraph_to_html_node(block)

def heading1_to_html_node(block):
    text = block.lstrip(" #")
    children = text_to_children(text)
    return ParentNode("h1", children)

def heading2_to_html_node(block):
    text = block.lstrip(" ##")
    children = text_to_children(text)
    return ParentNode("h2", children)

def heading3_to_html_node(block):
    text = block.lstrip(" ###")
    children = text_to_children(text)
    return ParentNode("h3", children)

def heading4_to_html_node(block):
    text = block.lstrip(" ####")
    children = text_to_children(text)
    return ParentNode("h4", children)

def heading5_to_html_node(block):
    text = block.lstrip(" #####")
    children = text_to_children(text)
    return ParentNode("h5", children)

def heading6_to_html_node(block):
    text = block.lstrip(" ######")
    children = text_to_children(text)
    return ParentNode("h6", children)

def code_to_html_node(block):
    text = block[3:-3]
    children = text_to_children(text)
    code_block = ParentNode("code", children)
    return ParentNode("pre", [code_block])

def unordered_list_to_html_node(block):
    list = block.split("\n")
    html_list = []
    for item in list:
        text = item[2:]
        children = text_to_children(text)
        html_list.append(ParentNode("li", children))
    return ParentNode("ul", html_list)

def ordered_list_to_html_node(block):
    list = block.split("\n")
    html_list = []
    regex = r"^[0-9]*\.\ "
    for item in list:
        text = re.sub(regex, "", item)
        children = text_to_children(text)
        html_list.append(ParentNode("li", children))
    return ParentNode("ol", html_list)

def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)
    
def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        print(html_node)
        children.append(html_node)
    return children
