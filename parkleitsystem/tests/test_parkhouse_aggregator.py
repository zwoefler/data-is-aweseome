import unittest
import os
import tempfile

from parkhouse_aggregator.parkhouse_aggregator import (
    create_parkhouse_data_folder,
    list_files_in_directory,
    convert_timestamp_to_epoch_seconds,
)


class FileSystemTests(unittest.TestCase):
    def setUp(self):
        self.temp_folder = self.create_temp_folder_with_json_files()

    def tearDown(self):
        for file in os.listdir(self.temp_folder):
            file_path = os.path.join(self.temp_folder, file)
            os.remove(file_path)
        os.rmdir(self.temp_folder)

    def create_temp_folder_with_json_files(self):
        temp_dir = tempfile.mkdtemp()

        json_file_contents = [
            '{"name": "file1.json", "content": "data1"}',
            '{"name": "file2.json", "content": "data2"}',
            '{"name": "file3.json", "content": "data3"}',
        ]

        for i, content in enumerate(json_file_contents, 1):
            file_path = os.path.join(temp_dir, f"file{i}.json")
            with open(file_path, "w") as f:
                f.write(content)

        return temp_dir

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
        data_dir = self.temp_folder
        file_list = list_files_in_directory(data_dir)

        self.assertIsInstance(file_list, list)
        self.assertEqual(len(file_list), 3)


class TestHelperFunctions(unittest.TestCase):
    def test_convert_timestamp_from_custom_to_epoch_seconds(self):
        epoch_timestamp = convert_timestamp_to_epoch_seconds("09112023-0900")

        self.assertEqual(epoch_timestamp, 1699520400)


if __name__ == "__main__":
    unittest.main()
