import unittest

from textnode import TextNode, TextType
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("link", "Decent Backend Courses", None, {"href": "https://boot.dev"} )
        node2 = HTMLNode("link", "Decent Backend Courses", None, {"href": "https://boot.dev"} )
        self.assertEqual(node, node2)
        
    def test_eq_false(self):
        node = HTMLNode("link", "Decent Backend Courses", None, {"href": "https://boot.dev"} )
        node2 = HTMLNode("bink", "Decent Backend Courses", None, {"href": "https://boot.dev"} )
        self.assertNotEqual(node, node2)
        
    def test_eq_false(self):
        node = HTMLNode("link", "Decent Backend Courses", None, {"href": "httpsss://boot.dev"} )
        node2 = HTMLNode("bink", "Decent Backend Courses", None, {"href": "https://boot.dev"} )
        self.assertNotEqual(node, node2)
        
    def test_repr(self):
        tag = "link"
        value = "Decent Backend Courses"
        children = None
        props = {"href": "https://boot.dev"}
        
        
        node = HTMLNode(tag, value, children, props)
        self.assertEqual(
            f"HTMLNode({tag}, {value}, {children}, {props})",
            repr(node)
        )
        
        