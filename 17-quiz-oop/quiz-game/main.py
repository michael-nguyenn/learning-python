from question_model import Question
from data import question_data

# Need to iterate over our list of dictionaries, and create a Question
#   object for each entry in question_data
# Append each Question object to the question_bank

question_bank = []

for i in range(len(question_data)):
    question = question_data[i]['text']
    answer = question_data[i]['answer']
    question_bank.append(Question(question, answer))
