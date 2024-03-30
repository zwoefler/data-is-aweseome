import unittest
import subprocess

class TestTeslaPriceVisualizerCLI(unittest.TestCase):
    def test_help_option(self):
        output = subprocess.check_output(["python3", "tesla_price_visualizer.py", "--help"], stderr=subprocess.STDOUT, universal_newlines=True)

        self.assertIn("--extract_json", output)
        self.assertIn("path_to_HTML", output)
        self.assertIn("usage: tesla_price_visualizer", output)


class TestFunctionality(unittest.TestCase):
    def test_can_extract_json_from_html(self):
        

if __name__ == '__main__':
    unittest.main()
