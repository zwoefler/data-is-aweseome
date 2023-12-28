import json
import re
import sys
import os

regex = re.compile(r'^'
                   r'(?:(?P<reminder>Reminder\.\s))?'
                   r'(?P<name>[^:]+):\s*'
                   r'(?P<beginSpeech>\d+:\d+:\d+)\s*-\s*'
                   r'(?P<endSpeech>\d+:\d+:\d+)'
                   r'(?:\.\s+(?P<question>[Qq]uestions?)\s*:?\s*'
                   r'(?P<beginQuestions>\d+:\d+:\d+)\s*-\s*'
                   r'(?P<endQuestions>\d+:\d+:\d+))?')

filename = sys.argv[1]
exportname = os.path.splitext(filename)[0] + "_info.json"

with open(filename, "r") as file:
    lines = file.readlines()
    speeches_info = []
    for line in lines:
        match = regex.match(line)
        if match:
            info = match.groupdict()
            speeches_info.append(info)

with open(exportname, "w") as outfile:
    json.dump(speeches_info, outfile)