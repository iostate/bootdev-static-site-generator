from htmlnode import HTMLNode



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
        
        
        
        
        
        
    
    