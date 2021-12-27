from tasks.game_generator import generate_game

print("Loading...")
mansion = generate_game()
print("Loading completed.")
print()

money_is_hidden = True #TODO end game when money is found
message = ""
code = ""
answer = ""

while money_is_hidden:
  if message == "":
    print("Welcome to Mystery Mansion!")
  
  if message.endswith("?"):
    # resolve question (y/n)
    # TODO handle question
    answer = input("Answer (y/n):  ").lower()
    message = mansion.answer_question(code, answer)
  else:
    # resolve room or furniture code
    code = input("Enter code:  ")
    answer = ""
    message = mansion.check_code(code)
  print()
  
  if code != "":
    print("INPUT Code: " + code)

  if answer != "":
    print("INPUT Answer: " + code)
  
  print("Message: " + message)
