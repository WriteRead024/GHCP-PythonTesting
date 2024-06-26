from os import path
import unittest


class TemplateFile(unittest.TestCase):
    def test_path_basename(self):
        filename = path.basename(__file__)
        self.assertEqual(filename, "test_template_filename.py")

if __name__ == "__main__":
    unittest.main()
