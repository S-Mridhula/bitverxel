import streamlit as st
import os
import wave
import json
import sounddevice as sd
from vosk import Model, KaldiRecognizer

# Path to Vosk model directory
vosk_model_path = r"C:\Users\SUSMITA.N\Downloads\vs code\vosk-model"

# Initialize the recognizer
if not os.path.exists(vosk_model_path):
    st.error(f"Model not found at {vosk_model_path}. Please download a model from https://alphacephei.com/vosk/models and extract it.")
else:
    model = Model(vosk_model_path)

# Function to capture audio and recognize speech
def recognize_speech():
    sample_rate = 16000  # Sample rate for Vosk
    duration = 5  # Record audio for 5 seconds
    
    st.write("Listening...")

    # Record audio for a fixed duration
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype="int16")
    sd.wait()  # Wait for the recording to finish
    
    # Initialize recognizer with the sample rate and model
    recognizer = KaldiRecognizer(model, sample_rate)
    recognizer.AcceptWaveform(audio_data.tobytes())
    result = json.loads(recognizer.FinalResult())

    if 'text' in result:
        recognized_word = result['text']
        return recognized_word
    return None

# Dictionary mapping recognized words to video/image paths
media_directory = r"C:/Users/SUSMITA.N/OneDrive/Desktop/videos"
media_dict = {
    "hello": os.path.join(media_directory, "hello.mp4"),    
    "thank you": os.path.join(media_directory,"thankyou.mp4"),
    "friend": os.path.join(media_directory,"friends.mp4"),
    "five":os.path.join(media_directory,"five.jpg" ),
}

# Streamlit app layout
st.title("Speech to Sign Language Converter")
st.write("This app listens to your voice and shows the corresponding sign language video or image.")

# Button to trigger speech recognition
if st.button("Start Listening"):
    recognized_word = recognize_speech()

    if recognized_word:
        st.write(f"Recognized word: {recognized_word}")

        # Display corresponding media
        if recognized_word in media_dict:
            file_path = media_dict[recognized_word]
            if file_path.endswith(".mp4"):
                st.video(file_path)
            elif file_path.endswith(".jpg"):
                st.image(file_path)
        else:
            st.write("No video or image found for the recognized word.")
    else:
        st.write("Could not recognize any word.")
