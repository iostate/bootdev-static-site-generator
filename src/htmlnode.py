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
        print(f"result = {result}")
        return result 
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
    def get_attributes_string(self):
        if self.props != None:
            return " " + " ".join(map(lambda kv: f"{kv[0]}=\"{kv[1]}\"", self.props.items()))
        
        return ""
            
        
        