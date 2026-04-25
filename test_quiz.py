import unittest
from question import MultipleChoiceQuestion, TrueFalseQuestion


class TestQuiz(unittest.TestCase):

    def test_mc_question(self):
        q = MultipleChoiceQuestion("2+2?", ["2", "3", "4"], "4")
        self.assertTrue(q.check_answer("3"))
        self.assertFalse(q.check_answer("1"))

    def test_tf_question(self):
        q = TrueFalseQuestion("Python?", "True")
        self.assertTrue(q.check_answer("True"))
        self.assertFalse(q.check_answer("False"))


if __name__ == "__main__":
    unittest.main()