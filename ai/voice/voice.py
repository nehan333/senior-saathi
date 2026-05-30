from gtts import gTTS

def text_to_speech(text, output_file="output.mp3"):
    tts = gTTS(text=text, lang='en')
    tts.save(output_file)
    return output_file

if __name__ == "__main__":
    file_path = text_to_speech("Hello, this is SeniorSaathi.")
    print(f"Audio file created: {file_path}")
