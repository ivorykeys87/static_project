class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        if self.tag is None:
            if self.value is None:
                raise ValueError("HTMLNode must have either a tag or a value")
            return self.value
        
        props_html = ""
        if self.props:
            for key, value in self.props.items():
                props_html += f' {key}="{value}"'
        
        if not self.children:
            return f"<{self.tag}{props_html}></{self.tag}>"
        
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        
        return f"<{self.tag}{props_html}>{children_html}</{self.tag}>"
    
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
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError("LeafNode missing value")
        elif self.tag == None:
            return f"{self.value}"
        props_string = " ".join(f'{key}="{value}"' for key, value in self.props.items()) if self.props else ""
        return f"<{self.tag}{(' ' + props_string) if props_string else ''}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("No Tag Present")
        elif self.children == None:
            raise ValueError("Missing Children")
        return f"<{self.tag}>{''.join(child.to_html() for child in self.children)}</{self.tag}>"
