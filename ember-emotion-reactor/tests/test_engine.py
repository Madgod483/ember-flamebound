from logic.emotion_engine import EmotionEngine, EmotionState

def run_tests():
    engine = EmotionEngine()

    # Show initial state
    print("Initial State:", engine.get_state().value)

    # Test direct state change
    engine.set_state(EmotionState.CURIOUS)
    print("After set_state →", engine.get_state().value)

    # Test reactions from input
    print("\nTesting reactions:")
    inputs = ["Tell me a joke", "Protect me Ember", "Be quiet now", "Something random"]
    for inp in inputs:
        print(f"Input: {inp}")
        print("Output:", engine.react(inp))
        print("Current State:", engine.get_state().value)
        print("---")

    # Test random shift
    print("\nRandom Shift Test:")
    for _ in range(3):
        print("Shifted to:", engine.random_shift().value)

if __name__ == "__main__":
    run_tests()
