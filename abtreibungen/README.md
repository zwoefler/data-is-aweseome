# Abtreibungen visualization
Abtreibung= Abortion

1. Get abortion data from destatis/genesis online database
2. Visualize

## Docs
This is by far the most complicated API interface and usage I have ever seen :). However, there is some help from the folks in this docs:

Link: https://www-genesis.destatis.de/genesis/misc/GENESIS-Webservices_Einfuehrung.pdf

Page 8.
2.1 Allgemeines
Der vorliegende RESTful-Webservice umfasst mehr als 40 Methoden, die auf die folgenden
Services aufgeteilt sind:
 HelloWorld: Methoden zum ersten Testen der API
Bsp: Test der Anmeldung im System mit den Zugangsdaten.
 Find: Methoden zum Finden von Informationen
Bsp: Tabellen mit Daten zu „Import“
 Cataloque: Methoden zum Auflisten von Objekten
Bsp: Tabellen aus der Statistik „Mikrozensus“
 Data: Methoden zum Herunterladen von Daten
Bsp: Tabelle „11111-0002 – Gebietsfläche: Kreise, Stichtag“
 Metadata: Methoden zum Herunterladen von Metadaten
Bsp: Statistik 11111 –Feststellung des Gebietsstandes
 Profile: Methoden zur Pflege des eigenen Accounts
Bsp: Passwort ändern.


The OpenAPI docs: https://destatis.api.bund.dev/

## Steps
1. Create Destatis account: https://www-genesis.destatis.de/genesis/online?Menu=RegistrierungForm&REGKUNDENTYP=001#abreadcrumb


---
Source:

Nutzungsrechte/Copyright

© Statistisches Bundesamt 2023
Vervielfältigung und Verbreitung, auch auszugsweise, mit Quellenangabe gestattet.
