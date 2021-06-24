# Write your code here
import random
import string
print("H A N G M A N")
options = ['python', 'java', 'kotlin', 'javascript']
winner = random.choice(options)
hidden = ["-"]*len(winner)
res = {letter: [] for letter in winner}
for idx, letter in enumerate(winner):
    res[letter].append(idx)
count = 0
tries = set()
while count < 8:
    print()
    print("".join(hidden))
    letter = input("Input a letter:")
    if len(letter) == 1 and letter not in string.ascii_letters.lower():
        print("Please enter a lowercase English letter")
    elif len(letter) != 1:
        print("You should input a single letter")
    elif letter in tries:
        print("You've already guessed this letter")
    elif letter in winner:
        indexes = res[letter]
        for idx in indexes:
            hidden[idx] = letter
        if "-" not in hidden:
            print("".join(hidden))
            print("You guessed the word!")
            print("You survived!")
            break
        tries.add(letter)
    else:
        tries.add(letter)
        count += 1
        print("That letter doesn't appear in the word")
else:
    print("You lost!")
