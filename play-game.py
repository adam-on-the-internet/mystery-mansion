from tasks.game_generator import generate_game
import random

def print_help():
  print()
  print("You can enter these options:")
  print(" - clear      : CLEAR the terminal.")
  print(" - code       : Show game CODE.")
  print(" - roll       : ROLL a six-sided die.")
  print(" - map        : Display a MAP of the mansion.")
  print(" - furniture  : Display the FURNITURE available in this game.")
  print(" - rooms      : Display the ROOMS available in this game.")
  print(" - clues      : Display the CLUES available in this game.")
  print(" - rules      : Display a link to the RULES Online.")
  print(" - exit       : EXIT the game.")

def print_roll():
  result = random.randrange(6) + 1
  print("You rolled a " + str(result) + ".")

def print_rules():
  print()
  print("Rules available here: https://www.hasbro.com/common/instruct/Mystery_Mansion_(1996).PDF")

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
turn_count = 1

print()
print("Welcome to Mystery Mansion!")
mansion.print_code()
print()
mansion.print_map()
print_rules()

while not mansion.game_over:
  previous_message = message
  message = ""
  if previous_message.endswith("?"):
    answer = input("Answer (y/n):\n").lower()
    requirement_met = answer == "y" or answer == "yes"
    answers.append(requirement_met)
    message = mansion.answer_question(code, answers)
  else:
    print()
    print()
    print("~~~~ Turn #" + str(turn_count) + " ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    print("Enter a Room Code, Furniture Code, or 'help' for more options.")
    code = input("Enter code:\n").lower()
    if code == "help":
      print_help()
    elif code == "roll":
      print_roll()
    elif code == "rules":
      print_rules()
    elif code == "clear":
      print_clear()
    elif code == "code":
      mansion.print_code()
    elif code == "map":
      mansion.print_map()
    elif code == "furniture":
      mansion.print_available_furniture()
    elif code == "rooms":
      mansion.print_available_rooms()
    elif code == "clues":
      mansion.print_available_clues()
    else:
      answers = []
      turn_count = turn_count + 1
      message = mansion.check_code(code)
  
  print()
  if message != "":
    print("(READ ALOUD) " + message)

  if len(clue_deck) != 0 and "You found a clue!" in message:
    drawn_clue = clue_deck.pop()
    print("Add this clue to your inventory : " + drawn_clue)
    use_manual_clear()
  if "FOR YOUR EYES ONLY" in message:
    use_manual_clear()
