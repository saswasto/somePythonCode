import random
import time

print("HANGMAN GAME")
name = input("Enter your name: ")
print("Hello " + name + ", best of luck!")
time.sleep(2)
print("The game is about to start! Let's play Hangman.")
time.sleep(3)


def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game

    words_to_guess = ["january", "border", "image", "film", "promise", "kids", "lungs", "doll", "rhyme", "damage",
                      "plants"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = "_ " * length
    already_guessed = []
    play_game = ""


def play_loop():
    global play_game

    play_game = input("Do you want to play again? Y = yes, N = no")

    while play_game not in ["Y", "y", "N", "n"]:
        play_game = input("Do you want to play again? Y = yes, N = no")

    if play_game == "Y" or play_game == "y":
        main()
        hangman()
    elif play_game == "N" or play_game == "n":
        print("Thanks for playing! Come back again.")
        exit()


def hangman():
    global count
    global display
    global word
    global already_guessed
    limit = 5

    guess = input("This is the Hangman Word: " + display + " Enter your guess: ")
    guess = guess.strip()

    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()

    elif guess in word:
        already_guessed += guess
        for i in range(0, length):
            if word[i] == guess:
                display = display[:i] + guess + display[i+1:]

        print(display + "\n")

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print(" _____ ")
            print(" | ")
            print(" | ")
            print(" | ")
            print(" | ")
            print(" | ")
            print("__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining.\n")

        elif count == 2:
            time.sleep(1)
            print(" _____ ")
            print(" |   | ")
            print(" |   O ")
            print(" | ")
            print(" | ")
            print(" | ")
            print("__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining.\n")

        elif count == 3:
            time.sleep(1)
            print(" _____ ")
            print(" |   | ")
            print(" |   O ")
            print(" |   | ")
            print(" |   | ")
            print(" | ")
            print("__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining.\n")

        elif count == 4:
            time.sleep(1)
            print(" _____ ")
            print(" |   | ")
            print(" |   O ")
            print(" |  /|\\")
            print(" |   | ")
            print(" |  / \\")
            print("__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining.\n")

        elif count == 5:
            time.sleep(1)
            print(" _____ ")
            print(" | | ")
            print(" | | ")
            print(" | | ")
            print(" | O ")
            print(" | /|\\ ")
            print(" | / \\ ")
            print("__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:", already_guessed, word)
        elif count == 4:
            time.sleep(1)
            print(" _____ ")
            print(" |   | ")
            print(" |   O ")
            print(" |  /| ")
            print(" | ")
            print(" | ")
            print("__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining.\n")

        elif count == 5:
            time.sleep(1)
            print(" _____ ")
            print(" |   | ")
            print(" |   O ")
            print(" |  /|\\ ")
            print(" | ")
            print(" | ")
            print("__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining.\n")

        elif count == 6:
            time.sleep(1)
            print(" _____ ")
            print(" |   | ")
            print(" |   O ")
            print(" |  /|\\ ")
            print(" |  / ")
            print(" | ")
            print("__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining.\n")

        elif count == 7:
            time.sleep(1)
            print(" _____ ")
            print(" |   | ")
            print(" |   O ")
            print(" |  /|\\ ")
            print(" |  / \\ ")
            print(" | ")
            print("__|__\n")
            print("Game over. The word was " + word + ".")
        main()

        if word == display:
            print("Congrats! You have guessed the word correctly!")
            play_loop()

        elif count != limit:
            hangman()


def play_loop():
    play_again = input("Do you want to play again")

