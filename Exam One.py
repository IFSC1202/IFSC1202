import random

info = str(input("Hello! What is your name? "))
print("Well, " + info + ', ' + 'I am thinking of a number between 1 and 20.')
print("You have 5 guesses.")

x = random.randint(1, 20)
a = int(input("Take a guess: "))
counter = 0
while x != "a":
  counter += 1
  if (counter < 5):
    if a < x:
        print ("Your guess is too low.")
        a = int(input("Take a guess: "))
    elif a > x:
        print ("Your guess is too high.")
        a = int(input("Take a guess: "))
    else:
        print("Good job, " , info , '! ' + 'You guessed my number in' , counter , 'guesses!')
        break
  else:
    print("Nope. The number I was thinking of was",x)
    break