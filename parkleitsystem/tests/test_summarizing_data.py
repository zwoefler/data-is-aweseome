import unittest
import generate_parkleitsystem_data
import json
import os

class FileSystemTests(unittest.TestCase):
    def setUp(self):
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


    def test_read_json_data_from_file(self):
        json_path = self.fake_json_path
        expected_json_data = self.fake_json

        json_data = generate_parkleitsystem_data.read_json_file(json_path)

        self.assertEqual(json_data, expected_json_data)


    def test_write_json_data_to_file(self):
        fake_json_path = self.fake_json_path
        json_data = self.fake_json
        generate_parkleitsystem_data.write_json_to_file(fake_json_path, json_data)

        self.assertTrue(os.path.exists(fake_json_path))


    def test_list_of_files_from_directory(self):
        data_directory = self.fake_directory
        fake_files_list = self.fake_files_list

        list_of_files = generate_parkleitsystem_data.list_files_in_directory(data_directory)

        self.assertIsInstance(list_of_files, list)
        self.assertEqual(len(list_of_files), len(fake_files_list))
        self.assertIn("fake_directory/fake_file_1.json", list_of_files[0])
        self.assertIn(data_directory, list_of_files[0])
        self.assertIn(fake_files_list[0], list_of_files[0])


    def test_Error_when_list_of_files_input_is_not_string(self):
        invalid_directory_list = ["Something"]

        with self.assertRaises(TypeError) as context:
            generate_parkleitsystem_data.list_files_in_directory(invalid_directory_list)

        self.assertIn("path should be string", str(context.exception))


    def test_throw_Error_when_data_directory_doesnt_exist(self):
        wrong_data_directory = "wrong_directory"

        with self.assertRaises(FileNotFoundError):
            generate_parkleitsystem_data.list_files_in_directory(wrong_data_directory)


class ExtractSingleParkhouseSystem(unittest.TestCase):
    def test_extract_single_parkhouse_data_from_parkhouse_entry(self):
        example_parkhouse_data = {
            "timestamp": "01112023-0900",
            "parkhouses": [
                { "name": "Karstadt", "free_spaces": 637, "occupied_spaces": 58, "max_spaces": 695 },
                { "name": "Dern-Passage", "free_spaces": 120, "occupied_spaces": 79, "max_spaces": 199 }
            ]
        }
        result_parkhouse_data = {
            "name": "Dern-Passage",
            "timestamp": "01112023-0900",
            "free_spaces": 120,
            "occupied_spaces": 79,
            "max_spaces": 199
        }

        parkhouse_name = "Dern-Passage"
        single_parkhouse_data = generate_parkleitsystem_data.extract_single_parkhouse_info(parkhouse_name, example_parkhouse_data)

        self.assertIsInstance(single_parkhouse_data, dict)
        self.assertEqual(single_parkhouse_data, result_parkhouse_data)
        self.assertIn(parkhouse_name, single_parkhouse_data["name"])


    # def test_valid_parkhouse_info_list_returns_list_with_single_parkhouse_info(self):

    #     generate_parkleitsystem_data.extract_parkhouse_info




