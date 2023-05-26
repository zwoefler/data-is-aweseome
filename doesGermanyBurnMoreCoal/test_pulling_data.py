import unittest
import pull_energy_charts_data as pe
import create_download_links as cl
from unittest.mock import patch
from requests import Response
import os
import shutil
import errors

class TestHelperFunctions(unittest.TestCase):
    def setUp(self):
        self.query_string = "year_2022.json"
        self.folder = "energy_data"


    def test_create_correct_filename(self):
        """
        Creates correct filename to export energy jsons to!
        """
        filename = cl.create_filename(self.folder, self.query_string)

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
        url = cl.create_url(self.query_string, base_url)

        self.assertEqual(url, "https://www.energy-charts.info/charts/power/data/de/year_2022.json")

class TestFetchingEnergyData(unittest.TestCase):
    def setup(self):
        pass


    # def test_if_service_not_reachable_throw_application_no_reachable(self):
    #     error_message = """Service not reachable.
    #     Could be because ther service is
    #     - offline
    #     - no data under that URL available"""


    #     with self.assertRaises as context:
    #         energy_data = pe.pull_data_from_url(url)

    #     self.assertEqual(str(context.exception), error_message)




    def test_create_correct_export_file_name_from_url(self):
        url = "https://www.energy-charts.info/charts/power/data/de/year_1990.json"

        export_filename = pe.create_export_filename(url)

        self.assertEqual(export_filename, "data_year_1990.json")


class TestWriteDataToJSONFile(unittest.TestCase):
    def setUp(self):
        self.folder = "test_data"
        if os.path.exists(self.folder):
            shutil.rmtree(self.folder)


    def test_when_folder_does_not_exist_throws_FileNotFoundError(self):
        with self.assertRaises(FileNotFoundError):
            pe.write_json_data_to_file(folder="data", filename="test_data.json", json_data={})


    def test_when_folder_does_not_exist_asks_user_to_create_folder(self):
        expected_error_message = "data/ - Folder does not exist."

        with self.assertRaises(FileNotFoundError) as context:
            pe.write_json_data_to_file(folder="data", filename="test_data.json", json_data={})

        self.assertEqual(str(context.exception), expected_error_message)


    def test_put_downloaded_files_into_data_folder(self):
        # Setup
        os.mkdir(self.folder)

        filename = "test_data_2023.json"
        data = ["Something here", "Some more thing"]


        pe.write_json_data_to_file(self.folder, filename, data)

        self.assertTrue(os.path.exists("test_data/test_data_2023.json"))

        #TearDown
        os.remove("test_data/test_data_2023.json")
        os.rmdir("test_data/")



if __name__ == '__main__':
    unittest.main()
