#Hangman code practice
import random
from hangmanart import stages
from hangmanword import word_list

lives = [1, 2, 3, 4, 5, 6]
chosen_word = random.choice(word_list)
# print(chosen_word)

word_Length = len(chosen_word)

display = []
for _ in range(word_Length):
    display += "_"
print(display)

chosen_word_List = []
for word in chosen_word:
    chosen_word_List += word
    
remaining_Lives = len(lives)
while display != chosen_word_List:
    guess = input("Guess a letter: \n").lower()
    if guess in display:
        print(f"You have already used {guess}")

    for position in range(word_Length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)

    if guess not in chosen_word:
        remaining_Lives -= 1
        print(f"Your choice {guess} is not in the word. You lose a life.{remaining_Lives} lives left")
        print(stages[remaining_Lives])
        if remaining_Lives == 0:
            print("Game Over! You Fail")
            exit()

print(f"The word is {chosen_word} YOU WIN!")

