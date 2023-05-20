import unittest
import pull_energy_charts_data as pe
from unittest.mock import patch
from requests import Response
import errors

class TestHelperFunctions(unittest.TestCase):
    def setUp(self):
        self.query_string = "year_2022.json"
        self.folder = "energy_data"


    def test_create_correct_filename(self):
        """
        Creates correct filename to export energy jsons to!
        """
        filename = pe.create_filename(self.folder, self.query_string)

        self.assertEqual(filename, "energy_data/year_2022.json")


    def test_create_year_query_search_string(self):
        date_query_string = 2022
        intervall_query_string = "year"

        query_string = pe.create_query_string(intervall_query_string, date_query_string)

        self.assertEqual(query_string, self.query_string)


    def test_create_data_url(self):
        """
        Creates the correct url to pull the energy data from
        """
        base_url = f"https://www.energy-charts.info/charts/power/data/de/"
        url = pe.create_url(self.query_string, base_url)

        self.assertEqual(url, "https://www.energy-charts.info/charts/power/data/de/year_2022.json")


class TestFetchingEnergyData(unittest.TestCase):
    def setup(self):
        pass

    @patch(pe.requests.get)
    def test_return_None_for_not_downloadable_data(self, mock_get):
        # Mock the requests.get() function to return a response with status code 404
        mock_get.return_value = Response()
        mock_get.return_value.status_code = 404
        url = "https://example.com/energy_data"

        with self.assertRaises(errors.DataNotAvailableException):
            pe.download_energy_data(url)

if __name__ == '__main__':
    unittest.main()
