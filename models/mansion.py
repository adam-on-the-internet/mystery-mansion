from util.string_utils import get_four_letter_id

class MyMansion:
  def __init__(self, style, assets, spaces, code_history, game_over, clues_taken):
    self.id = get_four_letter_id()
    self.style = style
    self.assets = assets
    self.spaces = spaces
    self.code_history = code_history
    self.game_over = game_over
    self.clues_taken = clues_taken
  def get_locked_spaces(self):
    locked_spaces = []
    for space in self.spaces:
      if space.is_locked:
        locked_spaces.append(space)
    return locked_spaces
  def get_unlocked_spaces(self):
    unlocked_spaces = []
    for space in self.spaces:
      if not space.is_locked:
        unlocked_spaces.append(space)
    return unlocked_spaces
  def get_all_interactions(self):
    _interactions = []
    for space in self.spaces:
      for interaction in space.interactions:
        _interactions.append(interaction)
    return _interactions
  def print_available_clues(self):
    print()
    print("Available Clues:")
    print("----------------")
    for asset in self.assets:
      print(asset.clue.name)
    print()
    print("Clues taken: " + str(self.clues_taken) + " of " + str(len(self.assets)))
  def print_available_rooms(self):
    print()
    print("Available Rooms:")
    print("----------------")
    print()
    for space in self.spaces:
      if space.discovered:
        print(space.room.name + " (" + space.game_code + ")")
      else:
        print("???")
  def print_available_furniture(self):
    print()
    print("Available Furniture:")
    print("----------------")
    for space in self.spaces:
      for interaction in space.interactions:
        if interaction.discovered:
          print(interaction.furniture.name + " (" + interaction.furniture.game_code + ")")
        else:
          print("???")
  def check_space_discovery(self, x, y):
    space_icon = "____"
    for space in self.spaces:
      if str(x) == space.coordinates[0] and str(y) == space.coordinates[1]:
        if space.discovered:
          space_icon = " " + str(space.game_code) + " "
        else:
          space_icon = str(space.game_code) + " ?"
        if len(space_icon) == 3:
          space_icon = " " + space_icon
    return space_icon
  def end_game(self):
    self.game_over = True
  def print_code(self):
    print("Mansion Code: " + self.id)
  def print_map(self):
    if self.style in ["classic", "sequel"]:
      print()
      print("Map of the Mansion:")
      if self.style == "classic":
        print("          ______          ")
        print("o--------/      \--------o")
      elif self.style == "sequel":
        print("o-------o--------o-------o")
      print("|       |        |       |")
      print("| " + self.check_space_discovery(2,-1) + "  x  " + self.check_space_discovery(2,0) + "  x " + self.check_space_discovery(2,1) + "  |")
      print("|       |        |       |")
      print("o---xx------xx------xx---o")
      print("|       |        |       |")
      print("| " + self.check_space_discovery(1,-1) + "  x  " + self.check_space_discovery(1,0) + "  x " + self.check_space_discovery(1,1) + "  |")
      print("|       |        |       |")
      print("o---xx------xx------xx---o")
      print("|       |        |       |")
      print("| " + self.check_space_discovery(0,-1) + "  x  " + self.check_space_discovery(0,0) + "  x " + self.check_space_discovery(0,1) + "  |")
      print("|       |        |       |")
      print("o-------o---xx---o-------o")
      print("        | start  |       ")
    elif self.style == "small":
      print()
      print("Map of the Mansion:")
      print("o-------o-------o")
      print("|       |       |")
      print("| " + self.check_space_discovery(1,0) + "  x " + self.check_space_discovery(1,1) + "  |")
      print("|       |       |")
      print("o---xx-----xx---o")
      print("|       |       |")
      print("| " + self.check_space_discovery(0,0) + "  x " + self.check_space_discovery(0,1) + "  |")
      print("|       |       |")
      print("o---xx--o-------o")
      print("| start |       ")
  def take_clue(self):
    self.clues_taken = self.clues_taken + 1
  def answer_question(self, code, answers):
    if len(answers) == 0:
      return "Invalid input."
    recent_answer = answers[-1]
    if False in answers:
      return "Sorry..."
    elif len(answers) > 2:
      return "The provided answer(s) is invalid."
    else:
      return self.check_code_with_answers(code, answers)
  def check_code(self, code):
    return self.check_code_with_answers(code, [])
  def check_code_with_answers(self, code, answers):
    message = ""
    for space in self.spaces:
      if space.game_code == code:
        message = space.get_message(answers)
      else:
        for interaction in space.interactions:
          if interaction.furniture.game_code == code:
            message = interaction.get_message(answers)
    if message == "":
      message = "That code is invalid."
    else:
      self.code_history.append(code)

    if "You found a clue!" in message:
      if self.clues_taken >= len(self.assets):
        message = message.replace("You found a clue!", "Take a clue from another player.")
      self.take_clue()
    elif "You win!" in message:
      self.end_game()

    return message   
