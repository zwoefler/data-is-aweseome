with open('timestamps.txt', 'r') as file:
    lines = file.readlines()

segments = []
timestampLines = []
for i, line in enumerate(lines):
    strippedLine = line.strip()
    if len(strippedLine) > 8 and strippedLine[1] == ':' and strippedLine[4] == ':':  # check if line starts with a valid timestamp
        timestampLines.append(strippedLine)
print(timestampLines)

for i, line in enumerate(timestampLines):
    splitLine = line.split(' - ')
    print(splitLine)
    start = splitLine[0].strip()
    name = splitLine[1].strip()
    try:
        end = timestampLines[i+1].split(' - ')[0].strip()
    except IndexError:
        end = ""
    segments.append({'startSegment': start, 'name': name, 'endTime': end})

print(segments)