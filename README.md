# Hangman_CLI
## Introduction
Hangman is an old school favorite, a word game where the goal is simply to find the missing word or words.
You will be presented with a number of blank spaces representing the missing letters you need to find.
Use the keyboard to guess a letter (I recommend starting with vowels).
If your chosen letter exists in the answer, then all places in the answer where that letter appear will be revealed.
After you've revealed several letters, you may be able to guess what the answer is and fill in the remaining letters.
Be warned, every time you guess a letter wrong you loose a life and the hangman begins to appear, piece by piece.
Solve the puzzle before the hangman dies.

### Briefly basic rules
* Can guess all word(s) in a row or letter by letter
* 10 incorrect guesses are possible (in both game modes)
* Solve the puzzle before the hangman dies.

## How to run the game
1. Pull source code from Git repository and open directory:
```bash
git clone https://github.com/vladas333/Hangman_CLI.git
cd Hangman_CLI
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
source .venv/Scripts/activate
```

3. Install requirements:
```bash
pip install -r requirements.txt
```
4. Run the game:
```bash
python app.py
```

## How to play the game
1. Then you run the game, it would ask to enter your name and press Enter.
2. After then, you have to select from which category you whant to guess a word.
3. In third meniu, you would be able to select how to guess all word: guess all word or guess a letter. More over, here you could change your name and you could exit the game.
4. Now all fun begins. Try to guess a word and don't to hang man.
5. After you win or lose, you would be redirected to Main meniu (pt 3).
