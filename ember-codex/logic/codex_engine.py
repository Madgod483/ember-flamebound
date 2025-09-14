# logic/codex_engine.py

class CodexEngine:
    def __init__(self):
        self.entries = []

    def add_entry(self, entry: str):
        """Add a new entry to the Codex."""
        self.entries.append(entry)

    def list_entries(self):
        """Return all entries in the Codex."""
        return self.entries

    def search(self, keyword: str):
        """Search entries for a keyword."""
        return [e for e in self.entries if keyword.lower() in e.lower()]
