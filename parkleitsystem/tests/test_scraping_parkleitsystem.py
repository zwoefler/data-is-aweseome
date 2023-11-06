import unittest
import scraping_parkleitsystem

class DefaultHTMLDataExtraction(unittest.TestCase):
    def setUp(self):
        self.html = """
            <span class="free">Frei: 120</span>
        """


    def tearDown(self):
        self.html = ""


    def test_return_error_item_could_not_be_found(self):
        search_object = {
            "html_element": "div",
            "html_attribute": "class",
            "attribute_value": "free"
        }

        expected_error_message = "No div element with class 'free' found"

        with self.assertRaises(TypeError) as exception:
            html_info = scraping_parkleitsystem.get_text_from_html_tag(self.html, search_object)
        self.assertEqual(str(exception.exception), "No div element with class 'free' found")


    def test_returns_correct_parkhouse_data_for_correct_html(self):
        parkhouse_html_div = """
        <div class="info-panel">
            <span class="slot-name">Dern-Passage</span>
            <div class="slot-count">
                <span class="free">Frei: 120</span> | <span class="max">Gesamt: 199</span>
            </div>
        </div>
        """

        expected_parkhouse_return_value = {
            "name": "Dern-Passage",
            "free_spaces": 120,
            "occupied_spaces": 79,
            "max_spaces": 199
        }

        parkhouse_info = scraping_parkleitsystem.extract_parkhouse_data_from_html_tag(parkhouse_html_div)

        self.assertEqual(parkhouse_info, expected_parkhouse_return_value)


    def test_returns_list_with_parkhouse_data(self):
        parkhouse_data = scraping_parkleitsystem.extract_parkhouse_data(PAGE_HTML)

        self.assertIsInstance(parkhouse_data, list)
        self.assertIsInstance(parkhouse_data[0], dict)
        self.assertIs(len(parkhouse_data), 8)

        for parkhouse_dict in parkhouse_data:
            self.assertIn("name", parkhouse_dict)
            self.assertIn("free_spaces", parkhouse_dict)
            self.assertIn("occupied_spaces", parkhouse_dict)
            self.assertIn("max_spaces", parkhouse_dict)


    def test_scrape_correct_information_from_valid_html(self):
        parkhouse_information = scraping_parkleitsystem.scrape_webpage(PAGE_HTML)

        self.assertIsInstance(parkhouse_information["timestamp"], str)
        self.assertIsInstance(parkhouse_information, dict)
        self.assertIsInstance(parkhouse_information["parkhouses"], list)
        self.assertIs(len(parkhouse_information["parkhouses"]), 8)

        for parkhouse_dict in parkhouse_information["parkhouses"]:
            self.assertIn("name", parkhouse_dict)
            self.assertIn("free_spaces", parkhouse_dict)
            self.assertIn("occupied_spaces", parkhouse_dict)
            self.assertIn("max_spaces", parkhouse_dict)


    def test_get_correct_html_list_from_parkhouse_html(self):
        search_object = {
            "html_element": "div",
            "html_attribute": "class",
            "attribute_value": "parken-giessen"
        }

        return_html = scraping_parkleitsystem.get_text_from_html_tag(PAGE_HTML, search_object)

        self.assertIn("Zuletzt aktualisiert: ", return_html)
        self.assertIn('<span class="slot-name">Dern-Passage</span>', return_html)


    def test_get_last_updated_time(self):
        last_updated = scraping_parkleitsystem.get_last_updated_time(PAGE_HTML)
        self.assertEqual(last_updated, "13102023-1900")


if __name__ == '__main__':
    unittest.main()




