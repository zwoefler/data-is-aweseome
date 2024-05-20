import unittest
import subprocess
from tesla_deliveries import (
    extract_totals,
)


class TestTeslaDeliveryIntegration(unittest.TestCase):

    def test_extract_totals_from_URL(self):
        """
        As a user I want to provide the URL to the Tesla Press release and get the totals in return
        """
        url = "https://ir.tesla.com/press-release/tesla-vehicle-production-deliveries-and-date-financial-results-webcast-first-quarter"

        output = subprocess.check_output(
            ["python3", "tesla_deliveries.py", url]
        ).decode("utf-8")

        self.assertIn("Date: 2022-04-02T12:00:00Z", output)
        self.assertIn("Production: 305407", output)
        self.assertIn("Deliveries: 310048", output)

    def test_get_press_release_links_from_ir_webpage(self):
        # url = "https://ir.tesla.com/#quarterly-disclosure"

        # press_release_links = get_press_release_links(url)
        # self.assertIsInstance(press_release_links, list)
        # self.assertIsInstance(press_release_links[0], str)
        pass

    def test_get_dataset_from_reports(self):
        press_release_urls = [
            "https://ir.tesla.com/press-release/tesla-q4-2021-vehicle-production-deliveries",
            "https://ir.tesla.com/press-release/tesla-vehicle-production-deliveries-and-date-financial-results-webcast-first-quarter",
            "https://ir.tesla.com/press-release/tesla-vehicle-production-deliveries-and-date-financial-results-webcast-second-quarter",
            "https://ir.tesla.com/press-release/tesla-vehicle-production-deliveries-and-date-financial-results-webcast-third-quarter",
        ]


if __name__ == "__main__":
    unittest.main()
