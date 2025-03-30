class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        result = []
        for i in self.props:
            value = self.props[i]
            result.append(f' {i}="{value}"')
        return "".join(result)
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError("LeafNode missing value")
        elif self.tag == None:
            return f"{self.value}"
        props_string = " ".join(f'{key}="{value}"' for key, value in self.props.items()) if self.props else ""
        return f"<{self.tag}{(' ' + props_string) if props_string else ''}>{self.value}</{self.tag}>"
