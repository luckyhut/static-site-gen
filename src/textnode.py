class TextNode:
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        result = True
        if self.text != other.text:
            result = False
        if self.text_type != other.text_type:
            result = False
        if self.url != other.url:
            result = False
        return result

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

