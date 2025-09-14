# logic/visuals_engine.py

class VisualsEngine:
    def __init__(self):
        self.visuals = []

    def add_visual(self, visual: str):
        """Add a new visual placeholder (later could be image/animation hooks)."""
        self.visuals.append(visual)

    def list_visuals(self):
        """Return all stored visuals."""
        return self.visuals

    def render(self, index: int):
        """Render a stored visual by index (placeholder for now)."""
        if 0 <= index < len(self.visuals):
            return f"Rendering visual: {self.visuals[index]}"
        return "No visual found at that index."
