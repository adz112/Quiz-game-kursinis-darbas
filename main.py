import csv
from quiz import Quiz
from factory import QuestionFactory
from player import Player
from score_manager import ScoreManager


def load_questions(filename):
    quiz = Quiz()

    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            question = QuestionFactory.create_question(
                row['type'],
                row['question'],
                row['options'],
                row['answer']
            )
            quiz.add_question(question)

    return quiz


def main():
    name = input("Enter your name: ")
    player = Player(name)

    quiz = load_questions("questions.csv")
    quiz.start()

    score = quiz.get_score()
    player.set_score(score)

    print(f"{name}, your score is {score}")

    manager = ScoreManager("scores.txt")
    manager.save_score(player)
    manager.show_scores()


if __name__ == "__main__":
    main()