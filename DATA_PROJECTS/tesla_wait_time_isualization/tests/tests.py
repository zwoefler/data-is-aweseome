import unittest
from bs4 import BeautifulSoup
import json
import sys
from io import StringIO
from tesla_price_visualizer import (
    extract_json_from_html,
    read_html_file,
    print_json_to_console,
)


class ExtractJSONFromHTML(unittest.TestCase):
    def test_extract_json_from_model3_2019(self):
        # Load MOdel3 2019 HTML
        with open(
            "tests/test_data/test_html_raw_de_DE_model3_20190327102025.html"
        ) as f:
            html_content = f.read()

        json_data = extract_json_from_html(html_content)
        self.assertIsInstance(json_data, (dict, list))

    def test_DSServices_is_key_in_JSON(self):
        """
        A JSON string is hidden inside the JSON that has the Key 'DSServices'
        To make sure the JSON extractio nwas correct, check if the key
        'DSServices' is inside the JSON
        """
        with open(
            "tests/test_data/test_html_raw_de_DE_model3_20190327102025.html"
        ) as f:
            html_content = f.read()

        json_data = extract_json_from_html(html_content)
        self.assertIn("DSServices", json_data)


class TestReadHTMLFile(unittest.TestCase):
    def test_read_html_file(self):
        html_file_path = "tests/test_data/test_html.html"

        html_content = read_html_file(html_file_path)
        self.assertIsInstance(html_content, str)

    def test_import_is_valid_HTML(self):
        html_file_path = "tests/test_data/test_html.html"

        html_content = read_html_file(html_file_path)

        self.assertTrue(BeautifulSoup(html_content, "html.parser"))


class TestPrintJSONToConsole(unittest.TestCase):
    def setUp(self):
        self.saved_stdout = sys.stdout
        self.output = StringIO()
        sys.stdout = self.output

    def tearDown(self):
        sys.stdout = self.saved_stdout

    def test_print_json_to_console(self):
        test_dict = {"key1": "value1", "key2": "value2"}

        print_json_to_console(test_dict)
        printed_output = self.output.getvalue()

        try:
            parsed_json = json.loads(printed_output)
            self.assertIsInstance(parsed_json, dict)
        except json.JSONDecodeError:
            self.fail("Output is not a valid JSON string")
