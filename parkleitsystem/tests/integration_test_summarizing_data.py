import unittest
import json
from datetime import datetime
import os
import generate_parkleitsystem_data

class FunctionalSummarzeParkhouseData(unittest.TestCase):
    def setUp(self):
        self.data_directory = "data/"
        self.aggregated_parkhouse_data_file = "parkhouse_data_05112023.json"


    def tearDown(self):
        if os.path.exists(self.aggregated_parkhouse_data_file):
            os.remove(self.aggregated_parkhouse_data_file)


    def test_aggregate_parkhouse_data(self):
        # Bob pulls the project for the first time and needs to aggreaget
        aggregated_data = generate_parkleitsystem_data.aggregate_data(self.data_directory)

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
