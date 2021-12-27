class MyMansion:
  def __init__(self, id, assets, spaces, code_history):
    self.id = id
    self.assets = assets
    self.spaces = spaces
    self.code_history = code_history
  def answer_question(self, code, answers):
    # TODO handle y/n checks 
    return "..."
  def check_code(self, code):
    message = ""
    for space in self.spaces:
      if space.game_code == code:
        message = space.get_message()
      else:
        for interaction in space.interactions:
          if interaction.furniture.game_code == code:
            message = interaction.get_message()
    if message == "":
      message = "That code is invalid."
    else:
      self.code_history.append(code)
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
  def __init__(self, interaction_type, name, requirement, hint, furniture):
    self.interaction_type = interaction_type
    self.name = name
    self.requirement = requirement
    self.hint = hint
    self.furniture = furniture
  def has_clue(self):
    return self.interaction_type == "clue"
  def has_money(self):
    return self.interaction_type == "money"
  def has_hint(self):
    return self.hint.strip() != ""
  def has_requirement(self):
    return self.requirement.strip() != ""
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
  def get_message(self):
    message = ""
    if self.has_requirement:
      message = "REQUIREMENT BLOCKS YOU." # TODO
    else:
      message = "..." # TODO
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
  def get_message(self):
    # TODO check room
    message = ""
    if self.is_locked:
      message = "This room is LOCKED. Do you have a KEY?"
    else:
      message = "This is the " + self.room.name + ". You see the following:"
      for interaction in self.interactions:
        message = message + "\n - " + interaction.furniture.name
    return "Room #" + self.game_code + " : " + message

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
    