import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode(text="This is a text node", text_type="bold")
        node2 = TextNode(text="This is a text node", text_type="bold")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode(text="Alternative Image Text", text_type="image", url="https://letsenhance.io/static/8f5e523ee6b2479e26ecc91b9c25261e/1015f/MainAfter.jpg")
        node2 = TextNode(text="Not an image", text_type="italic")
        self.assertNotEqual(node, node2)

    def test_none_url(self):
        node = TextNode(text="Alternative text that should appear", text_type="image")
        self.assertIsNone(node.url)

    def test_invalid_text_type(self):
        with self.assertRaises(ValueError) as e:
            TextNode(text="Big Text", text_type="quote")
        self.assertEqual(str(e.exception), "Invalid text type for TextNode")


if __name__ == "__main__":
    unittest.main()