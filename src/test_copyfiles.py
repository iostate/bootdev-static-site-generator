import unittest
from copyfiles import copy_files, delete_all_content

# class TestCopyFiles(unittest.TestCase):
#     def test_copy_files(self):
#         source = "/Users/qmtruong92/workspace/github.com/iostate/bootdev-static-site-generator/static"
#         destination =  "/Users/qmtruong92/workspace/github.com/iostate/bootdev-static-site-generator/public"
#         copy_success = copy_files(source, destination)
#         self.assertEqual(True, copy_success)
        
#     def test_delete_files(self):
#         delete_this =  "/Users/qmtruong92/workspace/github.com/iostate/bootdev-static-site-generator/public"
#         delete_all_content(delete_this)