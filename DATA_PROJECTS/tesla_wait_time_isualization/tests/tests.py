import unittest

from tesla_price_visualizer import extract_json_from_html


class ExtractJSONFromHTML(unittest.TestCase):
    def test_extract_JSON_from_HTML(self):
        html_content = """
            <hmtl>
                <body>
                    <script type="text/javascript">
                        window.tesla = {"App": "Something"};
                    </script>
                </body>
            </html>
        """

        json_data = extract_json_from_html(html_content)

        expected_json = {"App": "Something"}
        self.assertEqual(json_data, expected_json)
        # Add type check if json_data is valid json/dict!
