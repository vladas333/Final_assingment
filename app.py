import logging
import random
from typing import Union
from hang_man import hanged
from word_list import ANIMAL_LIST

logging.basicConfig(
    level=logging.DEBUG,
    filename="player_data.log",
    filemode="a",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
)


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
    def __init__(self, player_name: str, selected_word: str) -> None:
        self.player_name = player_name
        self.selected_word = list(selected_word)
        self.secret_word_lenght = HangManBase().word_lenght(self.selected_word)
        self.guessed_letter_list = [" "]
        self.max_guess = 10

    def check_unused_letters(self, letter_guessed: str) -> Union[bool, list]:
        if letter_guessed in self.guessed_letter_list:
            return self.guessed_letter_list or False
        else:
            return self.guessed_letter_list.append(letter_guessed) or True

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

    def bad_guess_counter(self) -> bool:
        guess_count = 0
        for letter in self.guessed_letter_list:
            if letter not in self.selected_word:
                guess_count = guess_count + 1
        if guess_count != self.max_guess:
            return True
        else:
            return False
    
    def is_won(self) -> bool:
        counter = 0
        for letter in self.selected_word:
            if letter in self.guessed_letter_list:
                counter += 1
        if counter == len(self.selected_word):
            return True
        else:
            return False


        # check_selected_word = self.selected_word.copy()
        # # check_selected_word = list(set(check_selected_word))
        # # print(F"just cheking", check_selected_word)
        # # for letter in check_selected_word:
        # #     if letter != self.guessed_letter_list:
        # #         check_selected_word.remove(letter)
        # l3 = [x for x in check_selected_word if x not in self.guessed_letter_list]
        # print(F"just cheking", l3)
        # if not l3:
        #     print(f"false ", l3)
        #     return False
        # else:
        #     print(f"true ", l3)
        #     return True

    def guess_one_letter(self, letter_guessed: str) -> Union[list, int]:
        if letter_guessed.isalpha() and len(letter_guessed) == 1:
            if self.check_unused_letters(letter_guessed) == True:
                if letter_guessed in self.selected_word:
                    if self.is_won() == True:
                        logging.info(
                        f"Player {self.player_name} wins. "
                        f"Word was: {self.selected_word}."
                        f"{self.bad_guess_counter} bad guesses was made."
                    )
                        return 6 # Winner
                    else:
                        return 1 # Guess successfull
                else:
                    # counter_bad =
                    if self.bad_guess_counter() == True:  # Bad guess counter
                        return 2  # Still have guess
                    else:
                        logging.info(
                            f"Player {self.player_name} lost. "
                            f"Word was: {self.selected_word}."
                            f"Guessed letters was: {self.show_used_letters}")
                        return 5 
                        # Dont have guess
            else:
                return 3  # You already used letter
        else:
            return 4  # Not a letter used or user several letters

    def guess_all_word(self, all_word: str) -> bool:
        all_word_list = list(all_word)
        try:
            if all_word_list == self.selected_word:
                return True
        except:
            return False


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
        print(main_game_mode.guessing_word_hide(guess_letter))
        all_word = input("So try to guess all word:\n").upper()
        if main_game_mode.guess_all_word(all_word) == True:
            print("Yuor guess was successfull!!")
        else:
            print("Your guess was not successfull")
            print("Word to guess was:", word_to_guess.upper())
            break
    if select_game_mode == 2:
        while True:
            print(main_game_mode.guessing_word_hide(guess_letter))
            guess_letter = input("Guess a letter: ").upper()
            letter_guess_mode = main_game_mode.guess_one_letter(guess_letter)
            if letter_guess_mode == 1:
                print(f"correct! there is one or more {guess_letter} in the word")
                print(letter_guess_mode)
                print("* * * * * * * * * * * * * *\n")
            elif letter_guess_mode == 2:
                print(f"Incorrect! there are no: {guess_letter}")
                # bad_guess_count += 1
                print(f"Incorrect guesses: ")
                print(letter_guess_mode)
                print("* * * * * * * * * * * * * *\n")
            elif letter_guess_mode == 3:
                print(f"Info! You already used letter: {guess_letter}")
                print(f"Olready used letters: ")
                print(letter_guess_mode)
                print("* * * * * * * * * * * * * *\n")
            elif letter_guess_mode == 4:
                print(
                    f"Incorrect! You guess not a letter or write not one letter {guess_letter}"
                )
                print(letter_guess_mode)
                print("* * * * * * * * * * * * * *\n")
            elif letter_guess_mode == 5:
                print("You loose")
                break
            elif letter_guess_mode == 6:
                print("You win")
                break
            print(f"Olready used letters:\n", main_game_mode.show_used_letters())
        # Here should start winner or loser logic
    elif select_game_mode == 3:
        exit()
