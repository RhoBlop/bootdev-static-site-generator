valid_text_types = ["text", "italic", "bold", "code", "link", "image"]

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.url = url

        if text_type in valid_text_types:
            self.text_type = text_type
        else:
            raise ValueError("Invalid text type for TextNode")

    def __eq__(self, other) -> bool:
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"