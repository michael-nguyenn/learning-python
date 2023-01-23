class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        cur_question = self.question_list[self.question_number]
        self.question_number += 1
        valid_input = False
        user_answer = ""

        while not valid_input:
            user_answer = input(f"Q.{self.question_number}: {cur_question.question}"
                                f" (True/False)?: ").lower()

            if user_answer == 'true' or user_answer == 'false':
                valid_input = True
            else:
                print("PLEASE PUT IN A CORRECT INPUT 😡")
                print("---------------------------------")

        self.check_answer(user_answer, cur_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
