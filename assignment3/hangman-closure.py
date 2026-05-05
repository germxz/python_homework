def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)

        display = ""
        for char in secret_word:
            if char in guesses:
                display += char
            else:
                display += "_"

        print(display)

        return "_" not in display

    return hangman_closure


if __name__ == "__main__":
    secret_word = input("Enter the secret word: ").lower()

    game = make_hangman(secret_word)

    print("\nStart guessing!")

    while True:
        guess = input("Guess a letter: ").lower()

        finished = game(guess)

        if finished:
            print("You guessed the word!")
            break