from tasks.style_reader import read_rooms_setting, read_locked_rooms, read_furniture_setting, read_clues_setting

def test_id(id):
  if id is None:
    print("ERR: ID must be set.")
  elif len(id) != 4:
    print("ERR: ID must be 4 characters.")

def test_spaces(style, spaces):
  expected = read_rooms_setting(style)
  if expected != len(spaces):
    print("ERR: Incorrect number of rooms generated.")

def test_locked_spaces(style, locked_spaces):
  expected = read_locked_rooms(style)
  if expected != len(locked_spaces):
    print("ERR: Incorrect number of locked rooms generated.")

def test_unlocked_spaces(style, unlocked_spaces):
  total_clues = read_clues_setting(style)
  clues_per_space = 2 # TODO make clues-per-space set in style/settings
  unlocked_clue_interactions = 0
  for space in unlocked_spaces:
    for interaction in space.interactions:
      if interaction.has_clue():
        unlocked_clue_interactions = unlocked_clue_interactions + 1
  unlocked_clues = unlocked_clue_interactions * clues_per_space
  if total_clues > unlocked_clues:
    print("ERR: The clues are set incorrectly, the game may become unwinnable.")

def test_furniture(style, interactions):
  expected = read_furniture_setting(style)
  if expected != len(interactions):
    print("ERR: Incorrect number of furniture generated.")

def test_furniture_per_room(spaces):
  for space in spaces:
    if len(space.interactions) < 2:
      print("ERR: A room was generated incorrectly, " + space.room.name + " has less than 2 items of furniture.")
    elif len(space.interactions) > 5:
      print("ERR: A room was generated incorrectly, " + space.room.name + " has more than 5 items of furniture.")

def test_mansion(mansion):
  test_id(mansion.id)
  test_spaces(mansion.style, mansion.spaces)
  test_locked_spaces(mansion.style, mansion.get_locked_spaces())
  test_unlocked_spaces(mansion.style, mansion.get_unlocked_spaces())
  test_furniture(mansion.style, mansion.get_all_interactions())
  test_furniture_per_room(mansion.spaces)
