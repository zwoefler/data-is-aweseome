import unittest

from tesla_price_visualizer import extract_json_from_html


class ExtractJSONFromHTML(unittest.TestCase):
    def setUp(self):
        self.html_content = """
            <hmtl>
                <body>
                    <script type="text/javascript">
                        window.tesla = {"App": "Something"};
                    </script>
                </body>
            </html>
        """
        self.expected_json = {"App": "Something"}

    def test_extract_JSON_from_HTML(self):
        json_data = extract_json_from_html(self.html_content)
        self.assertEqual(json_data, self.expected_json)

    def test_returns_valid_JSON(self):
        json_data = extract_json_from_html(self.html_content)
        self.assertIsInstance(json_data, (dict, list))


class TestReadHTMLFile(unittest.TestCase):
    def test_read_html_file(self):
        html_file_path = (
            "tests/test_data/test_html_raw_de_DE_model3_20190327102025.html"
        )

        expected_html_output = """
        <html>
            <head>
                <title>Test HTML File</title>
            </head>
            <body>
                <h1>This is a test HTML file.</h1>
            </body>
        </html>
        """

        html_content = read_html_file(html_file_path)
        self.assertEqual(html_content.strip(), expected_html_output.strip())
