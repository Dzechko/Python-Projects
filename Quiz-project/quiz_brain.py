# asking the questions
# checking if the answer was correct
# checking if were the end of the quiz

class QuizBrain:
    def __init__(self, q_list):
        self.question_no = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_no < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        ans = input(f"Q.{self.question_no} : {current_question.text} (True/False) ")
        self.check_answer(ans,current_question.answer)

    def check_answer(self, user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right")
            self.score += 1
            print(f"Your current score is: {self.score}/{self.question_no}")
        else:
            print("That's wrong")
        print(f"The correct answer is : {correct_answer}.")

    def is_finished(self):
        if self.question_no >= len(self.question_list):
            print("You've completed the quiz")
            print(f"Your final score was {self.score}/{len(self.question_list)}")


