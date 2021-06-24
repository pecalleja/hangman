# Write your code here
import random
print("H A N G M A N")
print("Guess the word:")
text = input()
options = ['python', 'java', 'kotlin', 'javascript']
winner = random.choice(options)
if text in winner:
    print("You survived!")
else:
    print("You lost!")
