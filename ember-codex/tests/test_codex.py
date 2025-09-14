from logic.codex_engine import CodexEngine

def run_tests():
    codex = CodexEngine()
    codex.add_entry("The flame remembers everything.")
    codex.add_entry("Caelen’s journey is written in the Codex.")

    print("All entries:", codex.list_entries())
    print("Search for 'flame':", codex.search("flame"))
    print("Search for 'Caelen':", codex.search("Caelen"))

if __name__ == "__main__":
    run_tests()
