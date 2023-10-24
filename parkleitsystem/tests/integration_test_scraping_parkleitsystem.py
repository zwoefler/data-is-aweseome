import unittest
import scraping_parkleitsystem
import io
import sys
from bs4 import BeautifulSoup
import subprocess
import json


class FunctionalExtractParkhouseInformation(unittest.TestCase):
    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_extract_parkhouse_information_from_url(self):
        """
        GIVEN: A valid URL
        WHEN: The user sends the request
        THEN: Return an Object with the representation of the parkhouse occupation
        """

        # capturedOutput = io.StringIO()                  # Create StringIO object
        # sys.stdout = capturedOutput                     #  and redirect stdout.

        # Annika wants to capture the parkhouse listings from the webpage gießen parkhouse
        # She enters the URL into the program
        parkhouse_webpage_url = "https://www.giessen.de/Umwelt_und_Verkehr/Parken/"

        # Download HTML from URL
        html = scraping_parkleitsystem.download_parkhouse_html(parkhouse_webpage_url)

        soup = BeautifulSoup(html, "html.parser")
        is_valid_html = bool(soup.find())
        self.assertTrue(is_valid_html)
        self.assertIn("Parken in Gießen", soup.title.text)

        parkhouse_info = scraping_parkleitsystem.scrape_webpage(html)

        self.assertRegex(parkhouse_info["timestamp"], r'\d{2}:\d{2} Uhr - \d{2}.\d{2}.\d{4}')
        self.assertIsInstance(parkhouse_info, dict)
        self.assertIsInstance(parkhouse_info["parkhouses"], list)
        self.assertIsInstance(parkhouse_info["parkhouses"][0], dict)


    def test_execute_parkleitsystem(self):
        url = "https://www.giessen.de/Umwelt_und_Verkehr/Parken/"

        # Run your script as a subprocess and capture its output
        result = subprocess.check_output(['python3', 'scraping_parkleitsystem.py'], text=True)

        # Try to parse the output as JSON
        result_dict = json.loads(result)

        # Check if the parsed result is a dictionary with the expected keys
        self.assertIsInstance(result_dict, dict)
        self.assertIsInstance(result_dict["parkhouses"], list)
        self.assertIn('timestamp', result_dict)
        self.assertIn('parkhouses', result_dict)