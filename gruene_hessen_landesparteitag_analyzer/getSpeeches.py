import re


# Read lines from speeches.md

# For each line if pattern like so:
# Tarek Al-Wazir: 1:36:45 - 1:42:35. Questions: 1:43:05 - 1:46:37
# (?<name>(.*?):).*?((?<begin>[^-])-(?!-)[^.]+).*?(?<end>-[^.]+$)

# "Angela Dorn: 2:01:55 - 2:07:40"
line_string = "Tarek Al-Wazir: 1:36:45 - 1:42:35. Questions: 1:43:05 - 1:46:37"
pattern = re.compile("^(?P<name>.*?):.*?(?P<beginSpeech>[\d]*?:[\d]*?:[\d]*?) .*?(?P<endSpeech>[\d]*?:[\d]*?:[\d]*?)\..*? ")
matches = pattern.match(line_string)
# match = re.search('(?<name>(.*?):).*?((?<begin>[^-])-(?!-)[^.]+).*?(?<end>-[^.]+$)', line_string)

print(matches.group("name"))
print(matches.group("beginSpeech"))
print(matches.group("endSpeech"))