import unittest
from tesla_deliveries import extract_totals, get_numbers_from_press_release

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

        totals = get_numbers_from_press_release(url)

        self.assertIsInstance(totals, dict)

        self.assertIn("production", totals)
        self.assertIn("deliveries", totals)
        self.assertIsInstance(totals["production"], int)
        self.assertIsInstance(totals["deliveries"], int)
        self.assertEqual(totals["production"], 305407)
        self.assertEqual(totals["deliveries"], 310048)

if __name__ == '__main__':
    unittest.main()
