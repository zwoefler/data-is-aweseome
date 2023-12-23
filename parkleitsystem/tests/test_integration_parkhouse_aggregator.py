import unittest
import os


class TestAggregateFunctionality(unittest.TestCase):
    def test_aggregate_data_function(self):
        # Call aggregate_data functionality with data/ folder
        data_dir = "data/"
        aggregate_data(data_dir)
        # Go through each JSON file in the folder (for testing like 20)
        # Extract the data in the format: { name: str<PARKHOUSE>, occupation-data: [sorted by timestamp<{ timestamp: EPOCH_seconds, occupied_spaces: int, free_spaces: int, max_spaces: int}>]}
        # assert for every parkhouse in the data there is a JSON file in the parkhouse_data folder with PARKHOUSE_NAME.JSON
        parkhouse_data_dir = "parkhouse_data"
        self.assertTrue(os.path.exists(parkhouse_data_dir))

        pass


if __name__ == "__main__":
    unittest.main()
