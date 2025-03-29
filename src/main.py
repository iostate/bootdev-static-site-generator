import sys
from textnode import TextNode
from copyfiles import copy_files_recursive
from generate_page import generate_page, generate_pages_recursive

def main():
    
    
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    
    
    
    # Copy all the files from static/ to public/
    source = "/Users/qmtruong92/workspace/github.com/iostate/bootdev-static-site-generator/static"
    destination =  "/Users/qmtruong92/workspace/github.com/iostate/bootdev-static-site-generator/docs"
    copy_files_recursive(source, destination)
    
    # Convert all the file contents inside of content/ directory (MD files) to HTML,
    # then save as HTML files inside of public
    dir_path_content = "/Users/qmtruong92/workspace/github.com/iostate/bootdev-static-site-generator/content"
    template_path = "/Users/qmtruong92/workspace/github.com/iostate/bootdev-static-site-generator/template.html"
    dest_dir_path = "/Users/qmtruong92/workspace/github.com/iostate/bootdev-static-site-generator/docs"
    generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath)
    

main()
