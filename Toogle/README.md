# Toogle
The data for the Tesla Search Engine

## Mission
Every available and official Tesla publication like:
- Earnings Reports
- Presentations (AI-Day, Investor Day, etc.)
- Earnings Calls
- Blog and PR News Entries

in an easily accessable, saerchable and comprehensive manner.

## ToDo
1. Download Investor-Day Video
2. Get timestamps for Video
3. Transscribe one segment via OpenAI-Whisper
4. Summarize segment and generate Buzzwords
5. Automate above process to transcribe every segment from the video
6. Embedd each sentence in the text!
7. Make function to do so for more videos!

In the end the JSON-file for the segment has:
- text
- summary
- buzzwords
- segments
- beginSection (of Video)
- endSection (of Video)
- Speakers
- YouTube-Link (embedded link)
- embeddings for each sentence of text!
