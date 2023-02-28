import re
lines = [
    "Tarek Al-Wazir: 2:18:00 - 2:18:55",
    "Angela Dorn: 1:17:52 - 1:25:20. Questions: 1:25:50 - 1:28:40"
]

regex = r"^([\w\s]+?):\s+([\d:]+)\s*-\s*([\d:]+)(?:\.\s*(Questions?):\s*([\d:]+)\s*-\s*([\d:]+))?$"

match = re.match(regex, line)

if match:
    name = match.group(1)
    begin_speech = match.group(2)
    end_speech = match.group(3)
    has_questions = match.group(4) is not None
    if has_questions:
        questions_begin = match.group(5)
        questions_end = match.group(6)
    else:
        questions_begin = None
        questions_end = None
    print(name, begin_speech, end_speech, has_questions, questions_begin, questions_end)
