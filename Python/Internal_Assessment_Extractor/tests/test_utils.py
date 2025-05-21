"""
test_utils.py

Unit tests for utility functions used in parser.py.
Specifically tests extract_question_answer logic for handling
correctly and incorrectly formatted input strings.
"""

import unittest
from src.parser import extract_question_answer

class TestExtractQuestionAnswer(unittest.TestCase):
    """
    Unit test case for the extract_question_answer function.
    """

    def test_valid_question_answer(self):
        """
        Test a properly formatted question and answer.
        """
        text = "CONCEPT CHECK\nASK participants: What is the capital of France? ANSWER: Paris"
        expected_question = "What is the capital of France?"
        expected_answer = "Paris"
        question, answer = extract_question_answer(text)
        self.assertEqual(question, expected_question)
        self.assertEqual(answer, expected_answer)

    def test_missing_answer(self):
        """
        Test when the 'ANSWER:' label is missing.
        """
        text = "ASK participants: What is the capital of France?"
        question, answer = extract_question_answer(text)
        self.assertIsNone(question)
        self.assertIsNone(answer)

    def test_missing_question(self):
        """
        Test when the 'ASK participants:' label is missing.
        """
        text = "ANSWER: Paris"
        question, answer = extract_question_answer(text)
        self.assertIsNone(question)
        self.assertIsNone(answer)

    def test_malformed_text(self):
        """
        Test with a completely malformed string.
        """
        text = "This is just random text without expected format."
        question, answer = extract_question_answer(text)
        self.assertIsNone(question)
        self.assertIsNone(answer)

    def test_question_answer_with_extra_spaces(self):
        """
        Test with extra spaces and newlines around text.
        """
        text = "ASK participants:   What is 2 + 2?   \nANSWER:  4  "
        expected_question = "What is 2 + 2?"
        expected_answer = "4"
        question, answer = extract_question_answer(text)
        self.assertEqual(question, expected_question)
        self.assertEqual(answer, expected_answer)

    def test_question_answer_multiline(self):
        """
        Test multi-line question and answer.
        """
        text = "ASK participants: What are the benefits of\nusing automation?\nANSWER: Improved speed and reduced errors."
        expected_question = "What are the benefits of\nusing automation?"
        expected_answer = "Improved speed and reduced errors."
        question, answer = extract_question_answer(text)
        self.assertEqual(question, expected_question)
        self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
