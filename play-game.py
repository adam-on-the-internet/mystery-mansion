from tasks.game_generator import generate_game

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
