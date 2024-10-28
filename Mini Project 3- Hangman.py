import random


# list of words and randomly showing a word
word_list = ["apple", "banana", "kiwi", "strawberry"]
random_word = random.choice(word_list)

guesses = 6
index_list = []
current_word = " "
guessed_letters = []

# creating a list
random_list = list(random_word)
print(random_list)

# dash per letter
secret_word = list("_" * len(random_word))
print(secret_word)

print("Welcome to HANGMAN")
print()
print(f"Current word: {" ".join(secret_word)}")
print(f"Guessed letters: - ")
print(f"Incorrect guesses remaining: {guesses} ")

while True:
    letter = input("Guess a letter: ")


    if letter not in guessed_letters:

        for i in range(len(random_list)):
            if random_list[i] == letter:
                index_list.append(i)
                print(index_list)

        for i in index_list:
            secret_word[i] = letter

        current_word = " ".join(secret_word)
        index_list.clear()

        guessed_letters.append(letter)

    else:
        print("You already guessed that letter")
        continue

    if letter not in random_list:
        guesses -= 1
        print(f"Sorry,- {letter} - is not in the word, try again")

    if guesses <= 0:
        print("You failed")
        print(f"The word was: {"".join(random_list)}")
        break

    print()
    print(f"Current word: {current_word}")
    print(f"Guessed letters: {",".join(guessed_letters)}")
    print(f"Incorrect guesses remaining: {guesses} ")










