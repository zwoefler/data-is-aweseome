import unittest
import subprocess
import json


class TestTeslaPriceVisualizerCLI(unittest.TestCase):
    def test_help_option(self):
        output = subprocess.check_output(
            ["python3", "tesla_price_visualizer.py", "--help"],
            stderr=subprocess.STDOUT,
            universal_newlines=True,
        )

        self.assertIn("--extract_json", output)
        self.assertIn("path_to_HTML", output)
        self.assertIn("usage: tesla_price_visualizer", output)


class TestFunctionality(unittest.TestCase):
    def test_can_extract_json_from_html(self):
        # James heard about hte script and has a valid HTML file
        html_file_path = (
            "tests/test_data/test_html_raw_de_DE_model3_20190327102025.html"
        )

        # James calls the script with the valid HTML
        output = subprocess.check_output(
            ["python3", "tesla_price_visualizer.py", "--extract_json", html_file_path],
            stderr=subprocess.STDOUT,
            universal_newlines=True,
        )

        # James notices the program tells him that the JSON was successfully extracted!
        try:
            json_data = json.loads(output)
        except json.JSONDecodeError:
            self.fail("Output is not a valid JSON string")

        self.assertIsInstance(json_data, dict)


if __name__ == "__main__":
    unittest.main()
