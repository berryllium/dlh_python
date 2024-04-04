class Question:
    def __init__(self, question_id, question_text) -> None:
        self.question_id = question_id
        self.question_text = question_text
        self.options = []

    def __str__(self):
        return f"Question ID: {self.question_id}, Text: {self.question_text}"