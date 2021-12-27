from tasks.game_generator import generate_game

def print_map():
  print()
  print("Here's the Map of Mystery Mansion:")
  print()
  print("0--------------------0")
  print("|      |      |      |")
  print("|  22  x  21  x  14  |")
  print("|      |      |      |")
  print("0--xx-----xx-----xx--0")
  print("|      |      |      |")
  print("|  23  x  31  x  13  |")
  print("|      |      |      |")
  print("0--xx-----xx-----xx--0")
  print("|      |      |      |")
  print("|  24  x  11  x  12  |")
  print("|      |      |      |")
  print("0---------xx---------0")
  print("       |start |       ")
  print()

def print_furniture():
  print("Coming soon...") # TODO print furniture list on command
  print()

def print_clear():
  print("\n\n\n\n\n\n\n\n\n\n")
  print("\n\n\n\n\n\n\n\n\n\n")
  print("\n\n\n\n\n\n\n\n\n\n")
  print("\n\n\n\n\n\n\n\n\n\n")
  print("\n\n\n\n\n\n\n\n\n\n")
  print("\n\n\n\n\n\n\n\n\n\n")
  print("\n\n\n\n\n\n\n\n\n\n")
  print("\n\n\n\n\n\n\n\n\n\n")

print("Loading...")
mansion = generate_game()
print("Loading completed.")
print()

message = ""
code = ""
answers = []

print()
print("Welcome to Mystery Mansion!")
print()
print_map()

while not mansion.game_over:
  message = ""
  
  if message.endswith("?"):
    answer = input("Answer (y/n):  ").lower()
    requirement_met = answer == "y" or answer == "yes"
    answers.append(requirement_met)
    message = mansion.answer_question(code, answers)
  else:
    print("You can enter a Room Code or Furniture Code.")
    print("You can also enter 'map', 'clear', and 'furniture'.")
    code = input("Enter code:  ").lower()
    if code == "map":
      print_map()
    elif code == "clear":
      print_clear()
    elif code == "furniture":
      print_furniture()
    else:
      answers = []
      message = mansion.check_code(code)
  
  if message != "":
    print()
    print(message)
    print()
