import re


regex = re.compile(r'^'
                   r'(?P<name>[^:]+):\s*'
                   r'(?P<beginSpeech>\d+:\d+:\d+)\s*-\s*'
                   r'(?P<endSpeech>\d+:\d+:\d+)'
                   r'(?:\.\s+(?P<question>[Qq]uestions?)\s*:?\s*'
                   r'(?P<beginQuestions>\d+:\d+:\d+)\s*-\s*'
                   r'(?P<endQuestions>\d+:\d+:\d+))?')

with open("speeches.md", "r") as file:
    lines = file.readlines()
    for line in lines:
        match = regex.match(line)
        if match:
            info = match.groupdict()
            print(info)