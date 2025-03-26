class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props
        
    # child classes will override this
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        result = " " +" ".join(map(lambda kv: f"{kv[0]}=\"{kv[1]}\"", self.props.items()))
        return result 
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
    def get_attributes_string(self):
        if self.props != None:
            return " " + " ".join(map(lambda kv: f"{kv[0]}=\"{kv[1]}\"", self.props.items()))
        
        return ""
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children: list[HTMLNode], props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("ParentNode must have a tag")
        
        if self.children == None:
            raise ValueError("ParentNode.children does not have a value")
        
        children_nodes = self.get_children_node_html_string(self.get_html_string, self.children, "")
        attributes_string = self.get_attributes_string()
        return f"<{self.tag}{attributes_string}>{children_nodes}</{self.tag}>"
    
    def get_html_string(self, initial, node):
        
        if node.children:
            return node.to_html()
        else:
            if node.tag == None:
                return initial + node.value
            attributes_string = node.get_attributes_string()
            return initial + f"<{node.tag}{attributes_string}>{node.value}</{node.tag}>"
    
    def get_children_node_html_string(self, func, children: list[HTMLNode], initial):
        if not children:
            return initial
        else:
            new_initial = func(initial, children[0])
            return self.get_children_node_html_string( func, children[1:], new_initial)
        
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
            
        
        