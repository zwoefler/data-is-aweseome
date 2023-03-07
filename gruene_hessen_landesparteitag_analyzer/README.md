# Grüne Hessen Landesparteitag SpeechAnalyzer
Kinda goal is to paste a youtube video, get the speech as text and offer a frontend to edit and select the text and run analysis.
Analysis could be:
- Counted words
- Most similar words being used
- Automatic topic and sentiment analysis

Want a frontend to put YouTube link, select your range of time for the video, ge tthe text for that area.

1. Basic Webpage with list of places ons list and links to speeches (only text)
2. Include timestamps in speech
3. Embedd Video on YouTube starting at that timestamp
4. Word-Count overview
5. Summary Word-Count with sentiment (renewable energies, wind and solar, etc. are one group!)

## Do CI
1. getSpeechesInfo.py
2. transcribeSpeeches.py
3. summarizeSpeeches.py
4. includeYouTubeID.py


## Steps
- Download youtube video
- Write Python script to
    iterate timestamps
    cut audio into clips
    push to whisper
    get text
    save text
- Save text
- get text from video/audio (per timestamp)
- split into indiviudal speeches
- include "text", "name", speaker_id" in the JSON file

# Timestamps
## 1. Place
Angela Dorn: 1:17:52 - 1:25:20. Questions: 1:25:50 - 1:28:40

## 2. Place
Tarek Al-Wazir: 1:36:45 - 1:42:35. Questions: 1:43:05 - 1:46:37
Joachim Mietusch: 1:47:35 - 1:53:25. Questions: 1:53:40 - 1:55:54

## Antrag auf das Votum der MP-Kandidatur
Angela Dorn: 2:01:55 - 2:07:40
Tarek Al-Wazir: 2:09:43 - 2:14:40

Sigrid Erfurth: 2:15:45 - 2:17:44
Tarek Al-Wazir: 2:18:00 - 2:18:55


##
Michael Kolmer: 2:22:00 - 1:23:15
Manuela Rottmann: 2:23:28 - 2:24:07
Sven Schöller: 2:24:22 - 2:25:11
Sigrid Hansen: 2:25:26 - 2:26:30

## 3. Place
Martina Feldmayer: 2:27:45 - 2:33:11. Questions: 2:33:41 - 2:36:01

## 4. Place
Mathias Wagner: 2:42:20 - 2:47:20. Questions: 2:47:50 - 2:49:30

## 5. Place
Eva Goldbach: 2:54:39 - 3:00:02. Questions 3:00:30 - 3:03:12
Lara Klaes: 3:03:43 - 3:08:46. Questions: 3:09:23 - 3:11:00
Katy Walther: 3:11:23 - 3:16:13. Questions: 3:16:50 - 3:18:56

## 6. Place
Robert Erkan: 3:29:58 - 3:35:25. Questions: 3:36:00 - 3:38:10
Jürgen Frömmrich: 3:38:53 - 3:44:27. Questions: 3:45:00 - 3:47:26
Patricia Peveling: 3:48:10 - 3:53:45. Questions: 3:54:15 - 3:56:00
Ingo Stürmer: 3:56:20 - 4:01:45. Questions: 4:02:06 - 4:03:50

## 7. Place
Kaya Kinkel: 4:15:48 - 4:21:02. Questions: 4:21:43 - 4:24:12

## 8. Place
Marcus Bockelt: 4:30:50 - 4:35:36. Questions: 4:36:10 - 4:38:00
Sebastian Schaub: 4:38:22 - 4:42:59. Questions: 4:43:30 - 4:45:50

## 9. Place
Hildegard Förster-Heldmann: 4:50:16 - 4:56:05. Questions: 4:56:40 - 4:58:25
Anja Zeller: 4:58:49 - 5:04:07. Questions: 5:04:30 - 5:05:50

## 10. Place
Daniel May: 5:15:45 - 5:20:07. Questions: 5:20:30 - 5:22:40
Sabine Schwöbel-Lehmann: 5:23:10 - 5:28:45. Questions: 5:29:08 - 5:5:30:43









