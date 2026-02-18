import random

# Predefined words
words = ["python", "intern", "developer", "hangman", "program"]

# Choose random word
word = random.choice(words)

# Create blank display
guessed_word = ["_"] * len(word)

wrong_attempts = 0
max_attempts = 6
guessed_letters = []

print("Welcome to Hangman Game!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect attempts.\n")

while wrong_attempts < max_attempts and "_" in guessed_word:
    
    print("Word:", " ".join(guessed_word))
    guess = input("Enter a letter: ").lower()
    
    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!\n")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        wrong_attempts += 1
        print(f"Wrong guess! Attempts left: {max_attempts - wrong_attempts}\n")

if "_" not in guessed_word:
    print("Congratulations! You guessed the word:", word)
else:
    print("Game Over! The word was:", word)
