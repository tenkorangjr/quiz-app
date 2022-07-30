from tkinter import *
from quiz_brain import QuizBrain
import time
from tkinter import messagebox

BACKGROUND = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.count = True

        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(padx=20, pady=20, bg=BACKGROUND)

        self.timer_label = Label(fg="white", text=f"Time Left: {self.quiz.timer}s", bg=BACKGROUND)
        self.timer_label.grid(row=0, column=0)

        self.score_label = Label(pady=20, fg="white", text=f"Score: {self.quiz.score}", bg=BACKGROUND)
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
        self.count_down()

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
            self.count = False
            messagebox.showinfo(message=f"Thank you for playing :) \n\n Your score was {self.quiz.score}")
        elif self.quiz.still_has_questions():
            self.give_feedback(self.quiz.check_answer(string))
            self.ui_next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.reset_count_down()

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        elif not is_right:
            self.canvas.config(bg="red")

        self.window.update()
        time.sleep(1)
        self.canvas.config(bg="white")
        self.window.update()

    def count_down(self):
        if self.quiz.timer > 0 and self.count:
            for _ in range(5):  # To update the screen every 0.2 seconds
                time.sleep(0.2)
                self.window.update()
            self.quiz.timer -= 1
            self.timer_label.config(text=f"Time Left: {self.quiz.timer}s")
            self.count_down()
        elif self.count:
            self.give_feedback(False)
            self.ui_next_question()
            self.reset_count_down()
        else:
            self.quiz.timer = 0
            self.timer_label.config(text=f"Time Left: {self.quiz.timer}s")

    def reset_count_down(self):
        self.quiz.timer = 15
        self.timer_label.config(text=f"Time Left: {self.quiz.timer}s")
        self.window.update()
        self.count_down()

