import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("Alternative Image Text", "image", "https://letsenhance.io/static/8f5e523ee6b2479e26ecc91b9c25261e/1015f/MainAfter.jpg")
        node2 = TextNode("Not an image", "italic")
        self.assertNotEqual(node, node2)

    def test_none_url(self):
        node = TextNode("Alternative text that should appear", "image")
        self.assertIsNone(node.url)

    def test_invalid_text_type(self):
        with self.assertRaises(ValueError) as e:
            node = TextNode("Big Text", "quote")
        self.assertEqual(str(e.exception), "Invalid text type for TextNode")


if __name__ == "__main__":
    unittest.main()