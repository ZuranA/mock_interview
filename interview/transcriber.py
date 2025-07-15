import openai
import os 
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")  

class Transcriber:
    def __init__(self, file_path):
        self.file_path = file_path

    def transcribe(self):
        with open(self.file_path, "rb") as audio_file:
            transcript = openai.Audio.transcribe(
                model="whisper-1",
                file=audio_file,
                response_format="text"
            )
        return transcript.strip()
