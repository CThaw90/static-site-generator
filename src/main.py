from textnode import TextNode, TextType
from htmlnode import LeafNode

import re

def text_node_to_html_node(text_node: TextNode):
    match text_node.text_type:
        case TextType.BOLD:
            return LeafNode('b', text_node.text)
        case TextType.LINK:
            return LeafNode('a', text_node.text, {'href': text_node.url})
        case TextType.ITALIC:
            return LeafNode('i', text_node.text)
        case TextType.CODE:
            return LeafNode('code', text_node.text)
        case TextType.IMAGE:
            return LeafNode('img', text_node.text, {'href': text_node.url})
        case TextType.NORMAL:
            return LeafNode(None, text_node.text)

    raise ValueError('Invalid text type')

def split_nodes_delimiter(nodes, delimiter, text_type):
    split_nodes_indexes = [(i, nodes[i].text.index(delimiter), nodes[i].text.rindex(delimiter)) for i in range(len(nodes)) if delimiter in nodes[i].text]
    split_nodes = []
    delimiter_length = len(delimiter)
    match delimiter:
        case '**':
            split_text_type = TextType.BOLD
        case '__':
            split_text_type = TextType.ITALIC
        case '`':
            split_text_type = TextType.CODE
        case _:
            split_text_type = TextType.NORMAL

    for split_node_indexes in split_nodes_indexes:
        (index, start, end) = split_node_indexes
        current_node = nodes[index]
        if start > 0:
            split_nodes.append(TextNode(current_node.text[:start], text_type))
        split_nodes.append(TextNode(current_node.text[start + delimiter_length:end], split_text_type))

        if end + delimiter_length < len(current_node.text):
            split_nodes.append(TextNode(current_node.text[end + delimiter_length:], text_type))

    return split_nodes

def extract_markdown_links(text):
    return re.findall(r'(?<!!)\[([^\[\]]*)]\(([^()]*)\)', text)

def extract_markdown_images(text):
    return re.findall(r'!\[([^\[\]]*)]\(([^()]*)\)', text)

def split_text_nodes(old_nodes: list[TextNode], text_type, split_function):
    split_nodes = []
    for node in old_nodes:
        extracted_nodes = split_function(node.text)
        start, end = 0, 0
        if extracted_nodes:
            for extracted in extracted_nodes:
                (name, url) = extracted
                start = node.text.index(name) - (1 if text_type == TextType.LINK else 2)
                split_nodes.append(TextNode(node.text[end:start], TextType.NORMAL))
                split_nodes.append(TextNode(name, text_type, url))
                end = node.text.index(url) + len(url) + 1

            if end < len(node.text):
                split_nodes.append(TextNode(node.text[end:], TextType.NORMAL))

    return split_nodes


def split_nodes_image(old_nodes):
    return split_text_nodes(old_nodes, TextType.IMAGE, extract_markdown_images)

def split_nodes_link(old_nodes):
    return split_text_nodes(old_nodes, TextType.LINK, extract_markdown_links)

def main():
    print(TextNode('Navigate to the Theezy Trader app', TextType.LINK, 'https://theezy-trader-da96c.ondigitalocean.app/'))


if __name__ == '__main__':
    main()