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
    @classmethod
    def setUpClass(cls) -> None:
        with open(
            "tests/test_data/test_html_raw_de_DE_model3_20190327102025.html"
        ) as f:
            cls.html_content = f.read()

    def test_extract_json_from_model3_2019(self):
        json_data = extract_json_from_html(self.html_content)
        self.assertIsInstance(json_data, (dict, list))

    def test_DSServices_is_key_in_JSON(self):
        """
        A JSON string is hidden inside the JSON that has the Key 'DSServices'
        To make sure the JSON extractio nwas correct, check if the key
        'DSServices' is inside the JSON
        """
        json_data = extract_json_from_html(self.html_content)
        self.assertIn("DSServices", json_data)

    def test_i18n_is_key_in_JSON(self):
        """
        The key i18n needs to be available as key in the JSON.
        It is hidden as an escaped JSON string inside the JSON
        """
        json_data = extract_json_from_html(self.html_content)
        self.assertIn("i18n", json_data)


class TestReadHTMLFile(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html_file_path = "tests/test_data/test_html.html"
        cls.html_content = read_html_file(cls.html_file_path)

    def test_read_html_file(self):
        self.assertIsInstance(self.html_content, str)

    def test_import_is_valid_HTML(self):
        self.assertTrue(BeautifulSoup(self.html_content, "html.parser"))


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
