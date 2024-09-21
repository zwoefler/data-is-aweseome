# Parkleitsystem Gießen

Historische Auslastung Gießener Parkhäuser seit Oktober 2023.

:parkleitsystem


### ❓️ Fragen
#### Woher kommen die Daten?
Von der Webseite des Parkleitsystems der Universitätsstadt Gießen
🔗 URL: https://www.giessen.de/Umwelt_und_Verkehr/Parken/


#### Kann ich den Daten vertrauen?
Ich kann nur darstellen was ich auslesen kann.

Nicht jedes Gießener Parkhaus ist an das Parkleitsystem angeschlossen.
Einige liefern keine oder falsche Daten (Am Kino).
Andere liefern immer die selben Daten, sind also nicht aussagekräftig.


#### Wie hast du die Daten erfasst?
Ein Script schaut alle fünf Minuten auf der Webseite des [Parkleitsystems Gießen](https://www.giessen.de/Umwelt_und_Verkehr/Parken/) nach Änderungen.
Dabei werden die Daten des Systems ca. alle fünf Minuten aktualisiert.

In der Tabelle zur Auslastung der Parkhäuser steht:
- Name des Parkhauses
- freie Parkplätze und
- verfügbaren Parkplätze.

Gibt es eine Ändeurng, liest das Script die Daten aus der Tabelle zu den Auslastungen und speichert sie.

#### Warum zeigt die Dern-Passage nur eine grade Linie an?
Das Parkhaus Dern-Passage aktualisiert ihre Daten nicht.


#### Warum gibt es im Juli keine Daten?
Fehler meinerseits.
Zwischen dem 26.06 und 06.08 hat meine Automatisierung versagt.

#### Warum "springen" die Datenpunkte?
An Tageswecheln "springen" die Daten teilweise rauf und runter.

Das Parkleitsystem aktualisiert die Daten nur zwischen ca. 9 Uhr und 21 Uhr.
Für die Nacht gibt es keine aktualisierten Daten.

Wenn Parkhäuser früher öffnen oder später schließen ist ist das hier nicht abgebildet.

