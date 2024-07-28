from textnode import TextNode

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        result = ""
        for key, value in self.props.items():
            result += f" {key}=\"{value}\""
        return result

    def __repr__(self):
        return f"{self.tag}, {self.value}, {self.children}, {self.props}"

    def __str__(self):
        return f"{self.tag}, {self.value}, {self.children}, {self.props}"    
