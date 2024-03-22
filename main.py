from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


q = []
for i in question_data:
    quest_text = i["question"]
    quest_answer = i["correct_answer"]
    a = Question(quest_text,quest_answer)
    q.append(a)

w = QuizBrain(q)


while w.still_has_question():
    w.next_question()
print("You have completed the quiz!")
print(f"Your total score was: {w.score}/{w.question_number}")