from tasks.style_reader import read_rooms_setting, read_locked_rooms, read_furniture_setting, read_clues_setting

def test_id(errs, id):
  if id is None:
    errs.append("ID must be set.")
  elif len(id) != 4:
    errs.append("ID must be 4 characters.")
  return errs

def test_spaces(errs, style, spaces):
  expected = read_rooms_setting(style)
  if expected != len(spaces):
    errs.append("Incorrect number of rooms generated.")
  return errs

def test_locked_spaces(errs, style, locked_spaces):
  expected = read_locked_rooms(style)
  if expected != len(locked_spaces):
    errs.append("Incorrect number of locked rooms generated.")
  return errs

def test_unlocked_spaces(errs, style, unlocked_spaces):
  total_clues = read_clues_setting(style)
  clues_per_space = 2 # TODO make clues-per-space set in style/settings
  unlocked_clue_interactions = 0
  for space in unlocked_spaces:
    for interaction in space.interactions:
      if interaction.has_clue():
        unlocked_clue_interactions = unlocked_clue_interactions + 1
  unlocked_clues = unlocked_clue_interactions * clues_per_space
  if total_clues > unlocked_clues:
    errs.append("The clues are set incorrectly, the game may become unwinnable.")
  return errs

def test_furniture(errs, style, interactions):
  expected = read_furniture_setting(style)
  if expected != len(interactions):
    errs.append("Incorrect number of furniture generated.")
  return errs

def test_furniture_per_room(errs, spaces):
  for space in spaces:
    if len(space.interactions) < 2:
      errs.append("A room was generated incorrectly, " + space.room.name + " has less than 2 items of furniture.")
    elif len(space.interactions) > 5:
      errs.append("A room was generated incorrectly, " + space.room.name + " has more than 5 items of furniture.")
  return errs

def is_mansion_valid(mansion):
  errs = []
  errs = test_id(errs, mansion.id)
  errs = test_spaces(errs, mansion.style, mansion.spaces)
  errs = test_locked_spaces(errs, mansion.style, mansion.get_locked_spaces())
  errs = test_unlocked_spaces(errs, mansion.style, mansion.get_unlocked_spaces())
  errs = test_furniture(errs, mansion.style, mansion.get_all_interactions())
  errs = test_furniture_per_room(errs, mansion.spaces)
  if len(errs) > 0:
    print()
    print("Errors found with mansion " + mansion.id + ":")
    for err in errs:
      print(err)
    print()
    return False
  else:
    return True
  # TODO more tests? better test setup?
