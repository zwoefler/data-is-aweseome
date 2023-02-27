import re
import os
import whisper
import torch
import json

def getRegexInformationFromString(line_string):
    pattern = re.compile("^(?P<name>.*?):.*?(?P<beginSpeech>[\d]*?:[\d]*?:[\d]*?) .*?(?P<endSpeech>[\d]*?:[\d]*?:[\d]*?)\..*? ")
    matches = pattern.match(line_string)
    info = {
        "name": matches.group("name"),
        "beginSpeech": matches.group("beginSpeech"),
        "endSpeech": matches.group("endSpeech")
    }
    return info


def createExportName(name):
    """Returns the export name based on speaker name"""
    return name.strip().lower().replace(" ", "_")


def cutAudioClip(line_string):
    """
    Cut audio between timestamps and save clip as name (ffmpeg)
    """
    print("Cutting Audio for: ", line_string)
    info = getRegexInformationFromString(line_string)
    export_name = createExportName(info["name"])
    os.system(f"ffmpeg -i landesparteitag_25.02.22_audio.mp3 -ss {info['beginSpeech']} -to {info['endSpeech']} -c copy speeches/{export_name}.mp3")
    return info


def audioToText(audioFile):
    """Transposes Audio File to German Text"""
    model = whisper.load_model("base", device=DEVICE)
    result = model.transcribe(audioFile)

    return result


def transcribeAllClips():
    """Transcribes all mp3 files in folder 'speeches'"""
    folder = "speeches/"
    for f in os.listdir(folder):
        name, ext = os.path.splitext(f)
        if ext == '.mp3':
            print("Transcribing:", name)
            speech = audioToText(f"{folder}/{name}.mp3")
            with open(f"{folder}/{name}.txt", "w") as f:
                f.write(speech["text"])
            with open(f"{folder}/{name}.json", "w") as f:
                json.dump(speech, f)


torch.cuda.is_available()
if torch.cuda.is_available():
    print("CUDA")
    DEVICE = "cuda"
else:
    print("CPU")
    DEVICE = "cpu"

list_of_lines = [
    "Angela Dorn: 1:17:52 - 1:25:20. Questions: 1:25:50 - 1:28:40",
    "Tarek Al-Wazir: 1:36:45 - 1:42:35. Questions: 1:43:05 - 1:46:37",
    "Joachim Mietusch: 1:47:35 - 1:53:25. Questions: 1:53:40 - 1:55:54"
    "Martina Feldmayer: 2:27:45 - 2:33:11. Questions: 2:33:41 - 2:36:01",
    "Mathias Wagner: 2:42:20 - 2:47:20. Questions: 2:47:50 - 2:49:30",
    "Eva Goldbach: 2:54:39 - 3:00:02. Questions 3:00:30 - 3:03:12",
    "Lara Klaes: 3:03:43 - 3:08:46. Questions: 3:09:23 - 3:11:00",
    "Katy Walther: 3:11:23 - 3:16:13. Questions: 3:16:50 - 3:18:56",
    "Robert Erkan: 3:29:58 - 3:35:25. Questions: 3:36:00 - 3:38:10",
    "Jürgen Frömmrich: 3:38:53 - 3:44:27. Questions: 3:45:00 - 3:47:26",
    "Patricia Peveling: 3:48:10 - 3:53:45. Questions: 3:54:15 - 3:56:00",
    "Ingo Stürmer: 3:56:20 - 4:01:45. Questions: 4:02:06 - 4:03:50",
    "Kaya Kinkel: 4:15:48 - 4:21:02. Questions: 4:21:43 - 4:24:12",
    "Marcus Bockelt: 4:30:50 - 4:35:36. Questions: 4:36:10 - 4:38:00",
    "Sebastian Schaub: 4:38:22 - 4:42:59. Questions: 4:43:30 - 4:45:50",
    "Hildegard Förster-Heldmann: 4:50:16 - 4:56:05. Questions: 4:56:40 - 4:58:25",
    "Anja Zeller: 4:58:49 - 5:04:07. Questions: 5:04:30 - 5:05:50",
    "Daniel May: 5:15:45 - 5:20:07. Questions: 5:20:30 - 5:22:40",
    "Sabine Schwöbel-Lehmann: 5:23:10 - 5:28:45. Questions: 5:29:08 - 5:5:30:43",
]
for line_string in list_of_lines:
    cutAudioClip(line_string)

transcribeAllClips()