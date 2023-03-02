import json
import re

regex = re.compile(r'^'
                   r'(?:(?P<reminder>Reminder\.))?'
                   r'(?P<name>[^:]+):\s*'
                   r'(?P<beginSpeech>\d+:\d+:\d+)\s*-\s*'
                   r'(?P<endSpeech>\d+:\d+:\d+)'
                   r'(?:\.\s+(?P<question>[Qq]uestions?)\s*:?\s*'
                   r'(?P<beginQuestions>\d+:\d+:\d+)\s*-\s*'
                   r'(?P<endQuestions>\d+:\d+:\d+))?')


with open("speeches_2.md", "r") as file:
    lines = file.readlines()
    speeches_info = []
    for line in lines:
        match = regex.match(line)
        if match:
            info = match.groupdict()
            speeches_info.append(info)

with open("speeches_info_2.json", "w") as outfile:
    json.dump(speeches_info, outfile)