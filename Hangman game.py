import random

def hangman():
    # List of words for the game
    word_list = ['python', 'programming', 'computer', 'hangman', 'algorithm']
    word = random.choice(word_list)  # Randomly select a word
    guessed_word = ['_' for _ in word]  # Hidden word represented by underscores
    attempts = 6  # Number of incorrect guesses allowed
    guessed_letters = set()  # Track guessed letters

    print("Welcome to Hangman!")
    print("Guess the word:", " ".join(guessed_word))

    while attempts > 0 and ''.join(guessed_word) != word:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
        elif guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
            print("Good guess:", " ".join(guessed_word))
        else:
            attempts -= 1
            print(f"Incorrect! You have {attempts} attempts left.")

        guessed_letters.add(guess)

    if ''.join(guessed_word) == word:
        print(f"Congratulations! You've guessed the word: {word}")
    else:
        print(f"Sorry, you've run out of attempts. The word was: {word}")

# Start the game
hangman()
