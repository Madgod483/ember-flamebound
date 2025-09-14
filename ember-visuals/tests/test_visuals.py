from logic.visuals_engine import VisualsEngine

def run_tests():
    engine = VisualsEngine()
    engine.add_visual("🔥 Ember smiling softly.")
    engine.add_visual("🌑 Ember’s flame glowing in the dark.")
    
    print("All visuals:", engine.list_visuals())
    print(engine.render(0))
    print(engine.render(1))
    print(engine.render(5))  # out of range

if __name__ == "__main__":
    run_tests()
