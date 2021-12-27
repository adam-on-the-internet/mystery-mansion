from tasks.game_generator import generate_game
import random

def print_help():
  print()
  print("You can enter these options:")
  print(" - clear")
  print(" - map")
  print(" - furniture")
  print(" - rules")
  print()

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

def print_rules():
  print()
  print("Rules available here: https://www.hasbro.com/common/instruct/Mystery_Mansion_(1996).PDF")
  print()

def print_furniture():
  print("Coming soon...") # TODO print furniture list on command
  print()

def use_manual_clear():
  input("Hit ENTER to clear the screen.")
  print_clear()

def print_clear():
  print("\n\n\n\n\n\n\n\n\n\n")
  print("\n\n\n\n\n\n\n\n\n\n")
  print("\n\n\n\n\n\n\n\n\n\n")
  print("\n\n\n\n\n\n\n\n\n\n")
  print("\n\n\n\n\n\n\n\n\n\n")
  print("\n\n\n\n\n\n\n\n\n\n")
  print("\n\n\n\n\n\n\n\n\n\n")
  print("\n\n\n\n\n\n\n\n\n\n")

def build_virtual_clue_deck(mansion):
  print()
  print("Setup 1 of 1:")
  input_deck_choice = input("Would you like to use a virtual Clue Deck? (y/n)\n").lower()
  use_virtual_deck = input_deck_choice == "y" or input_deck_choice == "yes"

  clue_deck = []
  if use_virtual_deck:
    for asset in mansion.assets:
      clue_deck.append(asset.clue.name)
    random.shuffle(clue_deck)
  return clue_deck

mansion = generate_game()
clue_deck = build_virtual_clue_deck(mansion)
message = ""
code = ""
answers = []

print()
print("Welcome to Mystery Mansion!")
print()
print_map()
print_rules()

while not mansion.game_over:
  message = ""
  
  if message.endswith("?"):
    answer = input("Answer (y/n):\n").lower()
    requirement_met = answer == "y" or answer == "yes"
    answers.append(requirement_met)
    message = mansion.answer_question(code, answers)
  else:
    print("Enter a Room Code, Furniture Code, or 'HELP' for more options.")
    code = input("Enter code:\n").lower()
    if code == "help":
      print_help()
    elif code == "rules":
      print_rules()
    elif code == "map":
      print_map()
    elif code == "clear":
      print_clear()
    elif code == "furniture":
      print_furniture()
    else:
      answers = []
      message = mansion.check_code(code)
  
  print()
  if message != "":
    print(message)

  if len(clue_deck) != 0 and "You found a clue!" in message:
    drawn_clue = clue_deck.pop()
    print("Add this clue to your inventory : " + drawn_clue)
    use_manual_clear()
  if "FOR YOUR EYES ONLY" in message:
    use_manual_clear()

  print()