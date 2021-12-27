from tasks.game_generator import generate_game

print("Loading...")
mansion = generate_game()
print("Loading completed.")
print()

money_is_hidden = True #TODO end game when money is found
message = ""
code = ""
answers = []

while money_is_hidden:
  if message == "":
    print("Welcome to Mystery Mansion!")
  
  if message.endswith("?"):
    # TODO resolve single question (y/n)
    # TODO resolve double question (y/n)
    answer = input("Answer (y/n):  ").lower()
    answers.push(answer)
    message = mansion.answer_question(code, answers)
  else:
    # resolve room or furniture code
    code = input("Enter code:  ")
    answers = []
    message = mansion.check_code(code)
  
  print()
  print("INPUT Code   : " + code)
  print("INPUT Answers: " + answers)
  
  print()
  print(message)
  print()
