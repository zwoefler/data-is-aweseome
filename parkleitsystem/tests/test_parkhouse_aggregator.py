import unittest
import os
import tempfile

from parkhouse_aggregator.parkhouse_aggregator import (
    create_parkhouse_data_folder,
    list_files_in_directory,
    convert_timestamp_to_epoch_seconds,
)


class FileSystemTests(unittest.TestCase):
    def test_create_parkhouse_data_folder(self):
        parent_directory = os.path.dirname(os.path.dirname(__file__))
        parkhouse_data_dir = "parkhouse_data"
        create_parkhouse_data_folder()

        self.assertTrue(
            os.path.exists(os.path.join(parent_directory, parkhouse_data_dir))
        )
        self.assertTrue(
            os.path.isdir(os.path.join(parent_directory, parkhouse_data_dir))
        )

        os.rmdir(parkhouse_data_dir)

    def test_get_file_list_from_data_folder(self):
        data_dir = "data/"
        file_list = list_files_in_directory(data_dir)

        self.assertIsInstance(file_list, list)


class TestHelperFunctions(unittest.TestCase):
    def test_convert_timestamp_from_custom_to_epoch_seconds(self):
        epoch_timestamp = convert_timestamp_to_epoch_seconds("09112023-0900")

        self.assertEqual(epoch_timestamp, 1699520400)


if __name__ == "__main__":
    unittest.main()
