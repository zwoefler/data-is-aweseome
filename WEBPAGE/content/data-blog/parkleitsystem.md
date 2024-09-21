# Parkleitsystem Gießen

Historische Auslastung Gießener Parkhäuser seit Oktober 2023.

:parkleitsystem


### ❓️ Fragen
#### Woher kommen die Daten?
Webseite des Parkleitsystems der Universitätsstadt Gießen
🔗 URL: https://www.giessen.de/Umwelt_und_Verkehr/Parken/


#### Wie verlässlich sind die Daten?
Ich kann nur darstellen was ich auslesen kann.

Nicht jedes Gießener Parkhaus ist an das Parkleitsystem angeschlossen.
Einige liefern keine oder falsche Daten (Am Kino).
Andere liefern nie ändernde Daten.

#### Wie hast du die Daten erfasst?
Ein Script schaut alle fünf Minuten auf der Webseite des [Parkleitsystems Gießen](https://www.giessen.de/Umwelt_und_Verkehr/Parken/) nach Änderungen.
Dabei werden die Daten des Systems in einer Tabelle ca. alle fünf Minuten aktualisiert.

In der Tabelle zur Auslastung der Parkhäuser stehen:
- Name des Parkhauses
- freie Parkplätze und
- verfügbaren Parkplätze.
Diese Daten lese ich aus.

Bei Änderungen, liest das Script die Daten aus der Tabelle aus.

#### Hat das Karstadtparkhaus nicht mehr Parkplätze?
Laut der Seite des Parkleitsystems, ja.

In der Auflistung gibt die Webseite 860 Stellplätze für das Parkhaus an.
An das Leitsystem scheinen aber nur noch 380 Stelplätze angeschlossen zu sein.
Am Freitag 14.06.24 sank die Anzahl maximal verfügbarer Parkplätze von 475 auf 380 (95 Parkplätze) im Parkleitsystem.


#### Warum zeigt die Dern-Passage nur eine grade Linie an?
Das Parkhaus Dern-Passage aktualisiert ihre Daten nicht.


#### Warum sind fehlen Daten Anfang März?
Zwischen Mittag 29.02.24 und dem 05.03 morgens fehlen Daten.
Hier war die Webseite des Parkleitsystems nicht zu erreichen und teils kaputt.

#### Warum gibt es im Juli keine Daten?
Fehler meinerseits.
Zwischen dem 26.06 und 06.08 hat meine Automatisierung versagt.

#### Warum "springen" die Datenpunkte?
An Tageswecheln "springen" die Daten teilweise rauf und runter.

Das Parkleitsystem aktualisiert die Daten nur zwischen ca. 9 Uhr und 21 Uhr.
Für die Nacht gibt es keine aktualisierten Daten.

Wenn Parkhäuser früher öffnen oder später schließen ist ist das hier nicht abgebildet.

