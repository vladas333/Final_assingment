import logging
import os
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
        self.word_lists_folder = "word_lists/"
        self.word_list = []

    # Words list read
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

    def list_available_word_lists(self) -> list:
        word_list_files = [file for file in os.listdir(self.word_lists_folder) if file.endswith(".txt")]
        return word_list_files

    # Word selection
    def word_selection(self, available_word_lists: list, select_word_category: int) -> str:
        if 1 <= select_word_category <= len(available_word_lists):
            selected_file = os.path.join(self.word_lists_folder, available_word_lists[select_word_category - 1])
            with open(selected_file, "r") as word_list_file:
                selected_word = self.select_word_list(word_list_file)
                return selected_word
        else:
            selected_word = "Python"
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
        self.guessed_letters_list = [" ", "-"]
        self.max_guess = 10
        self.bad_guess_count = 0

    def check_unused_letters(self, letter_guessed: str) -> Union[bool, list]:
        if letter_guessed in self.guessed_letters_list:
            return self.guessed_letters_list or False
        else:
            return self.guessed_letters_list.append(letter_guessed) or True

    def show_used_letters(self) -> str:
        return self.list_to_string(self.guessed_letters_list)

    def guessing_word_hide(self) -> str:
        print_guessing_word = []
        for letter_guessed in self.selected_word:
            if letter_guessed in self.guessed_letters_list:
                print_guessing_word.append(letter_guessed)
            else:
                print_guessing_word.append("_")
        return self.list_to_string(print_guessing_word)

    def check_if_whole_word_guessed(self) -> bool:
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

    def guess_one_letter(self, letter_guessed: str) -> int:
        if letter_guessed.isalpha() and len(letter_guessed) == 1:
            if self.check_unused_letters(letter_guessed) == True:
                if letter_guessed in self.selected_word:
                    if self.check_if_whole_word_guessed() == True:
                        logging.info(
                            f"Player {self.player_name} WINS. "
                            f"Word was: {self.list_to_string(self.selected_word)}. "
                            f"Guessed letters was: {self.list_to_string(self.guessed_letters_list)}"
                        )
                        return 1  # Winner
                    else:
                        return 6  # Correct! there is one or more letters
                else:
                    if self.bad_guess_counter() == self.max_guess:  # Bad guess counter
                        logging.info(
                            f"Player {self.player_name} LOST. "
                            f"Word was: {self.list_to_string(self.selected_word)}. "
                            f"Guessed letters was: {self.list_to_string(self.guessed_letters_list)}"
                        )
                        return 2  # You lose
                    else:
                        return 5  # Incorrect! there are no letters. Still have guess
            else:
                return 4  # "Info! You already used letter
        else:
            return 3  # Incorrect! You guess not a letter or write not one letter

    def guess_all_word(self, all_word: str) -> int:
        all_word_list = list(all_word)
        if all_word_list == self.selected_word:
            logging.info(
                f"Player {self.player_name} WINS. "
                f"Word was: {self.list_to_string(self.selected_word)}. "
                f"Guesses was made: {self.bad_guess_count}"
            )
            return 1  # Winner
        elif self.bad_guess_counter() == self.max_guess:
            logging.info(
                f"Player {self.player_name} LOST. "
                f"Word was: {self.list_to_string(self.selected_word)}. "
                f"Guesses was made: {self.bad_guess_count}"
            )
            return 2  # You lose
        else:
            return 3  # Incorrect guess
