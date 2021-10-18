movies_watched = {"The Matrix", "Green Book", "Her"}

user_movie = input("Enter a movie: ")

if user_movie in movies_watched:
  print("I've watched %s" % movies_watched)
else:
  print("I've not watched %s" % movies_watched)


print("\n")

number = 7


while True:

  user_input = input("Play? (y/n) ")

  if  user_input  == 'n':
    break

  user_number = int(input("Guess a number: "))

  if  user_number == number:
    print("You win!")
  elif user_number < number:
    print("your guess is lower than the lucky number.")
  elif user_number > number:
    print("your guess is higher than the lucky number.")
  else:
    print("Wrong!")
  
