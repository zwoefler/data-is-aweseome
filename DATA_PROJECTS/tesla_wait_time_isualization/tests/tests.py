import unittest

from tesla_price_visualizer import extract_json_from_html


class ExtractJSONFromHTML(unittest.TestCase):
    def test_extract_JSON_from_HTML(self):
        html_content = """
            <hmtl>
                <body>
                    <div id="json_data">
                        {"example_key": "example_value"}
                    </div>
                </body>
            </html>
        """

        json_data = extract_json_from_html(html_content)

        expected_json = {"example_key": "example_value"}
        self.assertEqual(json_data, expected_json)
