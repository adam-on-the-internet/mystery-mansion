class MyAsset:
  def __init__(self, name, asset_type, clue):
    self.name = name
    self.asset_type = asset_type
    self.clue = clue
  def get_requirement_message(self):
    if self.clue.get_is_person():
      return "Is the " + self.clue.name + " with you?"
    elif self.clue.get_is_item():
      return "Do you have the " + self.clue.name + "?"
    else:
      return "Invalid clue."
  def get_is_person(self):
    return self.asset_type == "person"
  def get_is_item(self):
    return self.asset_type == "item"
  def get_is_key(self):
    return self.asset_type == "key"
  def get_is_person_or_item(self):
    return self.asset_type == "person or item"
  def to_string(self):
    return self.clue.name + ": " + self.name
