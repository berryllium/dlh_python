class Option:
    def __init__(self, option_id, option_text, is_correct) -> None:
        self.option_id = option_id
        self.option_text = option_text
        self.is_correct = is_correct

    def __str__(self) -> str:
        correct_text = "Correct" if self.is_correct else "Incorrect"
        return f"Option ID: {self.option_id}, Text: {self.option_text}, {correct_text}"
