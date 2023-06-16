import os
import unittest
import gather_grade_data

url = "https://www.kmk.org/dokumentation-statistik/statistik/schulstatistik/abiturnoten.html"
archive_url = "https://www.kmk.org/dokumentation-statistik/statistik/schulstatistik/abiturnoten/archiv-abiturnoten.html"

class TestAggregateGradeData(unittest.TestCase):
    def test_true(self):
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()