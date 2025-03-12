import unittest

from main import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter_bold(self):
        nodes_bold = [
            TextNode('This will be one **HELL** of a journey', TextType.NORMAL),
            TextNode('Get **BACK** MF yaon know me like that', TextType.NORMAL),
            TextNode('Where the **HOES** at?', TextType.NORMAL)
        ]

        new_nodes_bold = [
            TextNode('This will be one ', TextType.NORMAL),
            TextNode('HELL', TextType.BOLD),
            TextNode(' of a journey', TextType.NORMAL),
            TextNode('Get ', TextType.NORMAL),
            TextNode('BACK', TextType.BOLD),
            TextNode(' MF yaon know me like that', TextType.NORMAL),
            TextNode('Where the ', TextType.NORMAL),
            TextNode('HOES', TextType.BOLD),
            TextNode(' at?', TextType.NORMAL)
        ]

        self.assertEqual(split_nodes_delimiter(nodes_bold, '**', TextType.NORMAL), new_nodes_bold)


    def test_split_nodes_delimiter_italic(self):

        nodes_italic = [
            TextNode('__Wish upon a star__', TextType.NORMAL),
            TextNode('__Notes:__ Will revisit this approach when it is time to scale', TextType.NORMAL),
            TextNode('This will be it. __(Hedging against all bets)__', TextType.NORMAL)
        ]

        new_nodes_italic = [
            TextNode('Wish upon a star', TextType.ITALIC),
            TextNode('Notes:', TextType.ITALIC),
            TextNode(' Will revisit this approach when it is time to scale', TextType.NORMAL),
            TextNode('This will be it. ', TextType.NORMAL),
            TextNode('(Hedging against all bets)', TextType.ITALIC)
        ]

        self.assertEqual(split_nodes_delimiter(nodes_italic, '__', TextType.NORMAL), new_nodes_italic)


    def test_split_nodes_delimiter_code(self):

        nodes_code = [
            TextNode('You must include the environment variable `PATH` in your shell', TextType.NORMAL),
            TextNode('Consider the following Array method `Array.prototype.some()`', TextType.NORMAL),
            TextNode('Remove the `console.log()` statement', TextType.NORMAL)
        ]

        new_nodes_code = [
            TextNode('You must include the environment variable ', TextType.NORMAL),
            TextNode('PATH', TextType.CODE),
            TextNode(' in your shell', TextType.NORMAL),
            TextNode('Consider the following Array method ', TextType.NORMAL),
            TextNode('Array.prototype.some()', TextType.CODE),
            TextNode('Remove the ', TextType.NORMAL),
            TextNode('console.log()', TextType.CODE),
            TextNode(' statement', TextType.NORMAL)
        ]

        self.assertEqual(split_nodes_delimiter(nodes_code, '`', TextType.NORMAL), new_nodes_code)

        nodes = [TextNode("This is text with a `code block` word", TextType.NORMAL)]
        new_nodes = [
            TextNode('This is text with a ', TextType.NORMAL),
            TextNode('code block', TextType.CODE),
            TextNode(' word', TextType.NORMAL),
        ]

        self.assertEqual(split_nodes_delimiter(nodes, '`', TextType.NORMAL), new_nodes)