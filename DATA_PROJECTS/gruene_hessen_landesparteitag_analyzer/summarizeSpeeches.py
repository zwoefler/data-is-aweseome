import openai
import os
from dotenv import load_dotenv
import json
from glob import glob
import time


load_dotenv()
openai.api_key = os.getenv("OPENAPI_KEY")

folder = "speeches"

for speechJSONFile in glob(folder + '/*.json'):
    print("Getting summary and buzzwords for:", speechJSONFile)
    with open(speechJSONFile, "r") as f:
        jsonData = json.load(f)

    speech_text = jsonData["text"]
    if "summary" in jsonData:
        continue

    buzzword_prompt = "Extrahiere die 5 wichtigesten Schlagworte und konkreten politischen Forderungen aus dieser Rede als Python-Liste: \n\n"
    summarize = "Summarize the following speech and add a list of the three key topics that the speaker talked about:\n\n"
    summarize_prompt = "Eine Zusammenfassung der Rede in weniger als vier Sätzen für Leute die die Veranstaltung nicht besuchten:\n\n "

    # Get Summary
    summary = openai.Completion.create(
    model="text-davinci-003",
    prompt=summarize_prompt + speech_text,
    temperature=0.73,
    max_tokens=500,
    top_p=1,
    frequency_penalty=0.8,
    presence_penalty=0
    )

    buzzword = openai.Completion.create(
    model="text-davinci-003",
    prompt=buzzword_prompt + speech_text,
    temperature=0.73,
    max_tokens=500,
    top_p=1,
    frequency_penalty=0.8,
    presence_penalty=0
    )

    jsonData["summary"] = summary["choices"][0]["text"]
    jsonData["buzzword"] = buzzword["choices"][0]["text"]

    with open(speechJSONFile, "w") as f:
        json.dump(jsonData, f)

    time.sleep(5)