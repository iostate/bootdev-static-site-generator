from textnode import TextNode
from copyfiles import copy_files_recursive
from generate_page import generate_page, generate_pages_recursive

def main():
    
    # Copy all the files from static/ to public/
    source = "/Users/qmtruong92/workspace/github.com/iostate/bootdev-static-site-generator/static"
    destination =  "/Users/qmtruong92/workspace/github.com/iostate/bootdev-static-site-generator/public"
    copy_files_recursive(source, destination)
    # generate_page("/Users/qmtruong92/workspace/github.com/iostate/bootdev-static-site-generator/content/index.md", "/Users/qmtruong92/workspace/github.com/iostate/bootdev-static-site-generator/template.html", "/Users/qmtruong92/workspace/github.com/iostate/bootdev-static-site-generator/public/index.html")
    
    # Convert all the file contents inside of content/ directory (MD files) to HTML,
    # then save as HTML files inside of public
    dir_path_content = "/Users/qmtruong92/workspace/github.com/iostate/bootdev-static-site-generator/content"
    template_path = "/Users/qmtruong92/workspace/github.com/iostate/bootdev-static-site-generator/template.html"
    dest_dir_path = "/Users/qmtruong92/workspace/github.com/iostate/bootdev-static-site-generator/public"
    generate_pages_recursive(dir_path_content, template_path, dest_dir_path)
    

main()
