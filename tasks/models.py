class MyMansion:
  def __init__(self, id, assets, spaces, code_history, game_over, clues_taken):
    self.id = id
    self.assets = assets
    self.spaces = spaces
    self.code_history = code_history
    self.game_over = game_over
    self.clues_taken = clues_taken
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
  def end_game(self):
    self.game_over = True
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

class MyAsset:
  def __init__(self, name, asset_type, clue):
    self.name = name
    self.asset_type = asset_type
    self.clue = clue
  def get_is_person(self):
    return self.asset_type == "person"
  def get_is_item(self):
    return self.asset_type == "item"
  def get_is_key(self):
    return self.asset_type == "key"
  def get_is_person_or_item(self):
    return self.asset_type == "person or item"
  def to_string(self):
    return self.clue.name + " : " + self.name

class MyInteraction:
  def __init__(self, interaction_type, name, requirement, hint, furniture, discovered, clues_taken):
    self.interaction_type = interaction_type
    self.name = name
    self.requirement = requirement
    self.hint = hint
    self.furniture = furniture
    self.discovered = discovered
    self.clues_taken = clues_taken
  def discover(self):
    self.discovered = True
  def take_clue(self):
    self.clues_taken = self.clues_taken + 1
  def has_clue(self):
    return self.interaction_type == "clue"
  def has_money(self):
    return self.interaction_type == "money"
  def has_hint(self):
    return self.hint.strip() != ""
  def has_public_hint(self):
    return self.has_hint() and "public hint" in self.interaction_type
  def has_private_hint(self):
    return self.has_hint() and "private hint" in self.interaction_type
  def has_requirement(self):
    return self.requirement.strip() != ""
  def has_single_requirement(self):
    return self.requirement.strip() != "" and not "&" in self.requirement
  def has_double_requirement(self):
    return self.requirement.strip() != "" and "&" in self.requirement
  def hint_message(self):
    if self.has_hint():
      return " [HINT: " + self.hint + "]"
    else:
      return ""
  def requirement_message(self):
    if self.has_requirement():
      return " [REQUIREMENT: " + self.requirement + "]"
    else:
      return ""
  def to_string(self):
    return self.furniture.name + " (code " + self.furniture.game_code + ") : " + self.name + self.requirement_message() + self.hint_message()
  def get_message(self, answers):
    if not self.discovered:
      return "Sorry, this item is not yet discovered."
    completed_checks = len(answers)
    recent_check_passed = completed_checks > 0 and answers[-1]

    show_full_message = (not self.has_requirement()) or (self.has_single_requirement() and completed_checks == 1 and recent_check_passed) or (self.has_double_requirement() and completed_checks == 2 and recent_check_passed)

    ask_requirement_1 = (self.has_single_requirement() and completed_checks == 0) or (self.has_double_requirement() and completed_checks == 0)
    
    ask_requirement_2 = (self.has_double_requirement() and completed_checks == 1 and recent_check_passed)

    message = ""
    if show_full_message:
      if self.has_money():
        message = "You found the money. You win!"
      elif self.has_clue():
        if self.clues_taken > 1:
          message = "Sorry, there are no clues left here."
        else:
          message = "You found a clue!"
        self.take_clue()
      elif self.has_public_hint():
        message = self.hint
      elif self.has_private_hint():
        message = "(FOR YOUR EYES ONLY) " + self.hint
      else:
        message = "Invalid input."
    elif ask_requirement_1:
      requirement = self.requirement.split("&")[0]
      message = "Do you have the " + requirement + "?" # TODO vary by person or item
    elif ask_requirement_2:
      requirement = self.requirement.split("&")[1]
      message = "Do you have the " + requirement + "?" # TODO vary by person or item
    else:
      message = "Invalid input."

    return self.furniture.name + " : " + message

class MySpace:
  def __init__(self, game_code, name, can_be_locked, is_locked, room, interactions):
    self.game_code = game_code
    self.name = name
    self.can_be_locked = can_be_locked
    self.is_locked = is_locked
    self.room = room
    self.interactions = interactions
  def locked_message(self):
    return " [LOCKED]" if self.is_locked else ""
  def to_string(self):
    return self.room.name + self.locked_message() + " (code " + self.game_code + ")"
  def unlock_door(self):
    self.is_locked = False
  def get_message(self, answers):
    should_unlock = self.is_locked and len(answers) == 1 and answers[0]
    if should_unlock:
      self.unlock_door()

    message = ""
    if self.is_locked:
      message = "This room is LOCKED. Do you have a KEY?"
    else:
      message = "This is the " + self.room.name + ". You see the following:"
      for interaction in self.interactions:
        interaction.discover()
        furniture_name = interaction.furniture.name
        furniture_code = interaction.furniture.game_code
        if not "#2" in furniture_name:
          if "#1" in furniture_name:
            furniture_name = furniture_name.replace(" #1", "")
            furniture_name = "Two " + furniture_name + "s"
            furniture_code = furniture_code + " & ?"
          message = message + "\n - " + furniture_name + " (" + furniture_code + ")"
    return "Room " + self.game_code + " : " + message

class MyRoom:
  def __init__(self, name):
    self.name = name

class MyFurniture:
  def __init__(self, game_code, name, rooms, selected_room):
    self.game_code = game_code
    self.name = name
    self.rooms = rooms
    self.selected_room = selected_room

class MyClue:
  def __init__(self, clue_type, name):
    self.clue_type = clue_type
    self.name = name
  def get_is_person(self):
    return self.clue_type == "person"
  def get_is_item(self):
    return self.clue_type == "item"
  def get_is_key(self):
    return self.clue_type == "key"
    