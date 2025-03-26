import unittest
from textnode import TextNode, TextType, text_node_to_html_node
from inline_markdown import extract_markdown_images, extract_markdown_links, split_nodes_images, split_node_links

# ---- BEGIN BOOT.DEV TESTS

import unittest
from htmlnode import LeafNode, ParentNode, HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

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

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )
        
        
        def test_extract_markdown_images(self):
            matches = extract_markdown_images(
                "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
            )
            self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
        
    # END extract_markdown_images tests
        
    # BEGIN extract_markdown_links tests    
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
            )
        
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)
        # ("to youtube", "https://www.youtube.com/@bootdotdev")
        
    # END extract_markdown_links tests
    
    # BEGIN 
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_images([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    
    def test_split_links(self):
        node = TextNode("This is text with a link [alternative text hello](https://www.boot.dev/u/bigfaxmachine)", TextType.TEXT)
        
        new_nodes = split_node_links([node])
        print(f"new_nodes = {new_nodes}")
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("alternative text hello", TextType.LINK, "https://www.boot.dev/u/bigfaxmachine")
            ],
            new_nodes
        )
        
    # When passing a TextNode with no links or images, we must get a list back with the original TextNode in it
    def test_split_images_no_links(self):    
        
        # Checking our split node links function
        node = TextNode("This is a text node with absolutely no links or image", TextType.TEXT)
        new_nodes = split_node_links([node])
        
        self.assertListEqual(
            [node],
            new_nodes            
        )
        
        # Now we are checking our split node images function
        node = TextNode("This is a text node with absolutely no links or image", TextType.TEXT)
        new_nodes = split_nodes_images([node])
        
        self.assertListEqual(
            [node],
            new_nodes            
        )
        

if __name__ == "__main__":
    unittest.main()

# ---- END BOOT.DEV TESTS

# ---- BEGIN MY TESTS
# I am going to use Boot.dev's tests instead


# class TestConverts(unittest.TestCase):
    
#     # BEGIN text_node_to_html_node tests
#     def test_text(self):
#         node = TextNode("This is a text node", TextType.TEXT)
#         html_node = text_node_to_html_node(node)
#         self.assertEqual(html_node.tag, None)
#         self.assertEqual(html_node.value, "This is a text node")
        
#     # Test that a Image text node correctly has a src attribute
#     def test_text_node_anchor_with_url(self):
#         node = TextNode("This is a text node", TextType.IMAGE, "https://boot.dev")
#         html_node = text_node_to_html_node(node)
#         self.assertEqual(html_node.tag, "img")
#         print(html_node.props)
#         print(html_node)
#         self.assertEqual(html_node.props['src'], "https://boot.dev")
        
#     def test_that_text_node_still_has_url_properties(self):
#           node = TextNode("This is a text node", TextType.TEXT, "https://boot.dev")
#           self.assertEqual(node.url, "https://boot.dev")
        
        
#     def test_anchor_test_node_has_href(self):
#         node = TextNode("This is a text node", TextType.LINK, "https://boot.dev")
#         html_node = text_node_to_html_node(node)
#         self.assertEqual(html_node.tag, "a")
#         self.assertEqual(html_node.props['href'], "https://boot.dev")
#         print(html_node)
        
#     def test_anchor_node_has_proper_inner_value(self):
#         node = TextNode("This is a text node", TextType.LINK, "https://boot.dev")
#         html_node = text_node_to_html_node(node)
#         self.assertEqual(html_node.value, "This is a text node")
        
#     def test_image_node_has_proper_inner_value(self):
#         node = TextNode("This is a text node", TextType.IMAGE, "https://boot.dev")
#         html_node = text_node_to_html_node(node)
#         self.assertEqual(html_node.value, "This is a text node")
        
#     def test_all_nodes_have_proper_inner_value(self):
#         all_nodes_to_be_checked = [
#             TextNode("This is a text node", TextType.IMAGE, "https://boot.dev"),
#             TextNode("This is a text node", TextType.LINK, "https://boot.dev"),
#             TextNode("This is a text node", TextType.BOLD),
#             TextNode("This is a text node", TextType.ITALIC),
#             TextNode("This is a text node", TextType.CODE),
#             TextNode("This is a text node", TextType.TEXT)
#         ]
        
#         for node in all_nodes_to_be_checked:
#             html_node = text_node_to_html_node(node)
#             self.assertEqual(html_node.value, "This is a text node",
#                              f"failed for node type {node.text_type}")
        
#     # END text_node_to_html_node tests
        
#     # BEGIN extract_markdown_images tests
#     def test_extract_markdown_images(self):
#         matches = extract_markdown_images(
#             "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
#         )
#         self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
        
#     # END extract_markdown_images tests
        
#     # BEGIN extract_markdown_links tests    
#     def test_extract_markdown_links(self):
        
#         test_cases = [ 
#                       ("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")  
#         ]
        
        
#         matches = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
        
#         self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)
#         # ("to youtube", "https://www.youtube.com/@bootdotdev")
        
        
    # END extract_markdown_links tests
    
# ---- END MY TESTS
        
        