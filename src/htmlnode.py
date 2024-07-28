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


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("LeafNode missing a value")
        if self.tag == None:
            return self.value
        if self.props == None:
            result = f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            for key, value in self.props.items():
                result = f"<{self.tag} {key}=\"{value}\">{self.value}</{self.tag}>"
        return result

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("ParentNode missing a tag")
        if self.children == None or len(self.children) == 0:
            raise ValueError("ParentNode missing children")

        result = f"<{self.tag}>"
        for child in self.children:
            result += child.to_html()
        result += f"</{self.tag}>"
        return result    
