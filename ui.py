from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(pady=20, fg="white", text=f"Score: {self.quiz.score}", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question = self.canvas.create_text(
            150,
            125,
            width=280,
            text="INPUT ANY QUESTION HERE",
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        self.cross_image = PhotoImage(file="./images/false.png")
        self.cross_button = Button(image=self.cross_image, highlightthickness=0, command=self.answer_false)
        self.cross_button.grid(column=1, row=2, pady=20)
        self.correct_image = PhotoImage(file="./images/true.png")
        self.correct_button = Button(image=self.correct_image, highlightthickness=0, command=self.answer_true)
        self.correct_button.grid(column=0, row=2, pady=20)

        self.ui_next_question()

        self.window.mainloop()

    def ui_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question, text=q_text)

    def answer_true(self):
        self.check_answer("True")

    def answer_false(self):
        self.check_answer("False")

    def check_answer(self, string):
        if self.quiz.question_number == 10:
            self.give_feedback(self.quiz.check_answer(string))
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question, text="You've reached the maximum number of questions")
            self.cross_button.config(state="disabled")
            self.correct_button.config(state="disabled")
        elif self.quiz.still_has_questions():
            self.give_feedback(self.quiz.check_answer(string))
            self.ui_next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}")

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        elif not is_right:
            self.canvas.config(bg="red")

        self.window.update()
        time.sleep(1)
        self.canvas.config(bg="white")
        self.window.update()


