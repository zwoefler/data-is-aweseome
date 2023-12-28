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
4. includeYouTubeID.py
3. summarizeSpeeches.py

## ToDos
- Simplyfy the process from cutting the videos to having the speeches, texts and summary in one script
- Rework Datastructure to contain database_key, name, youtube_link, summary, text, buzzwords as python list, begin- end- Speech and Question timestamps, language, segments, questions -- ALL directly readable in webapp. No shenanigans!


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
