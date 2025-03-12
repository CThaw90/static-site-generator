class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def __repr__(self):
        return f'HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})'


class LeafNode(HTMLNode):

    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

        self.value = value
        self.tag = tag

    def to_html(self):
        if self.value is None:
            raise ValueError('value cannot be None')

        return f'<{self.tag}>{self.value}</{self.tag}>' if self.tag else self.value


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self):
        if not self.tag:
            raise ValueError('tag cannot be None')

        if not self.children:
            raise ValueError('children cannot be None')

        return f'<{self.tag}>{''.join(list(map(lambda child: child.to_html(), self.children)))}</{self.tag}>'
