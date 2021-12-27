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

print("Loading...")
mansion = generate_game()
print("Loading completed.")
print()

message = ""
code = ""
answers = []

while not mansion.game_over:
  if message == "":
    print()
    print("Welcome to Mystery Mansion!")
    print()
    print_map()
  
  if message.endswith("?"):
    answer = input("Answer (y/n):  ").lower()
    requirement_met = answer == "y" or answer == "yes"
    answers.append(requirement_met)
    message = mansion.answer_question(code, answers)
  else:
    code = input("Enter code:  ")
    answers = []
    message = mansion.check_code(code)
  
  print()
  print(message)
  print()
