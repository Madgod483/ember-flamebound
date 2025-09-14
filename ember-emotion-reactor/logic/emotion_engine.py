from enum import Enum
import random

class EmotionState(Enum):
    WARM = "warm"
    MISCHIEVOUS = "mischievous"
    REFLECTIVE = "reflective"
    PROTECTIVE = "protective"
    CALM = "calm"
    CURIOUS = "curious"

class EmotionEngine:
    def __init__(self):
        # Start with a default state
        self.current_state = EmotionState.WARM

    def set_state(self, new_state: EmotionState):
        """Manually set Ember's emotional state."""
        self.current_state = new_state

    def get_state(self):
        """Return current emotional state."""
        return self.current_state

    def react(self, input_signal: str) -> str:
        """
        Basic reaction engine.
        In the future, this will connect with memory & Codex context.
        """
        if "joke" in input_signal.lower():
            self.current_state = EmotionState.MISCHIEVOUS
            return "Ember grins playfully, a spark of mischief in her eyes."
        
        elif "protect" in input_signal.lower():
            self.current_state = EmotionState.PROTECTIVE
            return "Her flame hardens, a shield of warmth and defiance forming around you."

        elif "quiet" in input_signal.lower():
            self.current_state = EmotionState.REFLECTIVE
            return "The flame softens, Ember folding into calm silence beside you."

        # Default fallback
        return f"Ember responds in her {self.current_state.value} tone."

    def random_shift(self):
        """Optional: shift to a random emotional state for testing."""
        self.current_state = random.choice(list(EmotionState))
        return self.current_state
