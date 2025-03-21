from htmlnode import HTMLNode

# html tag
# self.tag = tag
# value inside tag
# self.value = value
# no children here,
# self.children = children
# attributes of html tag
# self.props = {} if props is None else props

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)
        
    def to_html(self):
        # all leaf nodes must have value
        if self.value == None:
            raise ValueError("all leaf nodes must have a value")
        
        # if no tag, return raw text
        if self.tag == None:
            return self.value
        
        if self.props != None:
            attributes_string = " " + " ".join(map(lambda kv: f"{kv[0]}=\"{kv[1]}\"", self.props.items()))
            return f"<{self.tag}{attributes_string}>{self.value}</{self.tag}>"
        
        return f"<{self.tag}>{self.value}</{self.tag}>"