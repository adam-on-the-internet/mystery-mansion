from tasks.game_generator import generate_game
import random
import pyttsx3

def say_and_print_message(engine, message, secret_message):
  print(message)
  if secret_message != "":
    print()
    print("** FOR YOUR EYES ONLY **")
    print()
    print(secret_message)
    print()
    print("** FOR YOUR EYES ONLY **")
    print()
  if engine is not None:
    engine.say(message)
    engine.runAndWait()

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
  print(" - end        : END the game immediately.")

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
  print("\n\n\n\n\n\n\n\n\n\n")

def build_virtual_clue_deck(mansion):
  print()
  print("Setup 2 of 3:")
  input_deck_choice = input("Would you like to use a virtual Clue Deck? (y/n)\n").lower()
  use_virtual_deck = input_deck_choice == "y" or input_deck_choice == "yes"

  clue_deck = []
  if use_virtual_deck:
    for asset in mansion.assets:
      clue_deck.append(asset.clue.name)
    random.shuffle(clue_deck)
  return clue_deck

def choose_voice():
  print()
  print("Setup 3 of 3:")
  voice_choice = input("Would you like to use text-to-speech? (y/n)\n").lower()
  print()
  use_voice = voice_choice == "y" or voice_choice == "yes"
  if use_voice:
    return pyttsx3.init()
  else:
    return None

def choose_style():
  print()
  print("Setup 1 of 3:")

  classic_option = "Enter 1 for CLASSIC : original version, for use with the phyiscal game\n"
  small_option =   "Enter 2 for SMALL   : experimental version, shorter version for use with the physical game\n"  
  sequel_option =  "Enter 3 for SEQUEL  : experimental version, does not work with the physical game\n"
  style_prompt = "What game style would you like?\n\n" + classic_option + small_option + sequel_option + "\n"
  style_choice = input(style_prompt).lower()
  print()
  if str(style_choice) == "3":
    return "sequel"
  elif str(style_choice) == "2":
    return "small"
  elif str(style_choice) == "1":
    return "classic"
  else:
    return "classic"

# generate mansion with inputs
style = choose_style()
print(style.upper() + " style selected.")
mansion = generate_game(style)
clue_deck = build_virtual_clue_deck(mansion)
engine = choose_voice()

message = ""
code = ""
answers = []
investigation_count = 0
say_and_print_message(engine, "Welcome to Mystery Mansion!", "")
print()
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
    print("~~~~~~ Check #" + str(investigation_count + 1) + " ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
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
    elif code == "end":
      mansion.end_game()
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
      investigation_count = investigation_count + 1
      message = mansion.check_code(code)
  
  print()
  if message != "":
    secret_message = ""
    private_message_disclaimer = "\nAHEM. Look at the screen for a secret message.\nWhen you are finished, hit ENTER to clear the screen."
    should_deal_virtual_clue = len(clue_deck) != 0 and "You found a clue!" in message
    is_private_message = "** FOR YOUR EYES ONLY **" in message

    if should_deal_virtual_clue:
      drawn_clue = clue_deck.pop()
      message = message + private_message_disclaimer
      secret_message = "Add this clue to your inventory: " + drawn_clue
    elif is_private_message:
      split_message = message.split("** FOR YOUR EYES ONLY **")
      message = split_message[0].strip()
      message = message + private_message_disclaimer
      secret_message = split_message[1].strip()

    say_and_print_message(engine, message, secret_message)
    if secret_message != "":
      use_manual_clear()

say_and_print_message(engine, "\n\nSolved in " + str(investigation_count) + " checks.\n\n-- GAME OVER --", "")