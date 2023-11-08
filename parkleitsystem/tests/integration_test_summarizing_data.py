import unittest
import json
from datetime import datetime
import os
import generate_parkleitsystem_data

class FunctionalSummarzeParkhouseData(unittest.TestCase):
    def setUp(self):
        self.data_directory = "data/"
        self.aggregated_parkhouse_data_file = "parkhouse_data_05112023.json"

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


    def test_aggregate_parkhouse_data(self):
        # Isabel pulls the project for the first time and needs to aggregate the data

        # They notice the data dir which holds ALL the parkhouse data entries
        # To aggregate the data they execute the aggregate_data function
        # It returns a file 'parkhouse_data_<CURRENT_DATE>.json'
        # And contains a list with dictionaries
            # Each dict contains the keys: timestamp <str> "01112023_9000"
            # and parkhouses <list of Objects>
        existing_data = []
        aggreagted_data_file = self.aggregated_parkhouse_data_file

        data_files_list = generate_parkleitsystem_data.list_files_in_directory(self.data_directory)
        aggregated_data = generate_parkleitsystem_data.aggregate_data(data_files_list, existing_data)
        generate_parkleitsystem_data.write_json_to_file(aggreagted_data_file, aggregated_data)

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

        # the data into the parkhouse_data_ddmmyyyy.json file to run analysis
        # JSON file with containing list with name parkhouse_data_ddmmyyyy.json exists
        # list contains so many entries in how files exists in the data/ directory
        file_path = 'parkhouse_data_05112023.json'
        file_exists = os.path.exists(file_path)
        self.assertTrue(file_exists)


    def test_get_data_for_parkhouse(self):
        # Isabel wants to get the data for a single parkhouse
        # She provides the script with the path to the aggregated file
        # And gets a file <parkhouse_name_ddmmyyyy.json> with all the data just
        # for one parkhouse

        parkhouse_name = "Dern-Passage"
        parkhouse_data_file = "parkhouse_data_05112023.json"
        expected_output_file = "dern-passage_data_05112023.json"

        # Isabel calls the funtion
        generate_parkleitsystem_data.get_single_parkhouse_data(parkhouse_name, parkhouse_data_file)

        # And expects the parkhouse file to exist
        parkhouse_file_exists = os.path.exists(expected_output_file)
        self.assertTrue(parkhouse_file_exists)

        # She notices the data format in the file
        # it is a valid json
        with open(expected_output_file) as file:
            json_data = json_datajson.load(file)
        self.assertTrue(json_data)

        # The json data is a list
        self.assertIsInstance(json_data, list)
        self.assertIsInstance(json_data[0], dict)
        self.assertIn("timestamp", json_data[0])
        self.assertIn("parkhouses", json_data[0])
        self.assertIsInstance(json_data[0]["parkhouses"], list)

        # !! Remove test file!
        self.remove_file(expected_output_file)






        # He also want each parkhouses data to visualize easily
        # with a CSV file

        # Bob provides the module with the data/ directory
        # The module writes the aggregated data and each individual
        # parkhouse into files


        # He provides the folder as input into a function
        # list of files
        # open each file, write contents to list
        # write list to JSON file
        # The function aggregates all the data into one giant list
        # and writes it to "data/aggregated_data.json"


        # Bob runs a script that returns a big JSON files with all the parkhouse data in it!
        # The aggregated data has the format a list with ALL items in there

        # from that "parkhouse_data_<CURRENT_DATE>.json"
        # Bob extracts the data for each parkhouse as CSV files

        # Format:
        # parkhouse,timestamp,max_spaces,free_spaces,occupied_spaces
        # Dern-Passage,31102023-2035,100,70,30
        # Dern-Passage,31102023-2036,150,90,60
        # Dern-Passage,31102023-2037,200,120,80
        # Dern-Passage,31102023-2038,180,110,70
        # Dern-Passage,31102023-2039,160,80,80

        # For each parkhouse there are csv_files with their name in the
        # data/parkhouses/ directory


    def test_add_new_data_without_duplicates(self):
        pass


    def test_export_parkhouse_data_per_parkhouse(self):
        pass
