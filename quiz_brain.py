from question_model import Question

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.q_listLength = len (q_list)
        self.score = 0

    def still_has_question (self):
        return self.question_number < self.q_listLength

    def next_question (self):
        item = self.question_list[self.question_number]
        self.question_number+=1
        choice = input (f"Q.{self.question_number}: {item.text} (True/False): ")
        self.check_answer(choice, item.answer)

    def check_answer (self, userChoice, correctChoice):
        if userChoice.lower() == correctChoice.lower():
            self.score += 1
            print ("Correct!")
        else:
            print ("Incorrect.")
            print (f"The correct answer is: {correctChoice}")
        
        print (f"Your current score is: {self.score}/{self.question_number}\n")