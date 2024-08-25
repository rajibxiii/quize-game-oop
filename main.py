from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

questionBank = []
for q in question_data:
    ques = q["text"]
    ans = q["answer"]
    new_question = Question (ques, ans)
    questionBank.append(new_question)

quiz_br = QuizBrain(questionBank)

while quiz_br.still_has_question():
    quiz_br.next_question()