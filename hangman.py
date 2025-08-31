import random

# A list to hold the different visual stages of the hangman
hangman_stages = [
    # Stage 10 (Final)
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """,
    # Stage 9
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    # Stage 8
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    # Stage 7
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    # Stage 6
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    # Stage 5
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    # Stage 4
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    # Stage 3
    """
       +---+
           |
           |
           |
           |
           |
    =========
    """,
    # Stage 2
    """
           |
           |
           |
           |
           |
    =========
    """,
    # Stage 1
    """
    =========
    """,
    # Stage 0 (Initial empty state)
    ""
]


wordList = ["rizz", "ohio", "sigma", "tiktok", "skibidi"]
word = random.choice(wordList)
guessedWord = ['_'] * len(word)
attempts = 10

print("Welcome to Hangman!")

while attempts > 0:
    
    print(hangman_stages[attempts])
    
    print("\nCurrent word: " + ' '.join(guessedWord))
    print(f"You have {attempts} wrong guesses left.")

    guess = input("Guess a letter: ").lower()
   
    
    if guess in guessedWord:
        print(f"You've already guessed '{guess}'. Try again.")
        continue 

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
        print("Great guess!")
    else:
        attempts -= 1
        print(f"Wrong guess! The letter '{guess}' is not in the word.")

    if '_' not in guessedWord:
        print("\nCongratulations!! You guessed the word: " + word)
        break
else:
    
    print(hangman_stages[0]) 
    print("\nYou've run out of attempts! The word was: " + word)