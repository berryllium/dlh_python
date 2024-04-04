from button import Button
from header import Header
from question import Question
from option import Option
from db import DB


class Game:

    def __init__(self, grid):
        self.grid = grid

    def init(self):
        self.grid.addWidget(Header("Welcome to the quiz. Click the button to start!"), 0, 0)

        self.questions = {}
        self.current_question = None
        self.total_count = self.score = 0    

        button = Button("Play")
        button.clicked.connect(self.start_game)
        self.grid.addWidget(button, 1, 0)    

    def question_page(self):
        self.clear_widgets()

        if(len(self.questions)):
            self.current_question = self.questions.popitem()[1]
        else:
            self.show_result()
            return
        
        self.grid.addWidget(Header(self.current_question.question_text), 0, 0, 1, 2)

        for i, option in enumerate(self.current_question.options):
            row = i // 2 + 1
            col = i % 2
            button = Button(option.option_text)
            button.clicked.connect(lambda check, option=option: self.handle_click(option))
            self.grid.addWidget(button, row, col)
    

    def start_game(self):
        db = DB()
        data = db.get_questions_with_options()

        for row in data:
            if row['q_id'] not in self.questions:
                self.questions[row['q_id']] = Question(row['q_id'], row['question'])
            self.questions[row['q_id']].options.append(Option(row['opt_id'], row['answer'], row['is_correct']))
        self.total_count = len(self.questions)
        self.score = 0
        self.clear_widgets()
        print("The Game started")
        self.question_page()

    def clear_widgets(self):
        for i in reversed(range(self.grid.count())): 
            self.grid.itemAt(i).widget().setParent(None)
       
    def handle_click(self, opt):
        if(opt.is_correct):
            self.score += 1
        self.question_page()

    def show_result(self):
        self.clear_widgets()
        self.grid.addWidget(Header(f"Quiz completed! Your score is {self.score}/{self.total_count}."))