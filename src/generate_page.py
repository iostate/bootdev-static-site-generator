import re
import os
from markdown_blocks import markdown_to_html_node
from markdown_blocks import markdown_to_blocks
def extract_title(markdown):
    filtered_blocks = markdown_to_blocks(markdown)
    for block in filtered_blocks:
        match = re.match(r"^#\s(.+)", block)  
        if match:
            return match.group(1) 
        
    return None
        
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page {from_path} to {dest_path} using {template_path}")
    
    # Read markdown file
    md_file = open(from_path, "r")
    md = md_file.read()
    
    # Read template file
    template_file = open(template_path, "r")
    template = template_file.read()
    
    # Convert markdown to html
    md_html_node = markdown_to_html_node(md)
    content = md_html_node.to_html()
    
    # Extract title
    title = extract_title(md)
    
    # Replace the title and content
    replace_title = re.sub("{{ Title }}", title, template)
    replace_content = re.sub("{{ Content }}", content, replace_title)
    
    # Ensure that the directory exists before attempting to create destination
    # file
    dest_dir = os.path.dirname(dest_path)
    os.makedirs(dest_dir, exist_ok=True)
    
    # Create a new file, replace content of it
    destination = open(dest_path, "w+")
    destination.write(replace_content)
    
    return

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.makedirs(dest_dir_path)
        
    list_content_dir = os.listdir(dir_path_content)
    
    for filename in list_content_dir:
        file_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        
        # Recurse if it is a directory
        if os.path.isdir(file_path): 
            # Create a directory if needed
            if not os.path.exists(dest_path):
                os.makedirs(dest_path)
            generate_pages_recursive(file_path, template_path, dest_path)
        # Generate page
        else:
            # Save as an HTML file
            dest_path_without_ext, _ = os.path.splitext(dest_path)
            print(f"dest_path_without_ext = {dest_path_without_ext}")
            dest_path_as_html = dest_path_without_ext + ".html"
            generate_page(file_path, template_path, dest_path_as_html)
    