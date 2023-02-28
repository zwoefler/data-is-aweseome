import os
import whisper
import torch
import json

def cutAudio(info, audioFile):
    os.system(f"ffmpeg -i landesparteitag_25.02.22_audio.mp3 -ss {info['beginSpeech']} -to {info['endSpeech']} -c copy {audioFile}")
    return


def createExportName(name):
    """Returns the export name based on speaker name"""
    return name.strip().lower().replace(" ", "_")


def audioToText(audioFile):
    """Transposes Audio File to German Text"""
    model = whisper.load_model("base", device=DEVICE)
    result = model.transcribe(audioFile)

    return result


def transcribeFile(file, info):
    filename, extension = os.path.splitext(file)
    if extension == '.mp3':
        print("Transcribing:", file)
        if os.path.isfile(os.path.join(filename + ".txt")):
            return
        speech = audioToText(os.path.join(filename + ".mp3"))
        speech.update(info)
        with open(os.path.join(filename + ".txt"), "w") as f:
            f.write(speech["text"])
        with open(os.path.join(filename + ".json"), "w") as f:
            json.dump(speech, f)




torch.cuda.is_available()
if torch.cuda.is_available():
    print("CUDA")
    DEVICE = "cuda"
else:
    print("CPU")
    DEVICE = "cpu"

folder = "speeches/"

with open("speeches_info.json", "r") as f:
    speech_info_list = json.load(f)

for info in speech_info_list:
    export_name = createExportName(info["name"])
    audioFile = os.path.join(folder, export_name + ".mp3")
    print("Working on:", audioFile)
    if not os.path.isfile(audioFile):
        cutAudio(info, audioFile)
    transcribeFile(audioFile, info)
    print()