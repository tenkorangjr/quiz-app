from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface
import requests

quizzler_data = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
print(quizzler_data.json())
question_data = quizzler_data.json()["results"]

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()
