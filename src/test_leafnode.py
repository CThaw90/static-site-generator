import unittest

from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode(None, 'This is a text node')
        p_node = LeafNode('p', 'This is a paragraph')
        h1_node = LeafNode('h1', 'This is a header')
        self.assertEqual(node.to_html(), 'This is a text node')
        self.assertEqual(p_node.to_html(), '<p>This is a paragraph</p>')
        self.assertEqual(h1_node.to_html(), '<h1>This is a header</h1>')

    def test_init(self):
        self.assertRaises(ValueError, LeafNode().to_html)