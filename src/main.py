from textnode import TextNode
from copyfiles import copy_files_recursive

def main():
    source = "/Users/qmtruong92/workspace/github.com/iostate/bootdev-static-site-generator/static"
    destination =  "/Users/qmtruong92/workspace/github.com/iostate/bootdev-static-site-generator/public"
    copy_files_recursive(source, destination)
    

main()
