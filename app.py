import os
import time
from main_program import HangManBase, PlayHangMan
from hang_man_graphic import hangman_graphic


def select_category() -> str:
    while True:
        select_word_category = input(
            f"\nFrom which word category you want to guess a word: \n1. Countries\n2. Animals \n"
        )
        try:
            select_word_category == int(select_word_category)
            select_word_category = int(select_word_category)
            word_to_guess = HangManBase().word_selection(select_word_category)
            return word_to_guess
        except ValueError:
            print("You enter not integer. Try again to select word category.\n")
            continue


def game_mode_setup() -> int:
    while True:
        select_game_mode_input = input(
            "How you try to guess a word:\n 1. Guess all word\n 2. Guess a letter\n 3. Change name\n 4. Exit\n"
        )
        try:
            select_game_mode_input == int(select_game_mode_input)
            select_game_mode_input = int(select_game_mode_input)
            if select_game_mode_input >= 1 and select_game_mode_input <= 4:
                return select_game_mode_input
            else:
                print("Non-existent selection. Try again to select game mode.\n")
        except ValueError:
            print("You enter not integer. Try again to select game mode.\n")
            continue


def all_word_mode(player_name: str, word_to_guess: str) -> None:
    main_game_mode = PlayHangMan(player_name, word_to_guess)
    while True:
        print(hangman_graphic[main_game_mode.bad_guess_count])
        print(f"You already made unsuccessful {main_game_mode.bad_guess_count} guesses")
        print(
            f"Word to guess:\n*****->   {main_game_mode.guessing_word_hide()}   <-*****"
        )
        all_word = input("So try to guess all word:\n").upper()
        os.system("cls")

        word_guess_mode = main_game_mode.guess_all_word(all_word)
        if word_guess_mode == 1:
            print(hangman_graphic[main_game_mode.bad_guess_count])
            print("Your guess was successful!!.")
            time.sleep(5)
            return main_meniu(player_name)
        elif word_guess_mode == 2:
            print("Your guesses was not successful.")
            print(hangman_graphic[main_game_mode.bad_guess_count])
            print("Word to guess was:", word_to_guess)
            time.sleep(5)
            return main_meniu(player_name)
        elif word_guess_mode == 3:
            print("Your gues was not successful.")
            continue


def letter_mode(player_name: str, word_to_guess: str) -> None:
    guess_letter = ""
    main_game_mode = PlayHangMan(player_name, word_to_guess)
    while True:
        print(hangman_graphic[main_game_mode.bad_guess_count])
        print(f"Already used letters:\n", main_game_mode.show_used_letters())
        print(
            f"Word to guess:\n*****->   {main_game_mode.guessing_word_hide()}   <-*****\n"
        )
        guess_letter = input("Guess a letter: ").upper()
        os.system("cls")
        letter_guess_mode = main_game_mode.guess_one_letter(guess_letter)
        print("* * * * * * * * * * * * * *\n")
        if letter_guess_mode == 6:
            print(f"Correct! there is one or more {guess_letter} in the word")
        elif letter_guess_mode == 5:
            print(f"Incorrect! there are no: {guess_letter}")
            print(f"You already made {main_game_mode.bad_guess_count} guesses")
        elif letter_guess_mode == 4:
            print(f"Info! You already used letter: {guess_letter}")
            print(f"Already used letters: ")
        elif letter_guess_mode == 3:
            print(
                f"Incorrect! You guess not a letter or write not one letter {guess_letter}"
            )
        elif letter_guess_mode == 2:
            print(hangman_graphic[main_game_mode.bad_guess_count])
            print("Sorry. You loose.")
            print("Word to guess was:", word_to_guess)
            time.sleep(5)
            return main_meniu(player_name)
        elif letter_guess_mode == 1:
            print(hangman_graphic[main_game_mode.bad_guess_count])
            print("You win!!!!!")
            time.sleep(5)
            return main_meniu(player_name)


def main_meniu(player_name: str) -> None:
    while True:
        word_to_guess = select_category()
        print("\n-----------------------")
        print(f"PASALINTI PRIES GALUTINI, SPEJAMAS ZODIS:    {word_to_guess}")
        print("-----------------------\n")
        main_game_mode = PlayHangMan(player_name, word_to_guess)
        print("* * * * * * * * * * * * * *\n")
        print(hangman_graphic[main_game_mode.bad_guess_count])
        print(
            f"Word to guess:\n*****->   {main_game_mode.guessing_word_hide()}   <-*****"
        )
        select_game_mode = game_mode_setup()
        os.system("cls")
        print("* * * * * * * * * * * * * *\n")
        if select_game_mode == 1:
            all_word_mode(player_name, word_to_guess)

        if select_game_mode == 2:
            letter_mode(player_name, word_to_guess)

        elif select_game_mode == 3:
            app()
        elif select_game_mode == 4:
            exit()


def app() -> None:
    player_name = str(input(f"Hello, player. Please enter your name. \n").upper())
    main_meniu(player_name)


if __name__ == "__main__":
    app()
