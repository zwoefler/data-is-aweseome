import unittest
import generate_parkleitsystem_data

class SummarizeParkleitsystemData(unittest.TestCase):
    def test_dont_add_data_when_already_exists(self):
        existing_data = [
            { "timestamp": "01112023-0925", "parkhouses": [ { "name": "Dern-Passage", "free_spaces": 120, "occupied_spaces": 79, "max_spaces": 199 }, { "name": "Karstadt", "free_spaces": 608, "occupied_spaces": 87, "max_spaces": 695 }, { "name": "Liebig-Center", "free_spaces": 241, "occupied_spaces": 9, "max_spaces": 250 }, { "name": "Neust\u00c3\u20acdter Tor", "free_spaces": 428, "occupied_spaces": 442, "max_spaces": 870 }, { "name": "Rathaus", "free_spaces": 61, "occupied_spaces": 109, "max_spaces": 170 }, { "name": "Selters Tor", "free_spaces": 34, "occupied_spaces": 124, "max_spaces": 158 }, { "name": "Westanlage", "free_spaces": 217, "occupied_spaces": 18, "max_spaces": 235 }, { "name": "Am Bahnhof", "free_spaces": 184, "occupied_spaces": 58, "max_spaces": 242 } ] },
            { "timestamp": "01112023-0930", "parkhouses": [ { "name": "Dern-Passage", "free_spaces": 120, "occupied_spaces": 79, "max_spaces": 199 }, { "name": "Karstadt", "free_spaces": 595, "occupied_spaces": 100, "max_spaces": 695 }, { "name": "Liebig-Center", "free_spaces": 241, "occupied_spaces": 9, "max_spaces": 250 }, { "name": "Neust\u00c3\u20acdter Tor", "free_spaces": 409, "occupied_spaces": 461, "max_spaces": 870 }, { "name": "Rathaus", "free_spaces": 55, "occupied_spaces": 115, "max_spaces": 170 }, { "name": "Selters Tor", "free_spaces": 37, "occupied_spaces": 121, "max_spaces": 158 }, { "name": "Westanlage", "free_spaces": 217, "occupied_spaces": 18, "max_spaces": 235 }, { "name": "Am Bahnhof", "free_spaces": 184, "occupied_spaces": 58, "max_spaces": 242 } ] },
            { "timestamp": "01112023-0934", "parkhouses": [ { "name": "Dern-Passage", "free_spaces": 120, "occupied_spaces": 79, "max_spaces": 199 }, { "name": "Karstadt", "free_spaces": 587, "occupied_spaces": 108, "max_spaces": 695 }, { "name": "Liebig-Center", "free_spaces": 241, "occupied_spaces": 9, "max_spaces": 250 }, { "name": "Neust\u00c3\u20acdter Tor", "free_spaces": 397, "occupied_spaces": 473, "max_spaces": 870 }, { "name": "Rathaus", "free_spaces": 49, "occupied_spaces": 121, "max_spaces": 170 }, { "name": "Selters Tor", "free_spaces": 32, "occupied_spaces": 126, "max_spaces": 158 }, { "name": "Westanlage", "free_spaces": 217, "occupied_spaces": 18, "max_spaces": 235 }, { "name": "Am Bahnhof", "free_spaces": 184, "occupied_spaces": 58, "max_spaces": 242 } ] }
        ]

        new_data = [
            { "timestamp": "01112023-0934", "parkhouses": [ { "name": "Dern-Passage", "free_spaces": 120, "occupied_spaces": 79, "max_spaces": 199 }, { "name": "Karstadt", "free_spaces": 587, "occupied_spaces": 108, "max_spaces": 695 }, { "name": "Liebig-Center", "free_spaces": 241, "occupied_spaces": 9, "max_spaces": 250 }, { "name": "Neust\u00c3\u20acdter Tor", "free_spaces": 397, "occupied_spaces": 473, "max_spaces": 870 }, { "name": "Rathaus", "free_spaces": 49, "occupied_spaces": 121, "max_spaces": 170 }, { "name": "Selters Tor", "free_spaces": 32, "occupied_spaces": 126, "max_spaces": 158 }, { "name": "Westanlage", "free_spaces": 217, "occupied_spaces": 18, "max_spaces": 235 }, { "name": "Am Bahnhof", "free_spaces": 184, "occupied_spaces": 58, "max_spaces": 242 } ] }
        ]

        parkleitsystem_data = generate_parkleitsystem_data.add_new_data(existing_data, new_data)
        self.assertIsInstance(parkleitsystem_data, list)




if __name__ == '__main__':
    unittest.main()

