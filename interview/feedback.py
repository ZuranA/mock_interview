class FeedbackEngine:
    def __init__(self, transcript, tone_data):
        self.transcript = transcript
        self.tone_data = tone_data

    def evaluate(self):
        return {
            "clarity_score": self._clarity_score(),
            "tone_insights": self._interpret_tone()
        }

    def _interpret_tone(self):
        f = self.tone_data
        insights = {}

        # Confidence
        if f["avg_volume_db"] < -35:
            insights["confidence"] = "Your voice was too quiet, which can reduce clarity or perceived confidence."
        elif f["jitter_local"] > 0.01 or f["shimmer_local"] > 0.04:
            insights["confidence"] = "Your voice showed instability (jitter/shimmer), which may indicate nervousness."
        else:
            insights["confidence"] = "Your voice was steady and clear — suggesting good confidence."

        # Engagement
        if f["pitch_std_dev"] < 15:
            insights["engagement"] = "Your tone was quite flat. Try varying your pitch to sound more engaging."
        elif f["pitch_std_dev"] < 40:
            insights["engagement"] = "Moderate pitch variation — a good level of expressiveness."
        else:
            insights["engagement"] = "Very expressive tone — energetic, but be cautious of sounding overly emotional."

        # Fluency
        if f["pause_count"] >= 6:
            insights["fluency"] = "There were many pauses, which can suggest hesitation or thinking under pressure."
        elif f["pause_count"] <= 2:
            insights["fluency"] = "Fluent delivery with minimal pausing — well done."
        else:
            insights["fluency"] = "Some pausing detected — reasonable for natural delivery."

        # Pitch Level
        if f["mean_pitch_hz"] < 100:
            insights["tone"] = "Your pitch was low — can sound calm, but may come off as disengaged."
        elif f["mean_pitch_hz"] > 250:
            insights["tone"] = "Your pitch was high — can suggest enthusiasm or anxiety depending on delivery."
        else:
            insights["tone"] = "Your pitch was within a typical speaking range."

        return insights
