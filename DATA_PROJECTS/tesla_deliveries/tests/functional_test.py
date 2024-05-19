import unittest
import subprocess
from tesla_deliveries import extract_totals, get_numbers_from_press_release, get_press_release_links

class TestTeslaDeliveryIntegration(unittest.TestCase):
    def test_extract_totals_from_html(self):
        with open('tests/data/press_release.html', 'r') as f:
            html = f.read()

        totals = extract_totals(html)

        self.assertIsInstance(totals, dict)

        self.assertIn("production", totals)
        self.assertIn("deliveries", totals)

        self.assertIsInstance(totals["production"], int)
        self.assertIsInstance(totals["deliveries"], int)

        self.assertEqual(totals["production"], 305407)
        self.assertEqual(totals["deliveries"], 310048)

    def test_extract_totals_from_URL(self):
        """
        As a user I want to provide the URL to the Tesla Press release and get the totals in return
        """
        url = "https://ir.tesla.com/press-release/tesla-vehicle-production-deliveries-and-date-financial-results-webcast-first-quarter"

        process = subprocess.Popen(["python3", "tesla_deliveries.py", url], stdout=subprocess.PIPE)
        output, _ = process.communicate()
        output = output.decode("utf-8").strip()

        expected_output = """2022-04-02T12:00:00Z
        Production: 305407
        Deliveries: 310048"""
        self.assertEqual(output, expected_output)

    def test_get_press_release_links_from_ir_webpage(self):
        url = "https://ir.tesla.com/#quarterly-disclosure"

        press_release_links = get_press_release_links(url)
        self.assertIsInstance(press_release_links, list)
        self.assertIsInstance(press_release_links[0], str)


    def test_get_dataset_from_reports(self):
        press_release_urls = [
            "https://ir.tesla.com/press-release/tesla-q4-2021-vehicle-production-deliveries",
            "https://ir.tesla.com/press-release/tesla-vehicle-production-deliveries-and-date-financial-results-webcast-first-quarter",
            "https://ir.tesla.com/press-release/tesla-vehicle-production-deliveries-and-date-financial-results-webcast-second-quarter",
            "https://ir.tesla.com/press-release/tesla-vehicle-production-deliveries-and-date-financial-results-webcast-third-quarter"
        ]



if __name__ == '__main__':
    unittest.main()
