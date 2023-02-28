import re

lines = [
    "Tarek Al-Wazir: 2:18:00 - 2:18:55",
    "Angela Dorn: 1:17:52 - 1:25:20. Questions: 1:25:50 - 1:28:40",
]

regex = re.compile(r'^([^:]+):\s*(\d+:\d+:\d+)\s*-\s*(\d+:\d+:\d+)(?:\.\s+([Qq]uestions?):?\s*(\d+:\d+:\d+)\s*-\s*(\d+:\d+:\d+))?')

for line in lines:
    match = regex.match(line)
    if match:
        name, beginSpeech, endSpeech, question, beginQuestions, endQuestions = match.groups()
        print(name, beginSpeech, endSpeech, question, beginQuestions, endQuestions)
