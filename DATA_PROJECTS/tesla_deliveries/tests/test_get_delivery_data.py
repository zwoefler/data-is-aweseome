import unittest
import subprocess
from bs4 import BeautifulSoup
from tesla_deliveries import extract_totals_from_table, extract_table, fetch_html, extract_publishing_date


class TestURLFunctions(unittest.TestCase):
    # When schem isn't https://, add it to URL in front of www.
    # When internet is not available
    def test_fetch_html(self):
        url = "https://www.google.com"

        html = fetch_html(url)

        self.assertIsInstance(html, str)
        self.assertIn("<html", html)


class TestExtractDataFromPressRelease(unittest.TestCase):
    def test_extract_deliveries_number(self):
        html_table = """
<table >
	<tbody >
		<tr >
			<td >&nbsp;</td>
			<td ><strong>Production</strong></td>
			<td ><strong>Deliveries</strong></td>
			<td ><strong>Subject to operating lease accounting</strong></td>
		</tr>
		<tr >
			<td >Model S/X</td>
			<td >13,688</td>
			<td >15,985</td>
			<td >8%</td>
		</tr>
		<tr >
			<td >Model 3/Y</td>
			<td >416,800</td>
			<td >419,074</td>
			<td >4%</td>
		</tr>
		<tr >
			<td ><strong>Total</strong></td>
			<td ><strong>430,488</strong></td>
			<td ><strong>435,059</strong></td>
			<td ><strong>4%</strong></td>
		</tr>
	</tbody>
</table>
        """
        totals = extract_totals_from_table(html_table)
        self.assertIsInstance(totals, dict)
        self.assertIn("deliveries", totals)
        self.assertEqual(totals["deliveries"], 435059)


    def test_extract_total_production_number(self):
        html_table = """
<table >
	<tbody >
		<tr >
			<td >&nbsp;</td>
			<td ><strong>Production</strong></td>
			<td ><strong>Deliveries</strong></td>
			<td ><strong>Subject to operating lease accounting</strong></td>
		</tr>
		<tr >
			<td >Model S/X</td>
			<td >14,218</td>
			<td >14,724</td>
			<td >17%</td>
		</tr>
		<tr >
			<td >Model 3/Y</td>
			<td >291,189</td>
			<td >295,324</td>
			<td >3%</td>
		</tr>
		<tr >
			<td ><strong>Total</strong></td>
			<td ><strong>305,407</strong></td>
			<td ><strong>310,048</strong></td>
			<td ><strong>4%</strong></td>
		</tr>
	</tbody>
</table>
        """
        totals = extract_totals_from_table(html_table)
        self.assertIsInstance(totals, dict)
        self.assertIn("production", totals)
        self.assertEqual(totals["production"], 305407)

    def test_extract_table_from_HTML(self):
        html = """
        <html>
        <head>
            <title>Sample HTML</title>
        </head>
        <body>
            <h1>This is a heading</h1>
            <p>This is a paragraph.</p>
            <table>
                <tbody>
                    <tr>
                        <td>Row 1, Col 1</td>
                    </tr>
                    <tr>
                        <td>Row 2, Col 1</td>
                    </tr>
                </tbody>
            </table>
        </body>
        </html>
        """
        expected_table = """
        <table>
            <tbody>
                <tr>
                    <td>Row 1, Col 1</td>
                </tr>
                <tr>
                    <td>Row 2, Col 1</td>
                </tr>
            </tbody>
        </table>
        """
        extracted_table = extract_table(html)
        
        bs4_expected_table = BeautifulSoup(expected_table.strip(), "html.parser")
        bs4_extracted_table = BeautifulSoup(extracted_table, "html.parser")

        self.assertEqual(str(bs4_extracted_table), str(bs4_expected_table))
        self.assertIsInstance(extracted_table, str)


    def test_extract_date_from_pressrelease(self):
        """
        Extract the publishing date from the press relesae 
        """

        html = """
        <html>
        <time datetime="2022-04-02T12:00:00Z">Apr 2,      2022</time>
        </html>
        """
       
        publishing_date = extract_publishing_date(html)

        self.assertEqual(publishing_date, "2022-04-02T12:00:00Z")


class TestExtractPressReleaseLinks(unittest.TestCase):
    def test_gets_press_release_links_from_html(self):
        html = """
        <html>
            <div>
                <a href=/press-release/>Press Release</a>
            </div>
        </html>
        """

class TestCLIOptions(unittest.TestCase):
    def test_help_message(self):
        process = subprocess.Popen(['python3', 'tesla_deliveries.py', '-h'], stdout=subprocess.PIPE)
        output, _ = process.communicate()
        output = output.decode("utf-8").strip()

        self.assertIn("usage: tesla_deliveries.py [-h] URL", output)


    def test_no_url_provided(self):
        process = subprocess.Popen(['python3', 'tesla_deliveries.py'], stdout=subprocess.PIPE)
        output, _ = process.communicate()
        output = output.decode("utf-8").strip()

        self.assertIn("usage: tesla_deliveries.py [-h] URL", output)


if __name__ == '__main__':
    unittest.main()
