import random

def is_numeric(num):
  """
  This will return true if num is an int
  """
  return isinstance(num, int)

def guess_number(random_number, top_range):
  """
  This will get a guess from the users and let them know if
  - the guess is too high
  - the guess is too low
  - the guess is correct
  It will then prompt them to play again
  """
  guess = int(input("Guess a number between 0 and " + str(top_range) + ": "))

  if guess < random_number:
    print("Too low")
    guess_number(random_number, top_range)
  elif guess > random_number:
    print ("Too high")
    guess_number(random_number, top_range)
  else:
    print ("You got it!")
    play_again = input("Would you like to play again? (Y or N)")

    if (play_again == "Yes" or play_again == "yes" or play_again == "Y" or play_again == "y" or play_again == "YES"):
      play_game()
    else:
      print ("Thank you! Good bye!")

    
def play_game():
  """
  This will :
  - get input (int) from the user
  - generate a random number between 0 and input from user
  - call the guess_number function
  """
  try: 
    top_range = int(input("Enter a number: "))
  except ValueError:
    print ("You must enter a valid number")
    play_game()
  
  if (top_range < 1):
    print ("Number must be greater than 0")
    play_game()
    
  random_number = random.randint(0, top_range)
  guess_number(random_number, top_range)

play_game()
