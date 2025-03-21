import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        
    def test_lead_to_html_link(self):
        node = LeafNode("link", "Decent Backend Courses", {"href": "https://boot.dev", "rel": "stylesheet"})
        self.assertEqual(node.to_html(), "<link href=\"https://boot.dev\" rel=\"stylesheet\">Decent Backend Courses</link>")