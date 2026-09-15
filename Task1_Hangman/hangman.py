import random

WORDS = ["python", "django", "react", "coding", "developer"]


MAX_WRONG_GUESSES = 6


def play_hangman():
    word = random.choice(WORDS)

    hidden_word = []

    for letter in word:
        hidden_word.append("_")
    wrong_guesses = 0
    guessed_letters = []

    print("====================")
    print("     HANGMAN GAME")
    print("====================")

    print(" ".join(hidden_word))

    while True:
        print("\tGuessed letters:", ", ".join(guessed_letters))
        print("Attempts remaining:", MAX_WRONG_GUESSES - wrong_guesses)


        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue


        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue


        guessed_letters.append(guess)


        if guess in word:
            print("Correct!")


            for i in range(len(word)):
                if word[i] == guess:
                    hidden_word[i] = guess

            print(" ".join(hidden_word))


            if "_" not in hidden_word:
                print("\tCongratulations! You won!")
                print("The word was:", word)
                break

        else:
            print("Wrong!")

            wrong_guesses += 1

            if wrong_guesses == MAX_WRONG_GUESSES:
                print("\tGame Over!")
                print("The word was:", word)
                break

while True:
    play_hangman()

    play_again = input("\tDo you want to play again? (y/n): ").lower()

    if play_again != "y":
        print("Thanks for playing!")
        break