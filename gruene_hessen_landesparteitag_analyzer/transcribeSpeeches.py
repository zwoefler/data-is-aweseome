import sys
import os
import whisper
import torch
import json

def cutAudio(info, audioFile):
    os.system(f"ffmpeg -i {sourceAudio} -ss {info['beginSpeech']} -to {info['endSpeech']} -c copy {audioFile}")
    return


def createExportName(info):
    """Returns the export name based on speaker name"""
    export_name = info["name"].strip().lower().replace(" ", "_")
    if info["reminder"]:
        return "reminder_" + export_name

    return export_name


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


# Calculate speech length
# Transcribe Questions



torch.cuda.is_available()
if torch.cuda.is_available():
    print("CUDA")
    DEVICE = "cuda"
else:
    print("CPU")
    DEVICE = "cpu"

folder = "speeches/"
sourceAudio = "landesparteitag-am-25.und-26.februar-2023-ta.mp3"

with open(sys.argv[1], "r") as f:
    speech_info_list = json.load(f)

for info in speech_info_list:
    if "youtube_id" in info:
        continue
    export_name = createExportName(info)
    audioFile = os.path.join(folder, export_name + ".mp3")
    print("Working on:", audioFile)
    if info["question"]:
        questionAudioFile = os.path.join(folder, "question_" + export_name + ".mp3")
        if not os.path.isfile(questionAudioFile):
            cutAudio(info, questionAudioFile)
            transcribeFile(questionAudioFile, info)

    if not os.path.isfile(audioFile):
        cutAudio(info, audioFile)
    transcribeFile(audioFile, info)
    print()