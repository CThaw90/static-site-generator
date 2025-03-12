from textnode import TextNode, TextType
from htmlnode import LeafNode

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

def main():
    print(TextNode('Navigate to the Theezy Trader app', TextType.LINK, 'https://theezy-trader-da96c.ondigitalocean.app/'))


if __name__ == '__main__':
    main()