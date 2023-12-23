import unittest
import os
import tempfile

from parkhouse_aggregator.parkhouse_aggregator import create_parkhouse_data_folder


class FileSystemTests(unittest.TestCase):
    def test_create_parkhouse_data_folder(self):
        parent_directory = os.path.dirname(os.path.dirname(__file__))
        parkhouse_data_dir = "fake_parkhouse_dir"
        create_parkhouse_data_folder(parkhouse_data_dir)

        self.assertTrue(
            os.path.exists(os.path.join(parent_directory, parkhouse_data_dir))
        )
        self.assertTrue(
            os.path.isdir(os.path.join(parent_directory, parkhouse_data_dir))
        )

        os.rmdir(parkhouse_data_dir)


if __name__ == "__main__":
    unittest.main()
