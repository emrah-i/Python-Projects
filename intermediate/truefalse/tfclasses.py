from questions import questions 

class Question:

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        
class Quiz:

    def __init__(self):
        self.score = 0
        self.total = 0

    def get_questions(self):

        question_bank = []
        for q in questions:
            question_bank.append(Question(q['text'], q['answer']))
        return question_bank
        
    def ask(self):

        question_bank = self.get_questions()
        for q in question_bank:
            self.total += 1
            print(f"Question {self.total}:", q.question)

            answer = input("Answer (either 'true' or 'false'): ").capitalize().strip()

            while answer not in ['True', 'False']:
                answer = input("Answer (either 'true' or 'false'): ").capitalize().strip()

            if answer == "False":
                answer = False 
            else: 
                answer = True
    
            if answer == q.answer:
                self.score += 1
                print(f'You got it right!\nThe correct answer was: {q.answer}\nYour current score is: {self.score}/{self.total}\n')
            else:
                print(f'That is wrong.\nThe correct answer was: {q.answer}\nYour current score is: {self.score}/{self.total}\n')
        
        if self.total == 24:
            print(f"You've completed the quiz.\nYour score is {self.score}/{self.total}")