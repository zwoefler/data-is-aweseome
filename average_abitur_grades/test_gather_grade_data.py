import unittest
import json
import gather_grade_data

url = "https://www.kmk.org/dokumentation-statistik/statistik/schulstatistik/abiturnoten.html"

class TestGatherGradeData(unittest.TestCase):
    def test_return_list_of_xlsx_for_given_HTML(self):
        excel_links = gather_grade_data.get_xlsx_links(url)

        self.assertIsInstance(excel_links, list)
        self.assertGreater(len(excel_links), 2)
        for link in excel_links:
            self.assertTrue("https://www.kmk.org" in link)
            self.assertTrue(link.endswith(".xlsx"))

    def test_providing_grade_excel_returns_json_as_JSON(self):
        excel_file = "test_data/Schnellmeldung_Abiturnoten_2022.xlsx"
        grade_json = gather_grade_data.return_excel_as_JSON(excel_file)

        self.assertIsInstance(grade_json, dict)
        self.assertEqual(grade_json["year"], 2022)
        self.assertEqual(len(grade_json["states"]), 16)
        self.assertAlmostEqual(grade_json["states"]["BW"]["Notenmittel"], 2.23, places=1)
        self.assertEqual(grade_json["states"]["HH"]["Zahl der Prüfungen"], 9210)
        self.assertAlmostEqual(grade_json["states"]["SH"]["- nicht bestanden (%)"], 4.6, places=1)


    def test_get_correct_year_from_excel_file(self):
        excel_file = "test_data/Schnellmeldung_Abiturnoten_2022.xlsx"
        year = gather_grade_data.get_year_of_grade_report(excel_file)

        self.assertEqual(year, 2022)

if __name__ == '__main__':
    unittest.main()