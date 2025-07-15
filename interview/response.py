from interview.transcriber import Transcriber
from interview.analyzer import AudioAnalyzer
from interview.feedback import FeedbackEngine

class AudioResponse:
    def __init__(self, file_path):
        self.transcript = Transcriber(file_path).transcribe()
        self.tone_data = AudioAnalyzer(file_path).analyze()
        self.feedback = FeedbackEngine(self.transcript, self.tone_data).evaluate()
