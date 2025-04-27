import random
print("Welcome to the Number Guessing Game!")

low = 1
high = 10

print("Think of a number between 1 and 10 and computer will guess it.")

if low <= high:
   guess = random.randint(low, high)
   print(f"Computer's guess {guess}?")
   while True:
         feedback = input("Enter 'h' if the guess is too high, 'l' if it's too low, and 'c' if it's correct: ").lower()
         if feedback == 'h':
              high = guess - 1
              guess = random.randint(low, high)
              print(f"Computer's guess {guess}?")
         elif feedback == 'l':
              low = guess + 1
              guess = random.randint(low, high)
              print(f"Computer's guess {guess}?")
         elif feedback == 'c':
              print("Yay! Computer guessed your number.")
              break
         else:
              print("Invalid input. Please enter 'h', 'l', or 'c'.")
if low > high:
   print("Invalid range. Please try again.")