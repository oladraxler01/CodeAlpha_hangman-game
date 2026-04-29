#Hangman in python
from wordbank import words
import random


#dictionary of key:()
hangman_art = {0: ("   ",
                   "   ",
                   "   "),

              1: (" o ",
                   "   ",
                  "   "),

              2: (" o ",
                  " | ",
                 "   "),

              3: (" o ",
                  "/| ",
                  "   "),

              4: (" o ",
                 "/|\\",
                 "   "),

              5: (" o ",
                 "/|\\",
                 "/  "),

              6: (" o",
                 "/|\\",
                 "/ \\")}


#function to display the hangman art based on the number of wrong guesses
def display_man(wrong_guesses):
    print("**hangman_art**")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("**hangman_art**")


def display_hint(hint):
    print(" ".join(hint))


def display_answer(answer):
    print(" ".join(answer))

#main function to run the game
def main():
    answer = random.choice(words)
    hint =["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

#while loop to run the game until the player wins or loses
    while is_running :
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Guess a letter: ").lower()


# a loop to fileter the input of multiple letters and non-alphabetic characters
        if len(guess) != 1 or not guess.isalpha():
            print("invalid input")
            continue

# to filter out already guessed letter to avoid penalizing the player for guessing the same letter multiple times

        if guess in guessed_letters:
            print("you already guessed that letter")
            continue

        guessed_letters.add(guess)




#if the guess is correct, update the hint list with the guessed letter in the correct positions. If the guess is incorrect, increment the wrong_guesses counter. The game continues until the player either guesses all the letters correctly or reaches the maximum number of wrong guesses (6 in this case).

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess

        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("congratulations! you won!")
            is_running = False

        elif wrong_guesses >= 6:
            display_man(wrong_guesses)
            display_answer(answer)
            print("sorry, you lost!")
            is_running = False






if __name__ == "__main__":
    main()


