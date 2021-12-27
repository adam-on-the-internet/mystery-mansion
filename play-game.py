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
    print("Welcome to Mystery Mansion!")
  
  if message.endswith("?"):
    # TODO resolve single question (y/n)
    # TODO resolve double question (y/n)
    answer = input("Answer (y/n):  ").lower()
    answers.append(answer)
    message = mansion.answer_question(code, answers)
  else:
    # resolve room or furniture code
    code = input("Enter code:  ")
    answers = []
    message = mansion.check_code(code)
  
  print()
  print("INPUT Code   : " + code)
  print("INPUT Answers: " + str(answers))
  print("GAME OVER: " + str(mansion.game_over))
  
  print()
  print(message)
  print()
