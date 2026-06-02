from gtts import gTTS


def text_to_speech(text, output_file="output.mp3"):
    """
    Convert text to speech and save it as an MP3 file.

    Args:
        text (str): Text to convert into speech.
        output_file (str): Name of the output audio file.

    Returns:
        str: Path to the generated audio file.
    """
    tts = gTTS(text=text, lang="en")
    tts.save(output_file)

    return output_file


if __name__ == "__main__":
    sample_text = "Hello, this is SeniorSaathi."

    file_path = text_to_speech(sample_text)

    print(f"Audio file created: {file_path}")
