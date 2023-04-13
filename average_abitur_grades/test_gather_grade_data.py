import os
import unittest
import gather_grade_data

url = "https://www.kmk.org/dokumentation-statistik/statistik/schulstatistik/abiturnoten.html"
archive_url = "https://www.kmk.org/dokumentation-statistik/statistik/schulstatistik/abiturnoten/archiv-abiturnoten.html"

class TestGatherGradeData(unittest.TestCase):
    def test_return_list_of_xls_for_given_html(self):
        with open('test_data/Archiv - Abiturnoten.html') as f:
            html_string = f.read()
        excel_links = gather_grade_data.get_xlsx_links(html_string)

        assert_link_2018 = excel_links[1]
        self.assertTrue("https://www.kmk.org" in assert_link_2018)
        self.assertGreater(len(excel_links), 5)
        self.assertTrue(assert_link_2018.endswith('.xls'))


    def test_return_list_of_xlsx_for_given_HTML(self):
        with open('test_data/Abiturnoten.html') as f:
            html_string = f.read()
        excel_links = gather_grade_data.get_xlsx_links(html_string)

        real_links = ['https://www.kmk.org/fileadmin/Dateien/pdf/Statistik/Dokumentationen/Schnellmeldung_Abiturnoten_2022.xlsx', 'https://www.kmk.org/fileadmin/Dateien/pdf/Statistik/Dokumentationen/Aus_Abiturnoten_2021.xlsx', 'https://www.kmk.org/fileadmin/Dateien/pdf/Statistik/Dokumentationen/Aus_Abiturnoten_2020_Werte.xlsx']

        self.assertIsInstance(excel_links, list)
        self.assertGreater(len(excel_links), 2)
        for link in excel_links:
            self.assertTrue("https://www.kmk.org" in link)
            self.assertTrue(link.endswith(".xlsx"))


        self.assertEqual(excel_links, real_links)

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


    def test_get_correct_excel_file_name(self):
        excel_link = 'https://www.kmk.org/fileadmin/Dateien/pdf/Statistik/Dokumentationen/Aus_Abiturnoten_2020_Werte.xlsx'
        filename = gather_grade_data.get_excel_file_name(excel_link)

        self.assertEqual(filename, "Aus_Abiturnoten_2020_Werte.xlsx")


    def test_for_excel_files_return_valid_JSON(self):
        excel_files_list = ["Schnellmeldung_Abiturnoten_2022.xlsx"]
        abitur_grade_json = gather_grade_data.abitur_grades_as_JSON(excel_files_list, folder='test_data')

        self.assertTrue(os.path.exists('excel_files/'))
        self.assertIsInstance(abitur_grade_json, dict)
        self.assertIsInstance(abitur_grade_json[2022], dict)
        self.assertAlmostEqual(abitur_grade_json[2022]["states"]["BW"]["Notenmittel"], 2.23, places=1)


    def test_calculated_average_grade_for_country(self):
        excel_files_list = ["Schnellmeldung_Abiturnoten_2022.xlsx"]
        abitur_grade_json = gather_grade_data.abitur_grades_as_JSON(excel_files_list, folder='test_data')

        self.assertAlmostEqual(abitur_grade_json[2022]["average_grade"], 2.28, places=2)
        self.assertEqual(abitur_grade_json[2022]["number_of_tests"], 311804)
        self.assertEqual(abitur_grade_json[2022]["passed"], 299787)
        self.assertEqual(abitur_grade_json[2022]["number_failed"], 12017)
        self.assertAlmostEqual(abitur_grade_json[2022]["percentage_failed"], 3.85, places=2)

        self.assertEqual(abitur_grade_json[2022]["grades"][2.3], 14979)
        self.assertEqual(len(abitur_grade_json[2022]["grades"]), 31)


    def test_form_zip_link_to_excel_files(self):
        archive_zip_url = "https://kmk.org/fileadmin/Dateien/pdf/Statistik/Aus_Abiturnoten_2006_2013.zip"
        extract_folder = 'extract_folder'
        list_of_excel_files = gather_grade_data.download_excel_files_from_zip_download(archive_zip_url, extract_folder)

        self.assertEqual(len(list_of_excel_files), 8)
        self.assertTrue(list_of_excel_files[5].endswith('.xls'))


    def test_average_grade_for_total_exists_as_own_timeline(self):
        excel_files_list = ["Schnellmeldung_Abiturnoten_2022.xlsx"]
        abitur_grade_json = gather_grade_data.abitur_grades_as_JSON(excel_files_list, folder='test_data')

        self.assertEqual(abitur_grade_json["average_grade"]["Total"][-1], 2.279767968591033)
        self.assertEqual(abitur_grade_json["average_grade"]["NI"][-1], 2.383948497854077)

    def test_grade_json_has_label_list_with_years(self):
        excel_files_list = ["Schnellmeldung_Abiturnoten_2022.xlsx"]
        abitur_grade_json = gather_grade_data.abitur_grades_as_JSON(excel_files_list, folder='test_data')

        self.assertTrue(abitur_grade_json["years"])


if __name__ == '__main__':
    unittest.main()