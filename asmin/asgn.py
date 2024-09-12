import requests
import uuid
import os
from openai import OpenAI
from pydub.playback import play
from pydub import AudioSegment

client = OpenAI()


def speech_to_text(audio_file):
    audio_file = open(audio_file, "rb")
    # prompt param is optional
    transcription = client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file, 
        response_format="text",
    )
    return transcription

def text_to_speech(text):
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text,
    )
    pk = uuid.uuid4().hex
    file_name = f"output_{pk}.mp3"
    response.stream_to_file(file_name)
    full_path = os.path.join(os.getcwd(), file_name)
    print("Saved to text to voice", full_path) 
    return full_path

def chat_completion(prompt):
    stream = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}, {"role": "assistant", "content": 'You are a helpful assistant.'}]
    )
    print(stream)
    print(stream.choices[0].message.content)
    return stream.choices[0].message.content

# step 1
# source - audio - write to disk
# next step - send audio  to whisper-1
# next step - chat completion - gpt - stream
# next step - post process text - gpt - qa
# next step - save response voice to disk - tts-1
# next step - play the file from the disk - read-it

import speech_recognition as sr

def listen_and_save():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    pk = uuid.uuid4().hex
    filename = f"input_{pk}.wav"
    with open(filename, "wb") as f:
        f.write(audio.get_wav_data())
    full_path = os.path.join(os.getcwd(), filename)
    print("Saved to", full_path)  # this will pri
    # print the current path of the file
    return full_path


if __name__ == "__main__":
    while True:
        full_path = listen_and_save()
        response_text = speech_to_text(full_path)
        if 'exit the bot' in response_text:
            print("Exiting....'")
            break
        if 'Exit the bot' in response_text:
            print("Exiting....'")
            break
        answer = chat_completion(response_text)
        response_voice = text_to_speech(answer)
        print("Server response:", response_text)
        print("Server response voice full path", response_voice)
        print("full path of wav", full_path)
        voice = AudioSegment.from_mp3(response_voice)
        play(voice)
        print("Server response:", response_text)
