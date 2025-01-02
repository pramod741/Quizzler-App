import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_question: QuizBrain):
        self.question = quiz_question
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = tkinter.Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canves = tkinter.Canvas(height=250, width=300, bg="white")
        self.question_text = self.canves.create_text(
            150,
            125,
            width=280,
            text="some thing",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canves.grid(column=0, row=1, columnspan=2, pady=50)

        image1 = tkinter.PhotoImage(file="images/false.png")
        image2 = tkinter.PhotoImage(file="images/true.png")

        self.false_button = tkinter.Button(image=image1, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=0, row=2)

        self.true_button = tkinter.Button(image=image2, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=1, row=2)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canves.config(bg="white")
        if self.question.still_has_questions():
            self.score_label.config(text=f"Score: {self.question.score}")
            q_text = self.question.next_question()
            self.canves.itemconfig(self.question_text, text=q_text)
        else:
            self.canves.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.question.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.question.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canves.config(bg="green")
        else:
            self.canves.config(bg="red")
        self.window.after(1000, self.next_question)
