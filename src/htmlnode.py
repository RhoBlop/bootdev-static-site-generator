class HtmlNode:
    def __init__(self, tag=None, props=None):
        self.tag = tag
        self.props = props

    def __repr__(self):
        return f"HtmlNode(\n    tag: <{self.tag}>,\n    props_html:{self.props_to_html()}\n)"

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props is None:
            return ""
        
        string = ""
        for key in self.props:
            string += f' {key}="{self.props[key]}"'
        return string
    

class LeafNode(HtmlNode):
    def __init__(self, content, tag=None, props=None):
        super().__init__(tag=tag, props=props)
        self.content = content

    def __repr__(self):
        return f'LeafNode(tag: {"None" if not self.tag else f"<{self.tag}>"}, content: "{self.content}", props_html: "{self.props_to_html()}")'

    def to_html(self):
        if self.content is None:
            raise ValueError("'content' attribute not provided for Leaf Node")
        if self.tag is None:
            return self.content
        
        return f"<{self.tag}{self.props_to_html()}>{self.content}</{self.tag}>"
    

class ParentNode(HtmlNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, props=props)
        self.children = children

    def __repr__(self):
        str_children = ""
        if self.children:
            for child in self.children:
                str_children += (" " * 8) + repr(child) + "\n"
        return f'ParentNode(\n    tag: <{self.tag}>,\n    props_html: "{self.props_to_html()}",\n    children:[\n{str_children}    ]\n)'
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("'tag' attribute not provided for Parent Node")
        if self.children is None:
            raise ValueError("'children' attribute not provided for Parent Node")
        
        html = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            html += child.to_html()
        html += f"</{self.tag}>"

        return html