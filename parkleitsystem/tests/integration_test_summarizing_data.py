import subprocess
import unittest
import json
from datetime import datetime
import os
import tempfile
import generate_parkleitsystem_data

class FunctionalSummarzeParkhouseData(unittest.TestCase):
    def setUp(self):
        self.data_directory = "data/"
        today = datetime.now().strftime("%d%m%Y")
        self.aggregated_parkhouse_data_file = f"aggregated_parkhouse_data_{today}.json"

        self.fake_json_path = "fake_json.json"
        self.fake_directory = "fake_directory"
        self.fake_json = [
            { "timestamp": "01112023", "parkhouses": [{ "name": "Dern-Passage", "free_spaces": 69, "occupied_spaces": 31, "max_spaces": 100 }]}
        ]
        self.fake_files_list = ["fake_file_1.json", "fake_file_2.json", "fake_file_3.json", "fake_file_4.json"]

        fake_directory = self.fake_directory
        if not os.path.exists(fake_directory):
            os.mkdir(self.fake_directory)


        def create_file(file_path, file_data):
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(file_data, f, ensure_ascii=False, indent=4)


        fake_files_list = self.fake_files_list
        for fake_file_path in fake_files_list:
            fake_json_path = os.path.join(fake_directory, fake_file_path)
            create_file(fake_json_path, self.fake_json)

        # Create single fake_json_file
        create_file(self.fake_json_path, self.fake_json)


    def tearDown(self):
        if os.path.exists(self.aggregated_parkhouse_data_file):
            os.remove(self.aggregated_parkhouse_data_file)

        def remove_file(file_path):
            if os.path.exists(file_path) and os.path.isfile(file_path):
                os.remove(file_path)
            else:
                print(f"Error deleting {file_path}")


        def remove_directory(directory_path):
            if os.path.exists(fake_directory):
                os.rmdir(fake_directory)
            else:
                print(f"Error deleting Direcotry {fake_directory}")

        fake_directory = self.fake_directory
        fake_files = self.fake_files_list
        for fake_file in fake_files:
            file_to_remove = os.path.join(fake_directory, fake_file)
            remove_file(file_to_remove)

        remove_file(self.fake_json_path)
        remove_directory(fake_directory)


    def test_aggregate_parkhouse_data_to_json_file(self):
        aggregated_data_file = self.aggregated_parkhouse_data_file
        data_directory = self.data_directory

        generate_parkleitsystem_data.aggregate_parkhouse_data(data_directory)

        with open(aggregated_data_file, 'r') as file:
            aggregated_data = json.load(file)

        # aggregated_data is a list with dicts
        self.assertIsInstance(aggregated_data, list)
        self.assertIsInstance(aggregated_data[0], dict)
        # Each dict has timestamp as string
        # and parkhouses as list
        self.assertIn("timestamp", aggregated_data[-1])
        self.assertIn("parkhouses", aggregated_data[-1])
        self.assertIsInstance(aggregated_data[-1]["timestamp"], str)
        self.assertIsInstance(aggregated_data[-1]["parkhouses"], list)

        # Aggregated Data has same length as files in data_directory
        files = os.listdir(self.data_directory)
        self.assertEqual(len(aggregated_data), len(files))

        file_exists = os.path.exists(aggregated_data_file)
        self.assertTrue(file_exists)


    def test_get_data_for_single_parkhouse(self):
        parkhouse_name = "Dern-Passage"
        today = datetime.now().strftime("%d%m%Y")
        expected_output_file = f"dern-passage_data_{today}.json"
        parkhouse_data = [
            { "timestamp": "01112023-0950", "parkhouses": [{ "name": "Dern-Passage", "free_spaces": 69, "occupied_spaces": 31, "max_spaces": 100 },
                                                      { "name": "Karstadt", "free_spaces": 100, "occupied_spaces": 20, "max_spaces": 120 }]},
            { "timestamp": "01112023-0955", "parkhouses": [{ "name": "Dern-Passage", "free_spaces": 70, "occupied_spaces": 30, "max_spaces": 100 },
                                                      { "name": "Karstadt", "free_spaces": 99, "occupied_spaces": 21, "max_spaces": 120 }]}
            ]

        _, parkhouse_data_file = tempfile.mkstemp(suffix=".json")
        with open(parkhouse_data_file, "w") as f:
            json.dump(parkhouse_data, f)


        # Isabel calls the funtion
        generate_parkleitsystem_data.get_single_parkhouse_data(parkhouse_name, parkhouse_data_file)

        # And expects the parkhouse file to exist
        parkhouse_file_exists = os.path.exists(expected_output_file)
        self.assertTrue(parkhouse_file_exists)

        # She notices the data format in the file
        # it is a valid json
        with open(expected_output_file) as file:
            json_data = json.load(file)
        self.assertTrue(json_data)

        # The json data is a list
        self.assertIsInstance(json_data, list)
        self.assertIsInstance(json_data[0], dict)
        self.assertIn("timestamp", json_data[0])
        self.assertIn("name", json_data[0])
        self.assertIn("max_spaces", json_data[0])
        self.assertIn("free_spaces", json_data[0])
        self.assertIn("occupied_spaces", json_data[0])


        # !! Remove test file!
        def remove_file(file_path):
            if os.path.exists(file_path) and os.path.isfile(file_path):
                os.remove(file_path)
            else:
                print(f"Error deleting {file_path}")

        remove_file(parkhouse_data_file)
        remove_file(expected_output_file)



    def test_transform_single_parkhouse_data_to_csv(self):

        single_parkhouse_data = [
            {
                "timestamp": "01112023-0950",
                "name": "Dern-Passage",
                "free_spaces": 20,
                "max_spaces": 100,
                "occupied_spaces": 80,
            },
            {
                "timestamp": "01112023-0955",
                "name": "Dern-Passage",
                "free_spaces": 30,
                "max_spaces": 100,
                "occupied_spaces": 70,
            }
        ]

        _, parkhouse_file = tempfile.mkstemp(suffix=".json")
        with open(parkhouse_file, "w") as f:
            json.dump(single_parkhouse_data, f)

        generate_parkleitsystem_data.export_single_parkhouse_data_to_csv(parkhouse_file)

        csv_file_path = "dern-passage_01112023.csv"
        self.assertTrue(os.path.exists(csv_file_path))

        # Read the contents of the created file
        with open(csv_file_path, 'r') as file:
            file_content = file.read()

        self.assertIn("max_spaces", file_content)
        self.assertIn("01112023-0955", file_content)



        # Remove file csv_file
        if os.path.exists(csv_file_path) and os.path.isfile(csv_file_path):
            os.remove(csv_file_path)
        else:
            print(f"Error deleting {csv_file_path}")


