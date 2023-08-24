import unittest
from main_program import PlayHangMan

class TestPlayHangMan(unittest.TestCase):
    def test_whole_word_guessed(self):
        word_guesser = PlayHangMan("Vladas", "apple")
        word_guesser.guessed_letters_list = ["a", "p", "l", "e"]
        # Test the function
        result = word_guesser.check_if_whole_word_guessed()
        # Check the result
        self.assertTrue(result)

    def test_not_whole_word_guessed(self):
        word_guesser = PlayHangMan("Lady", "banana")
        word_guesser.guessed_letters_list = ["b", "q", "n"]
        # Test the function
        result = word_guesser.check_if_whole_word_guessed()
        # Check the result
        self.assertFalse(result)




if __name__ == '__main__':
    unittest.main()