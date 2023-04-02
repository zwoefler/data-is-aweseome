import unittest
from unittest.mock import patch, mock_open
from gather_abitur_data import download_kmk_webpage, get_zip_links, load_json_data, main
from bs4 import BeautifulSoup
import os
import json


correct_url = "https://www.kmk.org/dokumentation-statistik/statistik/schulstatistik/abiturnoten.html"
archive_url = "https://www.kmk.org/dokumentation-statistik/statistik/schulstatistik/abiturnoten/archiv-abiturnoten.html"

zip_link_file = "zip_links.json"

class TestDownloadKMKWebpage(unittest.TestCase):
    def test_download_kmk_webpage(self):
        """Download KMK webpage"""
        url = "https://www.kmk.org/dokumentation-statistik/statistik/schulstatistik/abiturnoten/archiv-abiturnoten.html"
        webpage = download_kmk_webpage(url)

        self.assertIsNotNone(webpage)
        self.assertGreater(len(webpage), 0)


    def test_returns_not_valid_URL_for_not_containing_KMK_in_link(self):
        url = "https://www.statista/dokumentation-statistik/statistik/schulstatistik/abiturnoten/archiv-abiturnoten.html"
        with self.assertRaises(Exception) as context:
            download_kmk_webpage(url)
        self.assertTrue("domain kmk.org" in str(context.exception))


    def test_return_list_for_zip_files_aus_abiturnoten(self):
        """Test returns a list of strings with at least 5 entries that end with .zip"""
        webpage = download_kmk_webpage(correct_url)
        zip_links = get_zip_links(webpage)

        # List not empty and list
        self.assertTrue(zip_links)
        self.assertIsInstance(zip_links, list)

        for download_link in zip_links:
            self.assertIsInstance(download_link, str)
            self.assertTrue(download_link.endswith('.zip'))


    @patch('builtins.open', mock_open(read_data='["xxx.zip", "yyy.zip"]'))
    def test_when_json_link_file_exist(self):
        if(os.path.isfile(zip_link_file)):
            main()
            self.assertEqual('Data read from file: ["xxx.zip", "yyy.zip"]',
                            f'Data read from file: {main()}')


    def test_download_data_when_zip_file_doesnt_exist(self):
        if(not os.path.isfile(zip_link_file)):
            main()
            self.assertTrue(os.path.isfile(zip_link_file))







if __name__ == '__main__':
    unittest.main()
