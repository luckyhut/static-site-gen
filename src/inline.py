from textnode import TextNode
import re

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if delimiter not in node.text:
            new_nodes.append(node)
        else:
            print(node.text.count(delimiter))
            if node.text.count(delimiter) % 2 != 0:
                raise Exception("Uneven number of delimiters")
            split_text = node.text.split(delimiter)
            for i in range(len(split_text)):
                if i % 2 == 1:
                    new_nodes.append(TextNode(split_text[i], text_type))
                else:
                    if split_text[i] != "":
                        new_nodes.append(TextNode(split_text[i], text_type_text))
    return new_nodes

def extract_markdown_images(text):
    regex = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(regex, text)
    return matches

def extract_markdown_links(text):
    regex = r"\[(.*?)\]\((.*?)\)"
    matches = re.findall(regex, text)
    return matches
