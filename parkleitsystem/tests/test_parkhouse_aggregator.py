import unittest
import os
import tempfile
import json
from pathlib import Path


from parkhouse_aggregator.parkhouse_aggregator import (
    create_parkhouse_data_folder,
    list_files_in_directory,
    convert_timestamp_to_epoch_seconds,
    read_json_file,
    parkhouse_list_from_data,
    generate_parkhouse_data,
    export_parkhouse_data,
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
        self.assertIn(
            f"{data_dir}/file1.json",
            file_list,
        )

    def test_load_json_from_file(self):
        fake_json_data = [
            {
                "timestamp": "01112023",
                "parkhouses": [
                    {
                        "name": "Dern-Passage",
                        "free_spaces": 69,
                        "occupied_spaces": 31,
                        "max_spaces": 100,
                    }
                ],
            }
        ]
        with tempfile.NamedTemporaryFile(mode="w", delete=False) as json_file:
            json.dump(fake_json_data, json_file, ensure_ascii=False, indent=4)
            json_path = Path(json_file.name)

        json_data = read_json_file(json_path)

        self.assertEqual(json_data, fake_json_data)

        os.remove(json_path)


class ParkhouseDataFunctions(unittest.TestCase):
    def test_list_parkhouses_in_data(self):
        parkhouse_data = {
            "timestamp": "09112023-0905",
            "parkhouses": [
                {
                    "name": "Dern-Passage",
                    "free_spaces": 120,
                    "occupied_spaces": 79,
                    "max_spaces": 199,
                },
                {
                    "name": "Karstadt",
                    "free_spaces": 609,
                    "occupied_spaces": 86,
                    "max_spaces": 695,
                },
                {
                    "name": "Liebig-Center",
                    "free_spaces": 242,
                    "occupied_spaces": 8,
                    "max_spaces": 250,
                },
            ],
        }
        parkhouses = parkhouse_list_from_data(parkhouse_data)

        self.assertIsInstance(parkhouses, list)
        self.assertIn("Liebig-Center", parkhouses)
        self.assertIn("Karstadt", parkhouses)
        self.assertIn("Dern-Passage", parkhouses)

    def test_make_correct_data_schema(self):
        self.maxDiff = None
        raw_data_list = [
            {
                "timestamp": "09112023-0905",
                "parkhouses": [
                    {
                        "name": "Dern-Passage",
                        "free_spaces": 120,
                        "occupied_spaces": 79,
                        "max_spaces": 199,
                    },
                    {
                        "name": "Karstadt",
                        "free_spaces": 609,
                        "occupied_spaces": 86,
                        "max_spaces": 695,
                    },
                ],
            },
            {
                "timestamp": "09112023-0910",
                "parkhouses": [
                    {
                        "name": "Dern-Passage",
                        "free_spaces": 100,
                        "occupied_spaces": 99,
                        "max_spaces": 199,
                    },
                    {
                        "name": "Karstadt",
                        "free_spaces": 600,
                        "occupied_spaces": 95,
                        "max_spaces": 695,
                    },
                ],
            },
        ]

        expected_parkhouse_data = {
            "Dern-Passage": {
                "name": "Dern-Passage",
                "occupation_data": [
                    {
                        "timestamp": "09112023-0905",
                        "free_spaces": 120,
                        "occupied_spaces": 79,
                        "max_spaces": 199,
                    },
                    {
                        "timestamp": "09112023-0910",
                        "free_spaces": 100,
                        "occupied_spaces": 99,
                        "max_spaces": 199,
                    },
                ],
            },
            "Karstadt": {
                "name": "Karstadt",
                "occupation_data": [
                    {
                        "timestamp": "09112023-0905",
                        "free_spaces": 609,
                        "occupied_spaces": 86,
                        "max_spaces": 695,
                    },
                    {
                        "timestamp": "09112023-0910",
                        "free_spaces": 600,
                        "occupied_spaces": 95,
                        "max_spaces": 695,
                    },
                ],
            },
        }

        parkhouses_data = generate_parkhouse_data(raw_data_list)

        self.assertDictEqual(parkhouses_data, expected_parkhouse_data)

    def test_export_parkhouses_data_to_individual_files(self):
        parkhouses_data = {
            "Dern-Passage": {
                "name": "Dern-Passage",
                "occupation_data": [
                    {
                        "timestamp": "09112023-0905",
                        "free_spaces": 120,
                        "occupied_spaces": 79,
                        "max_spaces": 199,
                    },
                    {
                        "timestamp": "09112023-0910",
                        "free_spaces": 100,
                        "occupied_spaces": 99,
                        "max_spaces": 199,
                    },
                ],
            },
            "Karstadt": {
                "name": "Karstadt",
                "occupation_data": [
                    {
                        "timestamp": "09112023-0905",
                        "free_spaces": 609,
                        "occupied_spaces": 86,
                        "max_spaces": 695,
                    },
                    {
                        "timestamp": "09112023-0910",
                        "free_spaces": 600,
                        "occupied_spaces": 95,
                        "max_spaces": 695,
                    },
                ],
            },
        }

        with tempfile.TemporaryDirectory() as destination_data_dir:
            export_parkhouse_data(destination_data_dir, parkhouses_data)

            karstadt_json = os.path.join(destination_data_dir, "karstadt.json")
            dern_json = os.path.join(destination_data_dir, "dern-passage.json")
            self.assertTrue(os.path.exists(karstadt_json))
            self.assertTrue(os.path.exists(dern_json))



class TestHelperFunctions(unittest.TestCase):
    def test_convert_timestamp_from_custom_to_epoch_seconds(self):
        epoch_timestamp = convert_timestamp_to_epoch_seconds("09112023-0900")

        self.assertEqual(epoch_timestamp, 1699520400)


if __name__ == "__main__":
    unittest.main()
