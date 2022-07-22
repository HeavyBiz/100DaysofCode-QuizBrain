class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list


    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return 0
        else:
            return 5
        # Angela's code that I can't get to work
        # return self.question_number < len(self.question_list)






        # this code below works so long as the number of questions is 12, Angela's program is more adaptable.
        # while self.question_number<13:
        #     self.next_question()


    def next_question(self):
        global current_question
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text}. (True/False): ")
        self.check_answer(user_answer, current_question.answer)



        #While quiz has quiestions remaining, keep quiz going.

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {current_question.answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")










#TODO asking questions
#TODO checking if the answer was correct
#TODO: checking if we're at the end of the quiz