import random
from word_list import ANIMAL_LIST


class HangManBase:
    def __init__(self) -> None:
        self.animal_list = ANIMAL_LIST

    def word_selection(self) -> str:
        return random.choice(self.animal_list).upper()

    def word_lenght(self, picked_word: str) -> int:
        return len(picked_word.replace(" ", ""))
    

class WordGuessing(HangManBase):
    DATA_RETURN_DICT = {
        "max_failure" : 10,
        "wrong_guesses" : 0,
        "all_guessed_letters" : ""
        }
    def __init__(self, player_name: str, selected_word: str) -> None:
        self.player_name = player_name
        self.selected_word = selected_word
        self.secret_word_lenght = HangManBase().word_lenght(self.selected_word)
        
    def start_program(self, letter_guessed: int) -> dict:
        pass