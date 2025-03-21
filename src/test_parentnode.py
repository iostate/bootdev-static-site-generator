import unittest
from leafnode import LeafNode
from parentnode import ParentNode

class TestParentNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_with_multiple_children(self):
        # Create several children, mixing LeafNodes with and without tags.
        child1 = LeafNode("b", "Bold")
        child2 = LeafNode(None, "Normal")
        child3 = LeafNode("i", "italic")
        child4 = LeafNode(None, "more normal")
        parent_node = ParentNode("p", [child1, child2, child3, child4])
        expected = "<p><b>Bold</b>Normal<i>italic</i>more normal</p>"
        self.assertEqual(parent_node.to_html(), expected)
    
    def test_to_html_with_nested_parent_nodes(self):
        # Test deeper nesting: a ParentNode within a ParentNode.
        leaf_node = LeafNode("b", "nested bold")
        child_node = ParentNode("span", [leaf_node])
        parent_node = ParentNode("div", [child_node])
        expected = "<div><span><b>nested bold</b></span></div>"
        self.assertEqual(parent_node.to_html(), expected)
    
    def test_to_html_missing_tag_raises_error(self):
        # Creating a ParentNode with no tag should raise a ValueError.
        with self.assertRaises(ValueError) as context:
            node = ParentNode(None, [LeafNode("span", "child")])
            node.to_html()
        self.assertEqual(str(context.exception), "ParentNode must have a tag")
    
    def test_to_html_missing_children_raises_error(self):
        # Creating a ParentNode with children set to None should raise a ValueError.
        with self.assertRaises(ValueError) as context:
            node = ParentNode("div", None)
            node.to_html()
        self.assertEqual(str(context.exception), "ParentNode.children does not have a value")
    
    def test_to_html_with_props(self):
        # Test that properties (props) are correctly added to a LeafNode,
        # and then that HTML is generated correctly.
        props = {"class": "test", "id": "123"}
        child_node = LeafNode("span", "child", props=props)
        parent_node = ParentNode("div", [child_node])
        # The expected string should include the attributes.
        # Depending on your implementation of get_attributes_string,
        # adjust the expected ordering if necessary.
        expected = '<div><span class="test" id="123">child</span></div>'
        self.assertEqual(parent_node.to_html(), expected)

if __name__ == "__main__":
    unittest.main()
