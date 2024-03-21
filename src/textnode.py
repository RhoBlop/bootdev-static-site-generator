from htmlnode import LeafNode

valid_text_types = ["text", "bold", "italic", "code", "link", "image"]

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.url = url

        if text_type in valid_text_types:
            self.text_type = text_type
        else:
            raise ValueError("Invalid text type for TextNode")

    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
        
    
def text_node_to_leaf_node(text_node: TextNode):
    text_type = text_node.text_type
    if text_type == "text":
        return LeafNode(text_node.text)
    if text_type == "bold":
        return LeafNode(text_node.text, "b")
    if text_type == "italic":
        return LeafNode(text_node.text, "i")
    if text_type == "code":
        return LeafNode(text_node.text, "code")
    if text_type == "link":
        return LeafNode(text_node.text, "a", {"href": text_node.url})
    if text_type == "image":
        return LeafNode("", "img", {"src": text_node.url, "alt": text_node.text})