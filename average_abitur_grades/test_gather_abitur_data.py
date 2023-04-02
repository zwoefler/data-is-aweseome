import unittest
from unittest.mock import patch, mock_open
from gather_abitur_data import download_kmk_webpage, get_zip_links, load_json_data, main, is_zip_link
from bs4 import BeautifulSoup
import os
import json
import datetime

# Arrange, Act, Assert == Given, When, Then
# Arrange (Mock, Fake, etc.)
# Act: Run the method
# Assert: Does the output fir the expectation?

correct_url = "https://www.kmk.org/dokumentation-statistik/statistik/schulstatistik/abiturnoten.html"
archive_url = "https://www.kmk.org/dokumentation-statistik/statistik/schulstatistik/abiturnoten/archiv-abiturnoten.html"
urls = [correct_url, archive_url]

zip_link_file = "zip_links.json"


def load_json_data(link_json_file):
    with open(link_json_file, "r") as f:
        return json.load(f)

def last_year():
    return datetime.datetime.now().year - 1

class TestDownloadKMKWebpage(unittest.TestCase):
    def test_download_kmk_webpage(self):
        """Download KMK webpage"""
        webpage = download_kmk_webpage(correct_url)

        self.assertIsNotNone(webpage)
        self.assertGreater(len(webpage), 0)


    def test_returns_not_valid_URL_for_not_containing_KMK_in_link(self):
        wrong_url = "https://www.ktk.de/dokumentation-statistik/statistik/schulstatistik/abiturnoten.html"
        with self.assertRaises(Exception) as context:
            download_kmk_webpage(wrong_url)
        self.assertTrue("domain kmk.org" in str(context.exception))


    def test_return_list_for_zip_files_for_url_list(self):
        """
        GIVEN: A list of urls (archive and current)
        WHEN: Executing the main() function
        THEN: Returns a list with at least 5 downloadlinks that lead to download a zipfile"""
        zip_links = get_zip_links(correct_url)

        # List not empty and list
        self.assertTrue(zip_links)
        self.assertIsInstance(zip_links, list)

        for download_link in zip_links:
            self.assertIsInstance(download_link, str)
            self.assertTrue(download_link.endswith('.zip'))
            self.assertTrue(is_zip_link(download_link))


    @patch('builtins.open', mock_open(read_data='["xxx.zip", "yyy.zip"]'))
    def test_when_json_link_file_exist_load_json_file_instead_of_download(self):
        if(os.path.isfile(zip_link_file)):
            data = main()
            self.assertEqual(data, ["xxx.zip", "yyy.zip"])


    def test_when_json_link_file_doesnt_exist(self):
        if(not os.path.isfile(zip_link_file)):
            main()
            self.assertTrue(os.path.isfile(zip_link_file))

if __name__ == '__main__':
    unittest.main()