class SummarizeParkleitsystemData(unittest.TestCase):
    def test_add_new_data_to_existing_data(self):
        existing_data = [
            { "timestamp": "01112023-0925", "parkhouses": [ { "name": "Dern-Passage", "free_spaces": 120, "occupied_spaces": 79, "max_spaces": 199 }, { "name": "Karstadt", "free_spaces": 608, "occupied_spaces": 87, "max_spaces": 695 }, { "name": "Liebig-Center", "free_spaces": 241, "occupied_spaces": 9, "max_spaces": 250 }, { "name": "Neust\u00c3\u20acdter Tor", "free_spaces": 428, "occupied_spaces": 442, "max_spaces": 870 }, { "name": "Rathaus", "free_spaces": 61, "occupied_spaces": 109, "max_spaces": 170 }, { "name": "Selters Tor", "free_spaces": 34, "occupied_spaces": 124, "max_spaces": 158 }, { "name": "Westanlage", "free_spaces": 217, "occupied_spaces": 18, "max_spaces": 235 }, { "name": "Am Bahnhof", "free_spaces": 184, "occupied_spaces": 58, "max_spaces": 242 } ] },
            { "timestamp": "01112023-0930", "parkhouses": [ { "name": "Dern-Passage", "free_spaces": 120, "occupied_spaces": 79, "max_spaces": 199 }, { "name": "Karstadt", "free_spaces": 595, "occupied_spaces": 100, "max_spaces": 695 }, { "name": "Liebig-Center", "free_spaces": 241, "occupied_spaces": 9, "max_spaces": 250 }, { "name": "Neust\u00c3\u20acdter Tor", "free_spaces": 409, "occupied_spaces": 461, "max_spaces": 870 }, { "name": "Rathaus", "free_spaces": 55, "occupied_spaces": 115, "max_spaces": 170 }, { "name": "Selters Tor", "free_spaces": 37, "occupied_spaces": 121, "max_spaces": 158 }, { "name": "Westanlage", "free_spaces": 217, "occupied_spaces": 18, "max_spaces": 235 }, { "name": "Am Bahnhof", "free_spaces": 184, "occupied_spaces": 58, "max_spaces": 242 } ] },
            { "timestamp": "01112023-0934", "parkhouses": [ { "name": "Dern-Passage", "free_spaces": 120, "occupied_spaces": 79, "max_spaces": 199 }, { "name": "Karstadt", "free_spaces": 587, "occupied_spaces": 108, "max_spaces": 695 }, { "name": "Liebig-Center", "free_spaces": 241, "occupied_spaces": 9, "max_spaces": 250 }, { "name": "Neust\u00c3\u20acdter Tor", "free_spaces": 397, "occupied_spaces": 473, "max_spaces": 870 }, { "name": "Rathaus", "free_spaces": 49, "occupied_spaces": 121, "max_spaces": 170 }, { "name": "Selters Tor", "free_spaces": 32, "occupied_spaces": 126, "max_spaces": 158 }, { "name": "Westanlage", "free_spaces": 217, "occupied_spaces": 18, "max_spaces": 235 }, { "name": "Am Bahnhof", "free_spaces": 184, "occupied_spaces": 58, "max_spaces": 242 } ] }
        ]

        new_data = { "timestamp": "01112023-0936", "parkhouses": [ { "name": "Dern-Passage", "free_spaces": 120, "occupied_spaces": 79, "max_spaces": 199 }, { "name": "Karstadt", "free_spaces": 587, "occupied_spaces": 108, "max_spaces": 695 }, { "name": "Liebig-Center", "free_spaces": 241, "occupied_spaces": 9, "max_spaces": 250 }, { "name": "Neust\u00c3\u20acdter Tor", "free_spaces": 397, "occupied_spaces": 473, "max_spaces": 870 }, { "name": "Rathaus", "free_spaces": 49, "occupied_spaces": 121, "max_spaces": 170 }, { "name": "Selters Tor", "free_spaces": 32, "occupied_spaces": 126, "max_spaces": 158 }, { "name": "Westanlage", "free_spaces": 217, "occupied_spaces": 18, "max_spaces": 235 }, { "name": "Am Bahnhof", "free_spaces": 184, "occupied_spaces": 58, "max_spaces": 242 } ] }

        final_data = [
            { "timestamp": "01112023-0925", "parkhouses": [ { "name": "Dern-Passage", "free_spaces": 120, "occupied_spaces": 79, "max_spaces": 199 }, { "name": "Karstadt", "free_spaces": 608, "occupied_spaces": 87, "max_spaces": 695 }, { "name": "Liebig-Center", "free_spaces": 241, "occupied_spaces": 9, "max_spaces": 250 }, { "name": "Neust\u00c3\u20acdter Tor", "free_spaces": 428, "occupied_spaces": 442, "max_spaces": 870 }, { "name": "Rathaus", "free_spaces": 61, "occupied_spaces": 109, "max_spaces": 170 }, { "name": "Selters Tor", "free_spaces": 34, "occupied_spaces": 124, "max_spaces": 158 }, { "name": "Westanlage", "free_spaces": 217, "occupied_spaces": 18, "max_spaces": 235 }, { "name": "Am Bahnhof", "free_spaces": 184, "occupied_spaces": 58, "max_spaces": 242 } ] },
            { "timestamp": "01112023-0930", "parkhouses": [ { "name": "Dern-Passage", "free_spaces": 120, "occupied_spaces": 79, "max_spaces": 199 }, { "name": "Karstadt", "free_spaces": 595, "occupied_spaces": 100, "max_spaces": 695 }, { "name": "Liebig-Center", "free_spaces": 241, "occupied_spaces": 9, "max_spaces": 250 }, { "name": "Neust\u00c3\u20acdter Tor", "free_spaces": 409, "occupied_spaces": 461, "max_spaces": 870 }, { "name": "Rathaus", "free_spaces": 55, "occupied_spaces": 115, "max_spaces": 170 }, { "name": "Selters Tor", "free_spaces": 37, "occupied_spaces": 121, "max_spaces": 158 }, { "name": "Westanlage", "free_spaces": 217, "occupied_spaces": 18, "max_spaces": 235 }, { "name": "Am Bahnhof", "free_spaces": 184, "occupied_spaces": 58, "max_spaces": 242 } ] },
            { "timestamp": "01112023-0934", "parkhouses": [ { "name": "Dern-Passage", "free_spaces": 120, "occupied_spaces": 79, "max_spaces": 199 }, { "name": "Karstadt", "free_spaces": 587, "occupied_spaces": 108, "max_spaces": 695 }, { "name": "Liebig-Center", "free_spaces": 241, "occupied_spaces": 9, "max_spaces": 250 }, { "name": "Neust\u00c3\u20acdter Tor", "free_spaces": 397, "occupied_spaces": 473, "max_spaces": 870 }, { "name": "Rathaus", "free_spaces": 49, "occupied_spaces": 121, "max_spaces": 170 }, { "name": "Selters Tor", "free_spaces": 32, "occupied_spaces": 126, "max_spaces": 158 }, { "name": "Westanlage", "free_spaces": 217, "occupied_spaces": 18, "max_spaces": 235 }, { "name": "Am Bahnhof", "free_spaces": 184, "occupied_spaces": 58, "max_spaces": 242 } ] },
            { "timestamp": "01112023-0936", "parkhouses": [ { "name": "Dern-Passage", "free_spaces": 120, "occupied_spaces": 79, "max_spaces": 199 }, { "name": "Karstadt", "free_spaces": 587, "occupied_spaces": 108, "max_spaces": 695 }, { "name": "Liebig-Center", "free_spaces": 241, "occupied_spaces": 9, "max_spaces": 250 }, { "name": "Neust\u00c3\u20acdter Tor", "free_spaces": 397, "occupied_spaces": 473, "max_spaces": 870 }, { "name": "Rathaus", "free_spaces": 49, "occupied_spaces": 121, "max_spaces": 170 }, { "name": "Selters Tor", "free_spaces": 32, "occupied_spaces": 126, "max_spaces": 158 }, { "name": "Westanlage", "free_spaces": 217, "occupied_spaces": 18, "max_spaces": 235 }, { "name": "Am Bahnhof", "free_spaces": 184, "occupied_spaces": 58, "max_spaces": 242 } ] }
        ]

        parkleitsystem_data = generate_parkleitsystem_data.add_new_data(existing_data, new_data)
        self.assertIsInstance(parkleitsystem_data, list)
        self.assertEqual(parkleitsystem_data, final_data)


    def test_dont_add_existing_data(self):
        existing_data = [
            { "timestamp": "01112023-0925", "parkhouses": [ { "name": "Dern-Passage", "free_spaces": 120, "occupied_spaces": 79, "max_spaces": 199 }, { "name": "Karstadt", "free_spaces": 608, "occupied_spaces": 87, "max_spaces": 695 }, { "name": "Liebig-Center", "free_spaces": 241, "occupied_spaces": 9, "max_spaces": 250 }, { "name": "Neust\u00c3\u20acdter Tor", "free_spaces": 428, "occupied_spaces": 442, "max_spaces": 870 }, { "name": "Rathaus", "free_spaces": 61, "occupied_spaces": 109, "max_spaces": 170 }, { "name": "Selters Tor", "free_spaces": 34, "occupied_spaces": 124, "max_spaces": 158 }, { "name": "Westanlage", "free_spaces": 217, "occupied_spaces": 18, "max_spaces": 235 }, { "name": "Am Bahnhof", "free_spaces": 184, "occupied_spaces": 58, "max_spaces": 242 } ] },
            { "timestamp": "01112023-0930", "parkhouses": [ { "name": "Dern-Passage", "free_spaces": 120, "occupied_spaces": 79, "max_spaces": 199 }, { "name": "Karstadt", "free_spaces": 595, "occupied_spaces": 100, "max_spaces": 695 }, { "name": "Liebig-Center", "free_spaces": 241, "occupied_spaces": 9, "max_spaces": 250 }, { "name": "Neust\u00c3\u20acdter Tor", "free_spaces": 409, "occupied_spaces": 461, "max_spaces": 870 }, { "name": "Rathaus", "free_spaces": 55, "occupied_spaces": 115, "max_spaces": 170 }, { "name": "Selters Tor", "free_spaces": 37, "occupied_spaces": 121, "max_spaces": 158 }, { "name": "Westanlage", "free_spaces": 217, "occupied_spaces": 18, "max_spaces": 235 }, { "name": "Am Bahnhof", "free_spaces": 184, "occupied_spaces": 58, "max_spaces": 242 } ] },
            { "timestamp": "01112023-0934", "parkhouses": [ { "name": "Dern-Passage", "free_spaces": 120, "occupied_spaces": 79, "max_spaces": 199 }, { "name": "Karstadt", "free_spaces": 587, "occupied_spaces": 108, "max_spaces": 695 }, { "name": "Liebig-Center", "free_spaces": 241, "occupied_spaces": 9, "max_spaces": 250 }, { "name": "Neust\u00c3\u20acdter Tor", "free_spaces": 397, "occupied_spaces": 473, "max_spaces": 870 }, { "name": "Rathaus", "free_spaces": 49, "occupied_spaces": 121, "max_spaces": 170 }, { "name": "Selters Tor", "free_spaces": 32, "occupied_spaces": 126, "max_spaces": 158 }, { "name": "Westanlage", "free_spaces": 217, "occupied_spaces": 18, "max_spaces": 235 }, { "name": "Am Bahnhof", "free_spaces": 184, "occupied_spaces": 58, "max_spaces": 242 } ] }
        ]

        new_data = { "timestamp": "01112023-0934", "parkhouses": [ { "name": "Dern-Passage", "free_spaces": 120, "occupied_spaces": 79, "max_spaces": 199 }, { "name": "Karstadt", "free_spaces": 587, "occupied_spaces": 108, "max_spaces": 695 }, { "name": "Liebig-Center", "free_spaces": 241, "occupied_spaces": 9, "max_spaces": 250 }, { "name": "Neust\u00c3\u20acdter Tor", "free_spaces": 397, "occupied_spaces": 473, "max_spaces": 870 }, { "name": "Rathaus", "free_spaces": 49, "occupied_spaces": 121, "max_spaces": 170 }, { "name": "Selters Tor", "free_spaces": 32, "occupied_spaces": 126, "max_spaces": 158 }, { "name": "Westanlage", "free_spaces": 217, "occupied_spaces": 18, "max_spaces": 235 }, { "name": "Am Bahnhof", "free_spaces": 184, "occupied_spaces": 58, "max_spaces": 242 } ] }

        final_data = [
            { "timestamp": "01112023-0925", "parkhouses": [ { "name": "Dern-Passage", "free_spaces": 120, "occupied_spaces": 79, "max_spaces": 199 }, { "name": "Karstadt", "free_spaces": 608, "occupied_spaces": 87, "max_spaces": 695 }, { "name": "Liebig-Center", "free_spaces": 241, "occupied_spaces": 9, "max_spaces": 250 }, { "name": "Neust\u00c3\u20acdter Tor", "free_spaces": 428, "occupied_spaces": 442, "max_spaces": 870 }, { "name": "Rathaus", "free_spaces": 61, "occupied_spaces": 109, "max_spaces": 170 }, { "name": "Selters Tor", "free_spaces": 34, "occupied_spaces": 124, "max_spaces": 158 }, { "name": "Westanlage", "free_spaces": 217, "occupied_spaces": 18, "max_spaces": 235 }, { "name": "Am Bahnhof", "free_spaces": 184, "occupied_spaces": 58, "max_spaces": 242 } ] },
            { "timestamp": "01112023-0930", "parkhouses": [ { "name": "Dern-Passage", "free_spaces": 120, "occupied_spaces": 79, "max_spaces": 199 }, { "name": "Karstadt", "free_spaces": 595, "occupied_spaces": 100, "max_spaces": 695 }, { "name": "Liebig-Center", "free_spaces": 241, "occupied_spaces": 9, "max_spaces": 250 }, { "name": "Neust\u00c3\u20acdter Tor", "free_spaces": 409, "occupied_spaces": 461, "max_spaces": 870 }, { "name": "Rathaus", "free_spaces": 55, "occupied_spaces": 115, "max_spaces": 170 }, { "name": "Selters Tor", "free_spaces": 37, "occupied_spaces": 121, "max_spaces": 158 }, { "name": "Westanlage", "free_spaces": 217, "occupied_spaces": 18, "max_spaces": 235 }, { "name": "Am Bahnhof", "free_spaces": 184, "occupied_spaces": 58, "max_spaces": 242 } ] },
            { "timestamp": "01112023-0934", "parkhouses": [ { "name": "Dern-Passage", "free_spaces": 120, "occupied_spaces": 79, "max_spaces": 199 }, { "name": "Karstadt", "free_spaces": 587, "occupied_spaces": 108, "max_spaces": 695 }, { "name": "Liebig-Center", "free_spaces": 241, "occupied_spaces": 9, "max_spaces": 250 }, { "name": "Neust\u00c3\u20acdter Tor", "free_spaces": 397, "occupied_spaces": 473, "max_spaces": 870 }, { "name": "Rathaus", "free_spaces": 49, "occupied_spaces": 121, "max_spaces": 170 }, { "name": "Selters Tor", "free_spaces": 32, "occupied_spaces": 126, "max_spaces": 158 }, { "name": "Westanlage", "free_spaces": 217, "occupied_spaces": 18, "max_spaces": 235 }, { "name": "Am Bahnhof", "free_spaces": 184, "occupied_spaces": 58, "max_spaces": 242 } ] },
        ]

        parkleitsystem_data = generate_parkleitsystem_data.add_new_data(existing_data, new_data)

        self.assertIsInstance(parkleitsystem_data, list)
        self.assertEqual(parkleitsystem_data, final_data)




if __name__ == '__main__':
    unittest.main()