class SummarizeDataViaCLI(unittest.TestCase):
    def setUp(self):
        expected_date = datetime.now()
        self.parkhouse_data_file = f"aggregated_parkhouse_data_{expected_date.strftime('%d%m%Y')}.json"

        self.fake_json = [
            { "timestamp": "01112023-0935", "parkhouses": [{ "name": "Dern-Passage", "free_spaces": 69, "occupied_spaces": 31, "max_spaces": 100 }, { "name": "Johannesstraße", "free_spaces": 69, "occupied_spaces": 31, "max_spaces": 100 }]},
            { "timestamp": "01112023-0940", "parkhouses": [{ "name": "Dern-Passage", "free_spaces": 69, "occupied_spaces": 31, "max_spaces": 100 }, { "name": "Johannesstraße", "free_spaces": 69, "occupied_spaces": 31, "max_spaces": 100 }]}
        ]

        self.parkhouse_name = "Dern-Passage"

        self.today = datetime.now().strftime("%d%m%Y")
        self.single_parkhouse_data_file = f"dern-passage_data_{self.today}.json"


    def tearDown(self):
        def remove_file(file_name):
            if os.path.exists(file_name):
                os.remove(file_name)

        remove_file(self.parkhouse_data_file)
        remove_file(self.single_parkhouse_data_file)


    def test_aggregate_json_data_command(self):
        parkhouse_data_file = self.parkhouse_data_file
        # Call the module with the command-line flag using subprocess
        command = ["python3", "generate_parkleitsystem_data.py", "--aggregate-json-data", "data/"]
        subprocess.run(command, check=True)

        # Check if the JSON file is created in the main directory with the expected name
        self.assertTrue(os.path.isfile(parkhouse_data_file))


    def test_extract_single_parkhouse_info(self):
        parkhouse_data_file = self.parkhouse_data_file
        fake_json = self.fake_json

        with open(parkhouse_data_file, 'w', encoding='utf-8') as f:
            json.dump(fake_json, f, ensure_ascii=False, indent=4)

        parkhouse_name = self.parkhouse_name
        single_parkhouse_data_file = self.single_parkhouse_data_file

        command = ["python3", "generate_parkleitsystem_data.py", "--extract-single-parkhouse", parkhouse_name, parkhouse_data_file]
        subprocess.run(command, check=True)

        self.assertTrue(os.path.isfile(single_parkhouse_data_file))



