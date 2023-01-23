from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Need to iterate over our list of dictionaries, and create a Question
#   object for each entry in question_data
# Append each Question object to the question_bank

question_bank = []

for i in range(len(question_data)):
    question = question_data[i]['question']
    answer = question_data[i]['correct_answer']
    question_bank.append(Question(question, answer))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz 🎉")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
