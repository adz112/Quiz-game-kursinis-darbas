from question import MultipleChoiceQuestion, TrueFalseQuestion


class QuestionFactory:
    @staticmethod
    def create_question(q_type, text, options, answer):
        if q_type == "mc":
            return MultipleChoiceQuestion(text, options.split("|"), answer)
        elif q_type == "tf":
            return TrueFalseQuestion(text, answer)
        else:
            raise ValueError("Unknown question type")