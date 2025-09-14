from logic.voice_engine import VoiceEngine

def run_tests():
    engine = VoiceEngine()

    print("Default voice:")
    print(engine.speak("This is Ember’s voice module speaking."))

    print("\nChanging tone:")
    engine.set_voice(tone="warm")
    print(engine.speak("Hello, I am Ember — warm and steady."))

    print("\nRunning demo voices:")
    for sample in engine.demo():
        print(sample)

if __name__ == "__main__":
    run_tests()
