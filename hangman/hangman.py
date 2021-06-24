# Write your code here
import random
print("H A N G M A N")
options = ['python', 'java', 'kotlin', 'javascript']
winner = random.choice(options)
hidden = ["-"]*len(winner)
res = {letter: [] for letter in winner}
for idx, letter in enumerate(winner):
    res[letter].append(idx)
for i in range(8):
    print()
    print("".join(hidden))
    print("Input a letter:")
    letter = input()
    if letter in winner:
        indexes = res[letter]
        for idx in indexes:
            hidden[idx] = letter
    else:
        print("That letter doesn't appear in the word")

print("""
Thanks for playing!
We'll see how well you did in the next stage
""")
