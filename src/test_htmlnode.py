import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        node = HTMLNode('h1', 'This is a header', [], {'class':'header'})
        node2 = HTMLNode('p', 'This is a paragraph', [], {'style':'color:red'})
        self.assertRaises(NotImplementedError, node.to_html)
        self.assertRaises(NotImplementedError, node2.to_html)
