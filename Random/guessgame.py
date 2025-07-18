secret_word = "Om"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Guess the secret word: ")
        if guess != secret_word:
            print("Incorrect guess. Try again.")
        else:
            print("Correct! You've guessed the secret word.")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Sorry, you've run out of guesses. The secret word was:", secret_word)
else:
    print("Congratulations! You've guessed the secret word.")
