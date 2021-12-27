from tasks.game_generator import generate_game

print("Loading...")
mansion = generate_game()
print("Welcome to Mystery Mansion!")

money_is_hidden = True #TODO end game when money is found

while money_is_hidden:
  code = input("Enter code:  ")
  message = mansion.check_code(code)
  print()
  print("Code: " + code)
  print("Messge: " + message)
