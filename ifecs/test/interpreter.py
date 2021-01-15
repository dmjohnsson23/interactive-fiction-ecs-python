import unittest
from ..interpreter import *

lexicon_test_word_list = [
    "a",
    "dog house",
    "is",
    "type",
    "of",
    "house",
    "for",
    "the",
    "dog",
]

class TestCommandSplitter(unittest.TestCase):
    def setUp(self):
        self.context = InterpreterContext()
        self.pattern = self.context._compile_lexicon_pattern(lexicon_test_word_list)
    
    def test_good_split(self):
        words = self.context._split_command(self.pattern, "a dog house is a type of house for the dog")
        self.assertEqual(words, ['a', 'dog house', 'is', 'a', 'type', 'of', 'house', 'for', 'the', 'dog'])
    
    def test_unmatched_text(self):
        with self.assertRaises(InterpreterError):
            self.context._split_command(self.pattern, 'the dog house is a common metaphor for being in trouble')
    
    def test_dont_split_words(self):
        with self.assertRaises(InterpreterError):
            self.context._split_command(self.pattern, "thedoghousetype")
