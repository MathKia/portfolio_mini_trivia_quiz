from tkinter import *
from quiz_brain import QuizBrain  # Import the QuizBrain class
import os
import sys

THEME_COLOR = "#375362"


def resource_path(relative_path):
    """ Get the absolute path to bundled resources (works for both script & .exe) """
    if getattr(sys, 'frozen', False):  # Running as a PyInstaller executable
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # Create window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Create score label
        self.score_label = Label(
            text=f"Score: {self.quiz.score}",
            bg=THEME_COLOR,
            fg="white",
            font=("Arial", 15, "bold")
        )
        self.score_label.grid(row=0, column=1)

        # Create canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125,
            text="fact",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"),
            width=280
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Load images with resource_path
        self.true_img = PhotoImage(file=resource_path("images/true.png"))
        self.false_img = PhotoImage(file=resource_path("images/false.png"))

        # Create buttons
        self.true_btn = Button(image=self.true_img, highlightthickness=0, command=self.true_pressed)
        self.true_btn.grid(row=2, column=0)

        self.false_btn = Button(image=self.false_img, highlightthickness=0, command=self.false_pressed)
        self.false_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        """Fetch and display the next question"""
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")
            self.canvas.config(bg="white")
            self.canvas.itemconfig(
                self.question_text,
                text=f"Your final score was: {self.quiz.score}/{self.quiz.question_number}"
            )

    def true_pressed(self):
        """Handles True button press"""
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        """Handles False button press"""
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_correct):
        """Change canvas color based on correctness and updates score"""
        if is_correct:
            self.canvas.config(bg="Green")
        else:
            self.canvas.config(bg="Red")

        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.window.after(1000, self.get_next_question)








