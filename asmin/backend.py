from openai import OpenAI

# sk-proj-w5KqP5UOe75eT1HsX9QTT3BlbkFJF6uQX4muMR9Abt78IQj5
client = OpenAI()

audio_file = open("/path/to/file/speech.mp3", "rb")

transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file, 
  response_format="text",
  prompt="ZyntriQix, Digique Plus, CynapseFive, VortiQore V8, EchoNix Array, OrbitalLink Seven, DigiFractal Matrix, PULSE, RAPT, B.R.I.C.K., Q.U.A.R.T.Z., F.L.I.N.T."
)

print(transcription.text)



from openai import OpenAI

client = OpenAI()

response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input="Hello world! This is a streaming test.",
)

response.stream_to_file("output.mp3")

def speech_to_text(audio_file):
    # transcription
    return transcription.text
def post_process_text(text):
    return text
def text_to_speech(text):
    return text

