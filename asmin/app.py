from flask import Flask, render_template, request, jsonify
from backend import listen_and_save, speech_to_text, chat_completion, text_to_speech

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_audio', methods=['POST'])
def process_audio():
    # Save the audio file sent from the frontend
    audio_file = request.files['audio'].save('temp_audio.wav')

    # Pass the path of the saved audio file to the backend
    response_text = speech_to_text('temp_audio.wav')

    # Perform further processing and return the response
    if 'exit the bot' in response_text:
        return jsonify({'response': 'Exiting...'})
    if 'Exit the bot' in response_text:
        return jsonify({'response': 'Exiting...'})
    answer = chat_completion(response_text)
    response_voice = text_to_speech(answer)
    return jsonify({'response_text': response_text, 'response_voice': response_voice})

if __name__ == '__main__':
    app.run(debug=True)
