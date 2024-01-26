import random
import hangman_stages
word_list = ["grace", "apple", "emily", "beautiful", "kevin"]
chosen_word = random.choice(word_list)
print(word_list)
lives = 6
display = []
for x in range(len(chosen_word)):
    display += '_'
print(display)
end_of_game = False
while not end_of_game:
    Guessed_letter = input("Geuss a latter: ").lower()
    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        if letter == Guessed_letter:
            display[i] = Guessed_letter
    print(display)
    if Guessed_letter not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!😥")
    if '_' not in display:
        end_of_game = True
        print("You win!😁🦾")
    print(hangman_stages.stages[lives])