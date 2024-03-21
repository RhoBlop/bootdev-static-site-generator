import unittest

from htmlnode import HtmlNode, LeafNode, ParentNode

class TestHtmlNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HtmlNode(tag="image", props={"src": "https://google.com/placeholder.png", "style": "width: 50%"})
        self.assertEqual(node.props_to_html(), ' src="https://google.com/placeholder.png" style="width: 50%"')

    def test_leaf_to_html(self):
        node = LeafNode(content="google link", tag="a", props={"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">google link</a>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(content="Hello there")
        self.assertEqual(node.to_html(), "Hello there")

    def test_leaf_to_html_no_content_error(self):
        with self.assertRaises(ValueError) as e:
            LeafNode(content=None, tag="a", props={"href": "https://www.google.com"}).to_html()
        self.assertEqual(str(e.exception), "'content' attribute not provided for Leaf Node")

    def test_parent_to_html_no_tag_error(self):
        with self.assertRaises(ValueError) as e:
            ParentNode(tag=None, children=[LeafNode(tag="b", content="Bold text")]).to_html()
        self.assertEqual(str(e.exception), "'tag' attribute not provided for Parent Node")
    
    def test_parent_to_html_no_children_error(self):
        with self.assertRaises(ValueError) as e:
            ParentNode(tag="p", children=None).to_html()
        self.assertEqual(str(e.exception), "'children' attribute not provided for Parent Node")

    def test_parent_to_html_simple(self):
        node = ParentNode(
            tag="h2",
            children=[
                LeafNode(tag="b", content="Bold text"),
                LeafNode(content="Normal text"),
                LeafNode(tag="i", content="Italic text"),
                LeafNode(content="Normal text"),
            ]
        )
        self.assertEqual(node.to_html(), "<h2><b>Bold text</b>Normal text<i>Italic text</i>Normal text</h2>")

    def test_parent_to_html_nesting(self):
        node = ParentNode(
            tag="p",
            children=[
                ParentNode(tag="a", props={"href": "https://google.com"}, children=[
                    LeafNode(tag="b", props={"style": "color: blue"}, content="google"),
                    LeafNode(tag="i", props={"style": "color: red"}, content="link")
                ]),
                LeafNode(content="Normal text"),
                LeafNode(tag="i", props={"style": "color: yellow"}, content="Italic text"),
                LeafNode(content="Normal text"),
            ]
        )
        self.assertEqual(node.to_html(), '<p><a href="https://google.com"><b style="color: blue">google</b><i style="color: red">link</i></a>Normal text<i style="color: yellow">Italic text</i>Normal text</p>')


if __name__ == "__main__":
    unittest.main()