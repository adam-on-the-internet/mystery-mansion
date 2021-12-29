class MySpace:
  def __init__(self, coordinates, game_code, name, can_be_locked, is_locked, room, interactions, discovered):
    self.coordinates = coordinates
    self.game_code = game_code
    self.name = name
    self.can_be_locked = can_be_locked
    self.is_locked = is_locked
    self.room = room
    self.interactions = interactions
    self.discovered = discovered
  def discover(self):
    self.discovered = True
  def locked_message(self):
    return " [LOCKED]" if self.is_locked else ""
  def to_string(self):
    return self.room.name + self.locked_message() + " (code " + self.game_code + ")"
  def unlock_door(self):
    self.is_locked = False
  def get_message(self, answers):
    message = ""

    should_unlock = self.is_locked and len(answers) == 1 and answers[0]
    if should_unlock:
      self.unlock_door()
      message = message + "Door unlocked. Discard the Key you used to open this door.\n"

    if self.is_locked:
      message = message + "This room is LOCKED. Do you have a KEY?"
    else:
      self.discover()
      message = message + "This is the " + self.room.name + ". You see the following:"
      for interaction in self.interactions:
        interaction.discover()
        furniture = interaction.furniture
        furniture_name = furniture.name
        furniture_code = furniture.game_code
        if furniture.linked_code != "0":
          if furniture.linked_code != "":
            furniture_name = furniture.linked_text
            furniture_code = furniture_code + " & " + furniture.linked_code
          message = message + "\n - " + furniture_name + " (" + furniture_code + ")"
    return "Room " + self.game_code + ": " + message
