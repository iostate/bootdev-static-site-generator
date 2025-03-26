import re
from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode
            
 
# boot.dev's solution       
def split_nodes_delimiter(old_nodes, delimiter, text_type: TextNode) -> list[TextNode]:
    new_nodes = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        split_nodes = []
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0: # normal text
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
        
        return new_nodes
            
def extract_markdown_images(text):
    found = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    
    return found

def extract_markdown_links(text):
    found = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    
    return found


# my solution
# def split_nodes_delimiter(old_nodes, delimiter, text_type: TextNode) -> list[TextNode]:
#     result = []
#     for node in old_nodes:
#         if node.text_type != TextType.TEXT: 
#             result.append(node)
#             continue
        
#         text = node.text
        
#         if delimiter not in text:
#             result.append(node)
#             continue
        
#         current_text = text
#         while delimiter in current_text:
#             # get first index of delimiter
#             start_index = current_text.find(delimiter)
            
#             # get second index of delimiter
#             remaining_text = current_text[start_index + len(delimiter):]
#             if delimiter not in remaining_text:
#                 raise Exception("second delimiter not found")
            
#             end_index = remaining_text.find(delimiter)
            
#             before_text = current_text[:start_index]
#             if before_text:
#                 result.append(TextNode(before_text, TextType.TEXT))
                
#             middle_text = current_text[start_index +len(delimiter) : start_index + len(delimiter) + end_index]
#             if middle_text:
#                 result.append(TextNode(middle_text, text_type))
                
#             after_second_delimiter = start_index + len(delimiter) + end_index + len(delimiter)
            
#             current_text = current_text[after_second_delimiter:]
            
#         if current_text:
#             result.append(TextNode(current_text, TextType.TEXT))
            
#         return result
    
    
    
    
    
    
    
    