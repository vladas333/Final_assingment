import random
from hang_man import hanged

from word_list import ANIMAL_LIST


class HangManBase:
    def __init__(self) -> None:
        self.animal_list = ANIMAL_LIST

    def word_selection(self) -> str:
        return random.choice(self.animal_list).upper()

    def word_lenght(self, picked_word: str) -> int:
        return len(picked_word.replace(" ", ""))
    

class PlayHangMan(HangManBase):
    DATA_RETURN_DICT = {
        "max_failure" : 10,
        "wrong_guesses" : 0,
        "all_guessed_letters" : ""
        }
    def __init__(self, player_name: str, selected_word: str) -> None:
        self.player_name = player_name
        self.selected_word = selected_word
        self.secret_word_lenght = HangManBase().word_lenght(self.selected_word)
        self.secret_word_list = []

    def check_unused_letter(self, letter_guessed: str) -> bool:
        pass

    def secret_word_print(self, letter_guessed: str) -> None:
        
        for letter_guessed in self. selected_word:
            if letter_guessed in 
            
    def start_program(self, letter_guessed: str) -> bool:
        if self.check_unused_letter(letter_guessed) == True:

            if letter_guessed in self.selected_word:
                return True
    





# player_name = str(input(f"Hello, player. Please enter your name. \n").upper())
while True:
    player_name = str(input(f"Hello, player. Please enter your name. \n").upper())
    word_to_guess = HangManBase().word_selection()
    select_game_mode = int(input("How you try to guess a word:\n 1. Guess all word\n 2. Guess a letter\n 3. Exit"))
    if select_game_mode == 1:
        print("Later it would work")
    elif select_game_mode == 2:
        letter_guess_mode = PlayHangMan(player_name, word_to_guess)
        max_bad_guess = 10
        bad_guess_count = 0
        while bad_guess_count != max_bad_guess:
            guess_letter = input("Guess a letter: ").upper()
            if letter_guess_mode.start_program(guess_letter) == True:
                print(f"correct! there is one or more {guess_letter} in the word")
            else:
                print(f"Incorrect! there are no {guess_letter}")
                bad_guess_count += 1
    elif select_game_mode == 3:
        exit()


    