from abc import ABC, abstractmethod


class Question(ABC):
    def __init__(self, text, answer):
        self._text = text
        self._answer = answer

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def check_answer(self, user_answer):
        pass


class MultipleChoiceQuestion(Question):
    def __init__(self, text, options, answer):
        super().__init__(text, answer)
        self._options = options

    def display(self):
        print("\n" + self._text)
        for i, option in enumerate(self._options, 1):
            print(f"{i}. {option}")

    def check_answer(self, user_answer):
        try:
            return self._options[int(user_answer) - 1].lower() == self._answer.lower()
        except (ValueError, IndexError):
            return False


class TrueFalseQuestion(Question):
    def display(self):
        print(f"\n{self._text} (True/False)")

    def check_answer(self, user_answer):
        return user_answer.strip().lower() == self._answer.lower()