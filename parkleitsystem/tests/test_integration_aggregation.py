import unittest
import os

from pandas import read_json

from parkhouse_aggregator.parkhouse_aggregator import *


class TestFunctionalAggregateParkhouseData(unittest.TestCase):
    def test_aggregate_parkhouse_data_from_data_dir_into_separate_files(self):
        # As a User I want to call the parkhouse_aggregator.aggregate(data_dir) function
        # The function checks the JSON files in the data_dir (for test like first 20)
        # Rearranges the data and sorts them per parkhouse into files:
        # parkhouse_data/<parkhouse>.json
        data_dir = "data/"
        file_list = list_files_in_directory(data_dir)
        for json_file in file_list:
            # Iterate files in folder
            # Load each file
            # read it's content
            json_data = read_json_file(json_file)
        # get names of parkhouses
        # if scheme for parkhouse doesn#t exist, create one
        # put data into scheme
        # Get next file, read, add to parkhouse scheme
        # once finished with files from folder, write schemes to
        # parkhouse_data/<PARKHOUSE.JSON>

        parkhouse_data_dir = "parkhouse_data"
        self.assertTrue(os.path.exists(parkhouse_data_dir))
        self.assertTrue(expr=os.path.exists("parkhouse_data/Dern-Passage.json"))
        pass


if __name__ == "__main__":
    unittest.main()
