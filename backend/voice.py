import os
import uuid

from gtts import gTTS


def generate_voice(text, language):
    os.makedirs("audio", exist_ok=True)

    filename = f"{uuid.uuid4()}.mp3"
    filepath = f"audio/{filename}"

    tts = gTTS(text=text, lang=language, slow=True)

    tts.save(filepath)

    return filename
