import random


print("Welcome to the Guessing Game!")
print("Try to guess the word, one letter at a time.")
print("You have 10 attempts to guess the word correctly.")
print("Let's begin!")

word_bank = ['liverpool','chelsea','arsenal','manchester united','tottenham','manchester city']
word = random.choice(word_bank)
guessedWord = ['_'] * len(word)
attempts = 10

while attempts > 0:
    print('\n Current word: ' + ' '.join(guessedWord))

    guess = input("Enter a letter: ").lower()
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
        print("Great guess!")
    else:
        attempts -= 1
        print('Wrong guess! Attempts left: ' + str(attempts))
    if '_' not in guessedWord:
        print('\n Congratulations! You guessed the word: ' + word)
        break

if attempts == 0 and '_' in guessedWord:
    print('\nYou\'ve run out of attempts! The word was: ' + word)
