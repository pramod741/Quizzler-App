from question_model import Question
from quiz_brain import QuizBrain
from data import question_data
from ui import QuizInterface


question_bank = []
for questions in question_data:
    question_text = questions['question']
    question_answer = questions['correct_answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
ui = QuizInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

# print("You've completed the quiz")
# print(f"Your final score was: {quiz.score}/{quiz.question_number}")
