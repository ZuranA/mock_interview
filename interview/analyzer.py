import librosa
import numpy as np
import parselmouth

class AudioAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.y, self.sr = librosa.load(file_path)
        self.sound = parselmouth.Sound(file_path)

    def analyse(self):
        # return a single dict
        return {
            **self._basic_features(),
            **self._parselmouth_features()
        }

    def _basic_features(self):
        duration = librosa.get_duration(y=self.y, sr=self.sr)
        rms = np.sqrt(np.mean(self.y**2))
        db = 20 * np.log10(rms) if rms > 0 else -100
        pause_count = self._count_pauses()

        return {
            "duration_sec": round(duration, 2),
            "avg_volume_db": round(db, 2),
            "pause_count": pause_count,
        }

    def _count_pauses(self, threshold_db=-35.0, min_pause_sec=0.3):
        intervals = librosa.effects.split(self.y, top_db=abs(threshold_db))
        total_audio = sum((e - s) for s, e in intervals)
        silence_time = len(self.y) - total_audio
        pause_estimate = silence_time / (self.sr * min_pause_sec)
        return int(pause_estimate)
    
    def _parselmouth_features(self):
        pitch = self.sound.to_pitch()
        mean_pitch = pitch.get_mean()
        stdev_pitch = pitch.get_standard_deviation()

        point_process = self.sound.to_point_process_cc()
        jitter = parselmouth.praat.call(point_process, "Get jitter (local)", 0, 0, 0.0001, 0.02, 1.3)
        shimmer = parselmouth.praat.call([self.sound, point_process], "Get shimmer (local)", 0, 0, 0.0001, 0.02, 1.3, 1.6)

        return {
            "mean_pitch_hz": round(mean_pitch, 2),
            "pitch_std_dev": round(stdev_pitch, 2),
            "jitter_local": round(jitter, 4),
            "shimmer_local": round(shimmer, 4),
        }