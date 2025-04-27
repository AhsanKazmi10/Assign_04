import random

words = ["apple", "banana", "cherry", "grape", "orange", "watermelon"]

hangman_stages = [
    """
       ------
       |    |
       |    
       |   
       |   
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   
       |   
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |   
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |   
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / 
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------
    """
]

def choose_word():
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display

def play_hangman():
    word = choose_word()
    guessed_letters = []
    tries = 6  

    print("Welcome to Hangman with Rassi!")
    print("Guess the word:")

    while tries >= 0:
        print(hangman_stages[6 - tries])
        print(display_word(word, guessed_letters))
        if tries == 0:
            print(f"Sorry, you ran out of tries. The word was: {word}")
            break

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You guessed the word: {word}")
                break
        else:
            tries -= 1
            print(f"Wrong guess. You have {tries} tries left.")

play_hangman()
