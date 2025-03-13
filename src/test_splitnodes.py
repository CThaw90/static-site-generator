from main import split_nodes_link, split_nodes_image
from textnode import TextNode, TextType

import unittest


class TestSplitNodes(unittest.TestCase):
    def test_split_nodes_link(self):
        text_link_nodes = [
            TextNode('This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)', TextType.NORMAL),
        ]

        new_link_nodes = split_nodes_link(text_link_nodes)
        matches = [
            TextNode("This is text with a link ", TextType.NORMAL),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.NORMAL),
            TextNode(
                "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
            )
        ]
        self.assertListEqual(new_link_nodes, matches)


    def test_split_nodes_image(self):
        text_image_nodes = [
            TextNode('This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)', TextType.NORMAL),
        ]

        new_text_image_nodes = split_nodes_image(text_image_nodes)
        matches = [
            TextNode("This is text with an ", TextType.NORMAL),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.NORMAL),
            TextNode(
                "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
            )
        ]

        self.assertListEqual(new_text_image_nodes, matches)