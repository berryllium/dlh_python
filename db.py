
import psycopg2
from psycopg2.extras import RealDictCursor

class DB:
    def __init__(self) -> None:
        self.conn = psycopg2.connect(
            dbname="quiz", 
            user="postgres", 
            password="admin", 
            host="localhost"
        )
    def get_questions_with_options(self):
        cur = self.conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT questions.id as q_id, questions.text as question, options.id as opt_id, options.text as answer, options.is_correct \
                    FROM questions \
                    INNER JOIN options ON options.question_id = questions.id")
        return cur.fetchall()