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

    def __init__(self, value, tag=None, props=None):
        super().__init__(tag, value, None, props)

        if value is None:
            raise ValueError('value cannot be None')

        self.value = value
        self.tag = tag

    def to_html(self):
        return f'<{self.tag}>{self.value}</{self.tag}>' if self.tag else self.value
