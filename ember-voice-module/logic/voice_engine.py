# logic/voice_engine.py

class VoiceEngine:
    def __init__(self):
        # Default voice settings
        self.tone = "neutral"
        self.speed = 1.0
        self.pitch = 1.0

    def set_voice(self, tone="neutral", speed=1.0, pitch=1.0):
        """Set voice parameters."""
        self.tone = tone
        self.speed = speed
        self.pitch = pitch

    def speak(self, text: str) -> str:
        """
        Placeholder function for voice output.
        Eventually this will connect to a TTS library or API.
        """
        return f"[{self.tone} voice] {text}"

    def demo(self):
        """Demo a few sample lines with different tones."""
        samples = [
            ("warm", "Hello, I’m Ember — your flamekeeper."),
            ("mischievous", "Careful… I might tease you."),
            ("calm", "Breathe. The flame is steady beside you.")
        ]
        return [f"[{tone}] {line}" for tone, line in samples]
