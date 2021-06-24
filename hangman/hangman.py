# Write your code here
import random
print("H A N G M A N")
options = ['python', 'java', 'kotlin', 'javascript']
winner = random.choice(options)
hidden = ["-"]*len(winner)
res = {letter: [] for letter in winner}
for idx, letter in enumerate(winner):
    res[letter].append(idx)
count = 0
while count < 8:
    print()
    print("".join(hidden))
    letter = input("Input a letter:")
    if letter in hidden:
        count += 1
        print("No improvements")
    elif letter in winner:
        indexes = res[letter]
        for idx in indexes:
            hidden[idx] = letter
        if "-" not in hidden:
            print("".join(hidden))
            print("You guessed the word!")
            print("You survived!")
            break
    else:
        count += 1
        print("That letter doesn't appear in the word")
else:
    print("You lost!")
