import logging
import random
from typing import Union


logging.basicConfig(
    level=logging.DEBUG,
    filename="player_data.log",
    filemode="a",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
)


class HangManBase:
    def __init__(self) -> None:
        self.word_list = []

    def select_word_list(self, word_list: str) -> str:
        num_words_processed = 0
        curr_word = None
        word: str = None
        with word_list as f:
            for word in f:
                word = word.strip().upper()
                num_words_processed += 1
                if random.randint(1, num_words_processed) == 1:
                    curr_word = word
        return curr_word
      
    def word_selection(self, selected_list :int) -> str:
        if selected_list == 1:
            self.word_list = open("word_list/countries.txt", 'r')
            selected_word = self.select_word_list(self.word_list)
            return selected_word
        if selected_list == 2:
            self.word_list = open("word_list/animals.txt", 'r')
            selected_word = self.select_word_list(self.word_list)
            return selected_word

    def list_to_string(self, print_guessing_word: list) -> str:
        hidden_word = ""
        for element in print_guessing_word:
            hidden_word += element
        return hidden_word


class PlayHangMan(HangManBase):
    def __init__(self, player_name: str, selected_word: str) -> None:
        self.player_name = player_name
        self.selected_word = list(selected_word)
        self.guessed_letters_list = [" "]
        self.max_guess = 10
        self.bad_guess_count = 0

    def check_unused_letters(self, letter_guessed: str) -> Union[bool, list]:
        if letter_guessed in self.guessed_letters_list:
            return self.guessed_letters_list or False
        else:
            return self.guessed_letters_list.append(letter_guessed) or True

    def show_used_letters(self) -> str:
        return self.list_to_string(self.guessed_letters_list)

    def guessing_word_hide(self, letter_guessed: str) -> str:
        print_guessing_word = []
        for letter_guessed in self.selected_word:
            if letter_guessed in self.guessed_letters_list:
                print_guessing_word.append(letter_guessed)
            else:
                print_guessing_word.append("-")
        return self.list_to_string(print_guessing_word)

    def bad_guess_counter(self) -> bool:
        guess_count = 0
        for letter in self.guessed_letters_list:
            if letter not in self.selected_word:
                guess_count = guess_count + 1
        if guess_count != self.max_guess:
            return True
        else:
            return False
    
    def is_won(self) -> bool:
        counter = 0
        for letter in self.selected_word:
            if letter in self.guessed_letters_list:
                counter += 1
        if counter == len(self.selected_word):
            return True
        else:
            return False
    
    def bad_guess_counter(self) -> int:
        self.bad_guess_count += 1
        return self.bad_guess_count


    def guess_one_letter(self, letter_guessed: str) -> Union[list, int]:
        if letter_guessed.isalpha() and len(letter_guessed) == 1:
            if self.check_unused_letters(letter_guessed) == True:
                if letter_guessed in self.selected_word:
                    if self.is_won() == True:
                        logging.info(
                        f"Player {self.player_name} WINS. "
                        f"Word was: {self.list_to_string(self.selected_word)}. "
                        f"Guessed letters was: {self.list_to_string(self.guessed_letters_list)}"
                    )
                        return 6 # Winner
                    else:
                        return 1 # Guess successfull
                else:
                    
                    if self.bad_guess_counter() == self.max_guess:  # Bad guess counter
                        logging.info(
                            f"Player {self.player_name} LOST. "
                            f"Word was: {self.list_to_string(self.selected_word)}. "
                            f"Guessed letters was: {self.list_to_string(self.guessed_letters_list)}")
                        return 5  # Dont have guess Still have guess                    
                    else:
                        return 2 # Still have guess
            else:
                return 3  # You already used letter
        else:
            return 4  # Not a letter used or user several letters

    def guess_all_word(self, all_word: str) -> int:
        all_word_list = list(all_word)
        if all_word_list == self.selected_word:
            return 1
        elif self.bad_guess_counter() == self.max_guess:
            return 3
        else:
            return 2
