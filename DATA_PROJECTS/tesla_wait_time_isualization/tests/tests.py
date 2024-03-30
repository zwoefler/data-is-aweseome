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

    def test_extract_JSON_from_HTML(self):
        json_data = extract_json_from_html(self.html_content)

        expected_json = {"App": "Something"}
        self.assertEqual(json_data, expected_json)

    def test_returns_valid_JSON(self):
        html_content = """
            <hmtl>
                <body>
                    <script type="text/javascript">
                        window.tesla = {"App": "Something"};
                    </script>
                </body>
            </html>
        """

        json_data = extract_json_from_html(self.html_content)

        expected_json = {"App": "Something"}
        self.assertIsInstance(json_data, (dict, list))
