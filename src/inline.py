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

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        original_text = node.text
        extracted = extract_markdown_images(original_text)
        if len(extracted) == 0:
            new_nodes.append(node)
            continue
        for image in extracted:
            parts = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if parts[0] != "":
                new_nodes.append(TextNode(parts[0], text_type_text))
            new_nodes.append(TextNode(image[0], text_type_image, image[1]))
            print(parts)
            original_text = parts[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        original_text = node.text
        extracted = extract_markdown_links(original_text)
        if len(extracted) == 0:
            new_nodes.append(node)
            continue
        for link in extracted:
            parts = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if parts[0] != "":
                new_nodes.append(TextNode(parts[0], text_type_text))
            new_nodes.append(TextNode(link[0], text_type_link, link[1]))
            print(parts)
            original_text = parts[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes
                
def extract_markdown_images(text):
    regex = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(regex, text)
    return matches

def extract_markdown_links(text):
    regex = r"\[(.*?)\]\((.*?)\)"
    matches = re.findall(regex, text)
    return matches