PAGE_HTML = """

                    <a id="sprungziel_seiteninhalt"></a><div class="sprungziel"><strong>Seiteninhalt</strong></div>
                     <h1 class="page-title">Parken in Gießen</h1><div style="display:inline">
<ul class="flex-row">


                    <li class="cards flex-col-1">
                        <a href="/Leben/Verkehr-und-Mobilit%C3%A4t/Parken/index.php?object=tx%7c2874.5&amp;ModID=7&amp;FID=2874.57855.1&amp;NavID=1894.57&amp;La=1">
                                                            <div class="icon" aria-hidden="true">


                                    <i aria-hidden="true" title="Handyparken" class="far fa-mobile-phone"></i>
                                </div>
                                                        <div class="caption">
                                                                    <h2 class="title">Handyparken</h2>
                                                                          <p>In Gießen können Parkgebühren mit dem Handy per App gezahlt werden.</p>
                                                                 </div>
                        </a>
                    </li>

                      </ul>
<hr style="width: 100%; text-align: left; margin-left: 0; height: 1px;">
<h2>Aktuelle Auslastung der Parkhäuser des Parkleitsystems:</h2>
<h3><span style="color: #ba0000;"><em class="fa-solid fa-triangle-exclamation"></em>&nbsp; Tchnische Störung: die Daten sind leider nicht aktuell. Wir arbeiten an der Behebung des Problems!</span></h3>
<p>&nbsp;</p>
<div class="parken-giessen">
	<div class="elem slot-3">
				<div class="lights color-green"></div>

		<div class="info-panel">
			<span class="slot-name">Dern-Passage</span>
			<div class="slot-count">
				<span class="free">Frei: 120</span> | <span class="max">Gesamt: 199</span>
			</div>
		</div>
		<div class="location pull-right">
			<a class="csslink_extern" href="https://giessen.maps.arcgis.com/home/webmap/viewer.html?webmap=812366fe60d2456da69c7f581a0c2968&amp;center=8.668556,50.582447&amp;level=18" title="Zum Parkhaus" target="_blank">Standort</a>
		</div>
	</div>
		<hr>

	<div class="elem slot-4">
				<div class="lights color-green"></div>

		<div class="info-panel">
			<span class="slot-name">Karstadt</span>
			<div class="slot-count">
				<span class="free">Frei: 595</span> | <span class="max">Gesamt: 695</span>
			</div>
		</div>
		<div class="location pull-right">
			<a class="csslink_extern" href="https://giessen.maps.arcgis.com/home/webmap/viewer.html?webmap=812366fe60d2456da69c7f581a0c2968&amp;center=8.670187,50.583401&amp;level=18" title="Zum Parkhaus" target="_blank">Standort</a>
		</div>
	</div>
		<hr>

	<div class="elem slot-5">
				<div class="lights color-green"></div>

		<div class="info-panel">
			<span class="slot-name">Liebig-Center</span>
			<div class="slot-count">
				<span class="free">Frei: 237</span> | <span class="max">Gesamt: 250</span>
			</div>
		</div>
		<div class="location pull-right">
			<a class="csslink_extern" href="https://giessen.maps.arcgis.com/home/webmap/viewer.html?webmap=812366fe60d2456da69c7f581a0c2968&amp;center=8.666876,50.583407&amp;level=18" title="Zum Parkhaus" target="_blank">Standort</a>
		</div>
	</div>
		<hr>

	<div class="elem slot-6">
				<div class="lights color-green"></div>

		<div class="info-panel">
			<span class="slot-name">NeustÃ€dter Tor</span>
			<div class="slot-count">
				<span class="free">Frei: 536</span> | <span class="max">Gesamt: 870</span>
			</div>
		</div>
		<div class="location pull-right">
			<a class="csslink_extern" href="https://giessen.maps.arcgis.com/home/webmap/viewer.html?webmap=812366fe60d2456da69c7f581a0c2968&amp;center=8.67069,50.587879&amp;level=18" title="Zum Parkhaus" target="_blank">Standort</a>
		</div>
	</div>
		<hr>

	<div class="elem slot-7">
				<div class="lights color-green"></div>

		<div class="info-panel">
			<span class="slot-name">Rathaus</span>
			<div class="slot-count">
				<span class="free">Frei: 114</span> | <span class="max">Gesamt: 250</span>
			</div>
		</div>
		<div class="location pull-right">
			<a class="csslink_extern" href="https://giessen.maps.arcgis.com/home/webmap/viewer.html?webmap=812366fe60d2456da69c7f581a0c2968&amp;center=8.679392,50.584818&amp;level=18" title="Zum Parkhaus" target="_blank">Standort</a>
		</div>
	</div>
		<hr>

	<div class="elem slot-8">
				<div class="lights color-green"></div>

		<div class="info-panel">
			<span class="slot-name">Selters Tor</span>
			<div class="slot-count">
				<span class="free">Frei: 118</span> | <span class="max">Gesamt: 158</span>
			</div>
		</div>
		<div class="location pull-right">
			<a class="csslink_extern" href="https://giessen.maps.arcgis.com/home/webmap/viewer.html?webmap=812366fe60d2456da69c7f581a0c2968&amp;center=8.671646,50.581752&amp;level=18" title="Zum Parkhaus" target="_blank">Standort</a>
		</div>
	</div>
		<hr>

	<div class="elem slot-9">
				<div class="lights color-green"></div>

		<div class="info-panel">
			<span class="slot-name">Westanlage</span>
			<div class="slot-count">
				<span class="free">Frei: 217</span> | <span class="max">Gesamt: 235</span>
			</div>
		</div>
		<div class="location pull-right">
			<a class="csslink_extern" href="https://giessen.maps.arcgis.com/home/webmap/viewer.html?webmap=812366fe60d2456da69c7f581a0c2968&amp;center=8.668449,50.58573&amp;level=18" title="Zum Parkhaus" target="_blank">Standort</a>
		</div>
	</div>
		<hr>

	<div class="elem slot-10">
				<div class="lights color-green"></div>

		<div class="info-panel">
			<span class="slot-name">Am Bahnhof</span>
			<div class="slot-count">
				<span class="free">Frei: 179</span> | <span class="max">Gesamt: 242</span>
			</div>
		</div>
		<div class="location pull-right">
			<a class="csslink_extern" href="https://giessen.maps.arcgis.com/home/webmap/viewer.html?webmap=812366fe60d2456da69c7f581a0c2968&amp;center=8.665101,50.580103&amp;level=18" title="Zum Parkhaus" target="_blank">Standort</a>
		</div>
	</div>
	<br><small class="last-update">Zuletzt aktualisiert: 19:00 Uhr - 13.10.2023</small>
</div>
<p>Das&nbsp;<strong>Parkleitsystem der Stadt Gießen</strong>&nbsp;weist Ihnen&nbsp;bei der Parkplatzsuche den Weg. Mittels erkennbarer Zuordnung der Parkhäuser in vier Parkzonen sowie dynamischen Wegweisern werden die jeweils aktuellen freien Stellplätze der angeschlossenen Parkhäuser bereits auf den Haupteinfallstraßen angezeigt.</p>
<div>
			<h2 class="toggler-title active" id="acc-1-1" aria-controls="sect-1-1" aria-expanded="true" tabindex="0">Alle Parkhäuser - Tiefgaragen - Parkplätze</h2>
			<div class="toggler-container" id="sect-1-1" aria-labelledby="acc-1-1" role="region" style="">
				<div class="tog-size">

<div class="adressen">

			<div class="elem row">

<address class="liste-text column-1">


			<h4 class="liste-titel">
							<a href="/Leben/Verkehr-und-Mobilit%C3%A4t/Parken/index.php?object=tx,2874.1&amp;ModID=9&amp;FID=1894.27.1&amp;NavID=1894.57&amp;La=1" title="Detailansicht der Adresse anzeigen">Parkhaus Am Kino</a>
					</h4>
			<div class="row">
			<div class="column-2">
						<p>
						379 Stellplätze | Angeschlossen an elektronisches Parkleitsystem<br>1.00 € pro Stunde | Tageskarte 5.00 € | Sondertarif Kino 1.50 € für 4h <br>Mo-Fr 11:00-5:00 Uhr | Sa-So 00:00-24:00 Uhr<br>					</p>
									<p>
						Am Alten Gaswerk&nbsp;5<br>35390&nbsp;Gießen<br>					</p>
							</div>
			<div class="column-2">
				</div>
		</div>
			<p>
										<a class="btn csslink_extern" href="https://giessen.maps.arcgis.com/apps/webappviewer/index.html?id=dd2d284b8e15419489d1fb5edc79232a&amp;find=Am+Alten+Gaswerk+5%2C+35390+Gie%C3%9Fen" target="_blank" title="Externer Link: Digitaler Stadtplan Gießen">Karte anzeigen</a>
								</p>

</address>			</div>
							<hr class="trenner spacer">

			<div class="elem row">

<address class="liste-text column-1">


			<h4 class="liste-titel">
							<a href="/Leben/Verkehr-und-Mobilit%C3%A4t/Parken/index.php?object=tx,2874.1&amp;ModID=9&amp;FID=1894.419.1&amp;NavID=1894.57&amp;La=1" title="Detailansicht der Adresse anzeigen">Parkhaus Bahnhof</a>
					</h4>
			<div class="row">
			<div class="column-2">
						<p>
						247 Stellplätze | angeschlossen an elektronisches Parkleitsystem<br>je angefangene Stunde 1.70 € | Tagestarif 6.00 €<br>Montag-Sonntag 00:00-24:00 Uhr<br>					</p>
									<p>
						An der Alten Post&nbsp;6<br>35390&nbsp;Gießen<br>					</p>
							</div>
			<div class="column-2">
						<p>

								<a href="http://www.dbbahnpark.de/content/fahrplanauskunft/bahnpark/pdf/8000124.pdf" target="_blank" title="Externer Link" class="web">Website</a><br>
												</p>
							</div>
		</div>
			<p>
										<a class="btn csslink_extern" href="https://giessen.maps.arcgis.com/apps/webappviewer/index.html?id=dd2d284b8e15419489d1fb5edc79232a&amp;find=An+der+Alten+Post+6%2C+35390+Gie%C3%9Fen" target="_blank" title="Externer Link: Digitaler Stadtplan Gießen">Karte anzeigen</a>
								</p>

</address>			</div>
							<hr class="trenner spacer">

			<div class="elem row">

<address class="liste-text column-1">


			<h4 class="liste-titel">
							<a href="/Leben/Verkehr-und-Mobilit%C3%A4t/Parken/index.php?object=tx,2874.1&amp;ModID=9&amp;FID=1894.29.1&amp;NavID=1894.57&amp;La=1" title="Detailansicht der Adresse anzeigen">Parkplatz Brandplatz</a>
					</h4>
			<div class="row">
			<div class="column-2">
						<p>
						70 Stellplätze<br>Rund um die Uhr außer Mi und Sa 05:00-15:30 Uhr<br>					</p>
									<p>
						Brandplatz<br>					</p>
							</div>
			<div class="column-2">
				</div>
		</div>
			<p>
										<a class="btn csslink_extern" href="https://giessen.maps.arcgis.com/apps/webappviewer/index.html?id=dd2d284b8e15419489d1fb5edc79232a&amp;find=8.676655,50.587367&amp;level=18" target="_blank" title="Externer Link: Digitaler Stadtplan Gießen">Karte anzeigen</a>
								</p>

</address>			</div>
							<hr class="trenner spacer">

			<div class="elem row">

<address class="liste-text column-1">


			<h4 class="liste-titel">
							<a href="/Leben/Verkehr-und-Mobilit%C3%A4t/Parken/index.php?object=tx,2874.1&amp;ModID=9&amp;FID=1894.26.1&amp;NavID=1894.57&amp;La=1" title="Detailansicht der Adresse anzeigen">Parkhaus DB Lahnstraße (P+R)</a>
					</h4>
			<div class="row">
			<div class="column-2">
						<p>
						450 Stellplätze<br>Montag-Sonntag 00:00-24:00 Uhr<br>					</p>
									<p>
						Lahnstraße&nbsp;55<br>35398&nbsp;Gießen<br>					</p>
							</div>
			<div class="column-2">
				</div>
		</div>
			<p>
										<a class="btn csslink_extern" href="https://giessen.maps.arcgis.com/apps/webappviewer/index.html?id=dd2d284b8e15419489d1fb5edc79232a&amp;find=Lahnstra%C3%9Fe+55%2C+35398+Gie%C3%9Fen" target="_blank" title="Externer Link: Digitaler Stadtplan Gießen">Karte anzeigen</a>
								</p>

</address>			</div>
							<hr class="trenner spacer">

			<div class="elem row">

<address class="liste-text column-1">


			<h4 class="liste-titel">
							<a href="/Leben/Verkehr-und-Mobilit%C3%A4t/Parken/index.php?object=tx,2874.1&amp;ModID=9&amp;FID=1894.25.1&amp;NavID=1894.57&amp;La=1" title="Detailansicht der Adresse anzeigen">Parkhaus Dern Passage</a>
					</h4>
			<div class="row">
			<div class="column-2">
						<p>
						199 Stellplätze | angeschlossen an elektronisches Parkleitsystem<br>1. Stunde 1.00 € | jede weitere 1.50 € | Höchsttarif 6.00 €<br>Mo, Di, Mi, Fr 07:00-20:00 Uhr | Do 07:00-21:00 Uhr | Sa 7:00-19:00 Uhr | So geschl.<br>					</p>
									<p>
						Westanlage&nbsp;21<br>35390&nbsp;Gießen<br>					</p>
							</div>
			<div class="column-2">
				</div>
		</div>
			<p>
										<a class="btn csslink_extern" href="https://giessen.maps.arcgis.com/apps/webappviewer/index.html?id=dd2d284b8e15419489d1fb5edc79232a&amp;find=Westanlage+21%2C+35390+Gie%C3%9Fen" target="_blank" title="Externer Link: Digitaler Stadtplan Gießen">Karte anzeigen</a>
								</p>

</address>			</div>
							<hr class="trenner spacer">

			<div class="elem row">

<address class="liste-text column-1">


			<h4 class="liste-titel">
							<a href="/Leben/Verkehr-und-Mobilit%C3%A4t/Parken/index.php?object=tx,2874.1&amp;ModID=9&amp;FID=684.10501.1&amp;NavID=1894.57&amp;La=1" title="Detailansicht der Adresse anzeigen">Parkplatz Johannesstraße</a>
					</h4>
			<div class="row">
			<div class="column-2">
						<p>
						80 Stellplätze<br>Montag-Sonntag 00:00-24:00 Uhr<br>					</p>
									<p>
						Johannesstraße<br>					</p>
							</div>
			<div class="column-2">
				</div>
		</div>
			<p>
					</p>

</address>			</div>
							<hr class="trenner spacer">

			<div class="elem row">

<address class="liste-text column-1">


			<h4 class="liste-titel">
							<a href="/Leben/Verkehr-und-Mobilit%C3%A4t/Parken/index.php?object=tx,2874.1&amp;ModID=9&amp;FID=1894.35.1&amp;NavID=1894.57&amp;La=1" title="Detailansicht der Adresse anzeigen">Parkhaus Karstadt</a>
					</h4>
			<div class="row">
			<div class="column-2">
						<p>
						860 Stellplätze | angeschlossen an elektronisches Parkleitsystem<br>je angefangene Stunde 1.50 € | Höchsttarif 15.00 €<br>Mo-Fr 07:00-19:30 Uhr | Sa 07:00-18:30 Uhr | So geschl., an verkaufsoffenen Sonntagen geöffnet.<br>					</p>
									<p>
						Reichensand&nbsp;10<br>35390&nbsp;Gießen<br>					</p>
							</div>
			<div class="column-2">
				</div>
		</div>
			<p>
										<a class="btn csslink_extern" href="https://giessen.maps.arcgis.com/apps/webappviewer/index.html?id=dd2d284b8e15419489d1fb5edc79232a&amp;find=Reichensand+10%2C+35390+Gie%C3%9Fen" target="_blank" title="Externer Link: Digitaler Stadtplan Gießen">Karte anzeigen</a>
								</p>

</address>			</div>
							<hr class="trenner spacer">

			<div class="elem row">

<address class="liste-text column-1">


			<h4 class="liste-titel">
							<a href="/Leben/Verkehr-und-Mobilit%C3%A4t/Parken/index.php?object=tx,2874.1&amp;ModID=9&amp;FID=1894.30.1&amp;NavID=1894.57&amp;La=1" title="Detailansicht der Adresse anzeigen">Parkplatz Kongresshalle</a>
					</h4>
			<div class="row">
			<div class="column-2">
						<p>
						Mo-Sa: 07:00-19:00 Uhr (gebührenpflichtig)<br>					</p>
									<p>
						Lonystraße<br>					</p>
							</div>
			<div class="column-2">
				</div>
		</div>
			<p>
										<a class="btn csslink_extern" href="https://giessen.maps.arcgis.com/apps/webappviewer/index.html?id=dd2d284b8e15419489d1fb5edc79232a&amp;find=8.678058,50.583241&amp;level=18" target="_blank" title="Externer Link: Digitaler Stadtplan Gießen">Karte anzeigen</a>
								</p>

</address>			</div>
							<hr class="trenner spacer">

			<div class="elem row">

<address class="liste-text column-1">


			<h4 class="liste-titel">
							<a href="/Leben/Verkehr-und-Mobilit%C3%A4t/Parken/index.php?object=tx,2874.1&amp;ModID=9&amp;FID=2874.39.1&amp;NavID=1894.57&amp;La=1" title="Detailansicht der Adresse anzeigen">Parkhaus Lahnstraße</a>
					</h4>
			<div class="row">
			<div class="column-2">
						<p>
						je angefangene Stunde 1.50 € | Tagestarif 4.50 € (24 h)<br>					</p>
									<p>
						Lahnstraße&nbsp;1<br>35398&nbsp;Gießen<br>					</p>
							</div>
			<div class="column-2">
				</div>
		</div>
			<p>
										<a class="btn csslink_extern" href="https://giessen.maps.arcgis.com/apps/webappviewer/index.html?id=dd2d284b8e15419489d1fb5edc79232a&amp;find=Lahnstra%C3%9Fe+1%2C+35398+Gie%C3%9Fen" target="_blank" title="Externer Link: Digitaler Stadtplan Gießen">Karte anzeigen</a>
								</p>

</address>			</div>
							<hr class="trenner spacer">

			<div class="elem row">

<address class="liste-text column-1">


			<h4 class="liste-titel">
							<a href="/Leben/Verkehr-und-Mobilit%C3%A4t/Parken/index.php?object=tx,2874.1&amp;ModID=9&amp;FID=1894.34.1&amp;NavID=1894.57&amp;La=1" title="Detailansicht der Adresse anzeigen">Parkhaus Liebig-Center</a>
					</h4>
			<div class="row">
			<div class="column-2">
						<p>
						380 Stellplätze | angeschlossen an elektronisches Parkleitsystem<br>1. Stunde 1.50 € | jede weitere Stunde 1.30 €<br>Mo-Sa 06:00-21:00 Uhr | So geschl.<br>					</p>
									<p>
						Flutgraben&nbsp;4<br>35390&nbsp;Gießen<br>					</p>
							</div>
			<div class="column-2">
				</div>
		</div>
			<p>
										<a class="btn csslink_extern" href="https://giessen.maps.arcgis.com/apps/webappviewer/index.html?id=dd2d284b8e15419489d1fb5edc79232a&amp;find=Flutgraben+4%2C+35390+Gie%C3%9Fen" target="_blank" title="Externer Link: Digitaler Stadtplan Gießen">Karte anzeigen</a>
								</p>

</address>			</div>
							<hr class="trenner spacer">

			<div class="elem row">

<address class="liste-text column-1">


			<h4 class="liste-titel">
							<a href="/Leben/Verkehr-und-Mobilit%C3%A4t/Parken/index.php?object=tx,2874.1&amp;ModID=9&amp;FID=1894.37.1&amp;NavID=1894.57&amp;La=1" title="Detailansicht der Adresse anzeigen">Parkplatz Messeplatz</a>
					</h4>
			<div class="row">
			<div class="column-2">
						<p>
						1300 Stellplätze<br>					</p>
									<p>
						Ringallee<br>					</p>
							</div>
			<div class="column-2">
				</div>
		</div>
			<p>
										<a class="btn csslink_extern" href="https://giessen.maps.arcgis.com/apps/webappviewer/index.html?id=dd2d284b8e15419489d1fb5edc79232a&amp;find=8.682693,50.590311&amp;level=18" target="_blank" title="Externer Link: Digitaler Stadtplan Gießen">Karte anzeigen</a>
								</p>

</address>			</div>
							<hr class="trenner spacer">

			<div class="elem row">

<address class="liste-text column-1">


			<h4 class="liste-titel">
							<a href="/Leben/Verkehr-und-Mobilit%C3%A4t/Parken/index.php?object=tx,2874.1&amp;ModID=9&amp;FID=1894.36.1&amp;NavID=1894.57&amp;La=1" title="Detailansicht der Adresse anzeigen">Parkhaus Neustädter Tor</a>
					</h4>
			<div class="row">
			<div class="column-2">
						<p>
						1060 Stellplätze | angeschlossen an elektronisches Parkleitsystem<br>1.-3. Stunde jeweils 1.50 € | jeder weitere 2.00 € | Sparticket 3.50 € für 6h <br>Mo-Sa 07:00-23:00 Uhr | So 10:00-23:00 Uhr<br>					</p>
									<p>
						Neustadt&nbsp;28<br>35390&nbsp;Gießen<br>					</p>
							</div>
			<div class="column-2">
				</div>
		</div>
			<p>
										<a class="btn csslink_extern" href="https://giessen.maps.arcgis.com/apps/webappviewer/index.html?id=dd2d284b8e15419489d1fb5edc79232a&amp;find=Neustadt+28%2C+35390+Gie%C3%9Fen" target="_blank" title="Externer Link: Digitaler Stadtplan Gießen">Karte anzeigen</a>
								</p>

</address>			</div>
							<hr class="trenner spacer">

			<div class="elem row">

<address class="liste-text column-1">


			<h4 class="liste-titel">
							<a href="/Leben/Verkehr-und-Mobilit%C3%A4t/Parken/index.php?object=tx,2874.1&amp;ModID=9&amp;FID=1894.28.1&amp;NavID=1894.57&amp;La=1" title="Detailansicht der Adresse anzeigen">Parkhaus Q-West</a>
					</h4>
			<div class="row">
			<div class="column-2">
						<p>
						560 Stellplätze  | angeschlossen an elektronisches Parkleitsystem<br>je angefangene Stunde 2.00 € | Höchstsatz 6.00 €<br>Mo-Sa 05:00-22:00 Uhr | So 07:00-22:00 Uhr<br>					</p>
									<p>
						Westanlage&nbsp;44<br>35390&nbsp;Gießen<br>					</p>
							</div>
			<div class="column-2">
				</div>
		</div>
			<p>
										<a class="btn csslink_extern" href="https://giessen.maps.arcgis.com/apps/webappviewer/index.html?id=dd2d284b8e15419489d1fb5edc79232a&amp;find=Westanlage+44%2C+35390+Gie%C3%9Fen" target="_blank" title="Externer Link: Digitaler Stadtplan Gießen">Karte anzeigen</a>
								</p>

</address>			</div>
							<hr class="trenner spacer">

			<div class="elem row">

<address class="liste-text column-1">


			<h4 class="liste-titel">
							<a href="/Leben/Verkehr-und-Mobilit%C3%A4t/Parken/index.php?object=tx,2874.1&amp;ModID=9&amp;FID=684.10499.1&amp;NavID=1894.57&amp;La=1" title="Detailansicht der Adresse anzeigen">Parkhaus/Tiefgarage Rathaus</a>
					</h4>
			<div class="row">
			<div class="column-2">
						<p>
						250 Stellplätze  | angeschlossen an elektronisches Parkleitsystem<br>1.00 € pro angefangene Stunde | Höchsttarif 5.00 €<br>Montag-Sonntag 00:00-24:00 Uhr<br>					</p>
									<p>
						Berliner Platz&nbsp;1<br>Einfahrt Ostanlage 45 (Adresse für Navi)<br>35390&nbsp;Gießen<br>					</p>
							</div>
			<div class="column-2">
						<p>
														<span class="phone" title="Telefon">0641 306-1052</span><br>
												</p>
							</div>
		</div>
			<p>
										<a class="btn csslink_extern" href="https://giessen.maps.arcgis.com/apps/webappviewer/index.html?id=dd2d284b8e15419489d1fb5edc79232a&amp;find=Berliner+Platz+1%2C+35390+Gie%C3%9Fen" target="_blank" title="Externer Link: Digitaler Stadtplan Gießen">Karte anzeigen</a>
															<a class="btn ztx" href="/Leben/Verkehr-und-Mobilit%C3%A4t/Parken/index.php?object=tx,2874.1&amp;ModID=9&amp;FID=684.10499.1&amp;NavID=1894.57&amp;La=1" title="Weitere Informationen anzeigen">Weitere Informationen</a>
										</p>

</address>			</div>
							<hr class="trenner spacer">

			<div class="elem row">

<address class="liste-text column-1">


			<h4 class="liste-titel">
							<a href="/Leben/Verkehr-und-Mobilit%C3%A4t/Parken/index.php?object=tx,2874.1&amp;ModID=9&amp;FID=684.10502.1&amp;NavID=1894.57&amp;La=1" title="Detailansicht der Adresse anzeigen">Parkhaus THM/Ringallee</a>
					</h4>
			<div class="row">
			<div class="column-2">
						<p>
						380 Stellplätze<br>Montag-Sonntag 00:00-24:00 Uhr<br>					</p>
									<p>
						Ringallee&nbsp;6<br>35396&nbsp;Gießen<br>					</p>
							</div>
			<div class="column-2">
				</div>
		</div>
			<p>
										<a class="btn csslink_extern" href="https://giessen.maps.arcgis.com/apps/webappviewer/index.html?id=dd2d284b8e15419489d1fb5edc79232a&amp;find=Ringallee+6%2C+35396+Gie%C3%9Fen" target="_blank" title="Externer Link: Digitaler Stadtplan Gießen">Karte anzeigen</a>
								</p>

</address>			</div>
							<hr class="trenner spacer">

			<div class="elem row">

<address class="liste-text column-1">


			<h4 class="liste-titel">
							<a href="/Leben/Verkehr-und-Mobilit%C3%A4t/Parken/index.php?object=tx,2874.1&amp;ModID=9&amp;FID=1894.33.1&amp;NavID=1894.57&amp;La=1" title="Detailansicht der Adresse anzeigen">Parkhaus Selters Tor</a>
					</h4>
			<div class="row">
			<div class="column-2">
						<p>
						152 Stellplätze  | angeschlossen an elektronisches Parkleitsystem<br>je angefangene Stunde 1.60 € |Höchsttarif 10.00 €<br>Montag-Sonntag 06:00-23:00 Uhr<br>					</p>
									<p>
						Südanlage&nbsp;26<br>35390&nbsp;Gießen<br>					</p>
							</div>
			<div class="column-2">
				</div>
		</div>
			<p>
										<a class="btn csslink_extern" href="https://giessen.maps.arcgis.com/apps/webappviewer/index.html?id=dd2d284b8e15419489d1fb5edc79232a&amp;find=S%C3%BCdanlage+26%2C+35390+Gie%C3%9Fen" target="_blank" title="Externer Link: Digitaler Stadtplan Gießen">Karte anzeigen</a>
								</p>

</address>			</div>
							<hr class="trenner spacer">

			<div class="elem row">

<address class="liste-text column-1">


			<h4 class="liste-titel">
							<a href="/Leben/Verkehr-und-Mobilit%C3%A4t/Parken/index.php?object=tx,2874.1&amp;ModID=9&amp;FID=2874.375.1&amp;NavID=1894.57&amp;La=1" title="Detailansicht der Adresse anzeigen">Parkhaus/Tiefgarage Sparkasse</a>
					</h4>
			<div class="row">
			<div class="column-2">
						<p>
						Johannesstraße&nbsp;5<br>35390&nbsp;Gießen<br>					</p>
							</div>
			<div class="column-2">
				</div>
		</div>
			<p>
										<a class="btn csslink_extern" href="https://giessen.maps.arcgis.com/apps/webappviewer/index.html?id=dd2d284b8e15419489d1fb5edc79232a&amp;find=Johannesstra%C3%9Fe+5%2C+35390+Gie%C3%9Fen" target="_blank" title="Externer Link: Digitaler Stadtplan Gießen">Karte anzeigen</a>
								</p>

</address>			</div>
							<hr class="trenner spacer">

			<div class="elem row">

<address class="liste-text column-1">


			<h4 class="liste-titel">
							<a href="/Leben/Verkehr-und-Mobilit%C3%A4t/Parken/index.php?object=tx,2874.1&amp;ModID=9&amp;FID=684.10503.1&amp;NavID=1894.57&amp;La=1" title="Detailansicht der Adresse anzeigen">Parkplatz Stadtwerke Gießen</a>
					</h4>
			<div class="row">
			<div class="column-2">
						<p>
						200 Stellplätze<br>Mo-Do 18:00-24:00 Uhr | Fr ab 14:00 Uhr<br>					</p>
									<p>
						Lahnstraße<br>					</p>
							</div>
			<div class="column-2">
				</div>
		</div>
			<p>
					</p>

</address>			</div>
							<div class="spacer"></div>
				</div>
				</div>
			</div>
		</div>
<p>&nbsp;</p>
<p><a target="_blank" href="/redirect.phtml?extlink=1&amp;La=1&amp;url_fid=2874.2703.1" title="Externer Link" class="btn">Parkmöglichkeiten in der Karte anzeigen</a></p>
</div>
"""

