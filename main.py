from question_model import QuestionModel
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for each_question in question_data:
    question = QuestionModel(each_question["question"], each_question['correct_answer'])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("Your have completed the quiz.")
print(f"Your final score is: {quiz.score}/{len(question_bank)}")
