class MyInteraction:
  def __init__(self, interaction_type, name, requirement, hint, furniture, discovered, clues_taken, required_assets):
    self.interaction_type = interaction_type
    self.name = name
    self.requirement = requirement
    self.hint = hint
    self.furniture = furniture
    self.discovered = discovered
    self.clues_taken = clues_taken
    self.required_assets = required_assets
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
    return len(self.required_assets) == 1
  def has_double_requirement(self):
    return len(self.required_assets) == 2
  def hint_message(self):
    if self.has_hint():
      return " [HINT: " + self.hint + "]"
    else:
      return ""
  def requirement_message(self):
    if self.has_requirement():
      _requirement_message = ""
      for asset in self.required_assets:
        if _requirement_message != "":
          _requirement_message = _requirement_message + " & "
        _requirement_message = _requirement_message + asset.clue.name
      return " [REQUIREMENT: " + _requirement_message.strip() + "]"
    else:
      return ""
  def to_string(self):
    return self.furniture.name + " (code " + self.furniture.game_code + "): " + self.name + self.requirement_message() + self.hint_message()
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
        clues_per_space = 2 # TODO make the clues-per-space value set in the style/settings
        if self.clues_taken >= clues_per_space:
          message = "Sorry, there are no clues left here."
        else:
          message = "You found a clue!"
        self.take_clue()
      elif self.has_public_hint():
        message = self.hint
      elif self.has_private_hint():
        message = "** FOR YOUR EYES ONLY ** " + self.hint
      else:
        message = "Invalid input."
    elif ask_requirement_1:
      asset = self.required_assets[0]
      message = asset.get_requirement_message()
    elif ask_requirement_2:
      asset = self.required_assets[1]
      message = asset.get_requirement_message()
    else:
      message = "Invalid input."

    return self.furniture.name + " (" + self.furniture.game_code + "): " + message
