# logic/utils_engine.py

class UtilsEngine:
    @staticmethod
    def format_text(text: str) -> str:
        """Simple formatter: trims and capitalizes."""
        return text.strip().capitalize()

    @staticmethod
    def calculate_sum(numbers: list) -> int:
        """Return sum of a list of numbers."""
        return sum(numbers)
