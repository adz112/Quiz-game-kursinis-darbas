import random


class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0

    def add_question(self, question):
        self.questions.append(question)

    def start(self):
        random.shuffle(self.questions)

        for question in self.questions:
            question.display()
            answer = input("Your answer: ")

            if question.check_answer(answer):
                print("Correct!\n")
                self.score += 1
            else:
                print("Wrong!\n")

    def get_score(self):
        return self.score