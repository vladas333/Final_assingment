import random
from typing import Union
from hang_man import hanged
from word_list import ANIMAL_LIST


class HangManBase:
    def __init__(self) -> None:
        self.animal_list = ANIMAL_LIST

    def word_selection(self) -> str:
        return random.choice(self.animal_list).upper()

    def word_lenght(self, picked_word: str) -> int:
        return len(picked_word)
    
    def list_to_string(self, print_guessing_word: list) -> str:
        hidden_word = ""
        for element in print_guessing_word:
            hidden_word += element
        return hidden_word


class PlayHangMan(HangManBase):
    DATA_RETURN_DICT = {
        "max_failure": 10,
        "wrong_guesses": 0,
        "all_guessed_letters": "",
    }

    def __init__(self, player_name: str, selected_word: str) -> None:
        self.player_name = player_name
        self.selected_word = list(selected_word)
        self.secret_word_lenght = HangManBase().word_lenght(self.selected_word)
        self.guessed_letter_list = [" "]

    def check_unused_letters(self, letter_guessed: str) -> Union[bool, list]:
        if letter_guessed in self.guessed_letter_list:
            return self.guessed_letter_list or False
        else:
            return self.guessed_letter_list.append(letter_guessed) or True

    # def list_to_string(self, print_guessing_word: list) -> str:
    #     hidden_word = ""
    #     for element in print_guessing_word:
    #         hidden_word += element
    #     return hidden_word
    
    def show_used_letters(self) -> str:
        return self.list_to_string(self.guessed_letter_list)

    def guessing_word_hide(self, letter_guessed: str) -> str:
        print_guessing_word = []
        for letter_guessed in self.selected_word:
            if letter_guessed in self.guessed_letter_list:
                print_guessing_word.append(letter_guessed)
            else:
                print_guessing_word.append("-")
        return self.list_to_string(print_guessing_word)
    
    
    def start_program(self, letter_guessed: str) -> Union[list, int]:
        if letter_guessed.isalpha():
            if self.check_unused_letters(letter_guessed) == True:
                if letter_guessed in self.selected_word:
                    return 1
                else:
                    return 2
            else:
                return 3
        else:
            return 4


while True:
    player_name = str(input(f"Hello, player. Please enter your name. \n").upper())
    word_to_guess = HangManBase().word_selection()
    main_game_mode = PlayHangMan(player_name, word_to_guess)
    guess_letter = ""
    print(word_to_guess)
    print(main_game_mode.guessing_word_hide(guess_letter))
    select_game_mode = int(
        input(
            "How you try to guess a word:\n 1. Guess all word\n 2. Guess a letter\n 3. Exit\n"
        )
    )
    print("* * * * * * * * * * * * * *\n")
    if select_game_mode == 1:
        print("Later it would work")
    if select_game_mode == 2:
        max_bad_guess = 10
        bad_guess_count = 0
        while bad_guess_count != max_bad_guess:
            print(main_game_mode.guessing_word_hide(guess_letter))
            guess_letter = input("Guess a letter: ").upper()
            letter_guess_mode = main_game_mode.start_program(guess_letter)
            if letter_guess_mode == 1:
                print(f"correct! there is one or more {guess_letter} in the word")
                print(letter_guess_mode)
                print("* * * * * * * * * * * * * *\n")
            elif letter_guess_mode == 2:
                print(f"Incorrect! there are no: {guess_letter}")
                bad_guess_count += 1
                print(f"Incorrect guesses: ", bad_guess_count)
                print(letter_guess_mode)
                print("* * * * * * * * * * * * * *\n")
            elif letter_guess_mode == 3:
                print(f"Info! You olready used letter: {guess_letter}")
                print(f"Olready used letters: ", bad_guess_count)
                print(letter_guess_mode)
                print("* * * * * * * * * * * * * *\n")
            elif letter_guess_mode == 4:
                print(f"Incorrect! there are no {guess_letter}")
                print(f"Incorrect guesses: ", bad_guess_count)
                print(letter_guess_mode)
                print("* * * * * * * * * * * * * *\n")
            print(f"Olready used letters:\n", main_game_mode.show_used_letters())
        # Here should start winner or loser logic
    elif select_game_mode == 3:
        exit()
