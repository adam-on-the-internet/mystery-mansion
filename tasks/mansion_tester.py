from tasks.style_reader import read_rooms_setting, read_locked_rooms, read_furniture_setting

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

def test_furniture(style, interactions):
  expected = read_furniture_setting(style)
  if expected != len(interactions):
    print("ERR: Incorrect number of furniture generated.")

def test_mansion(mansion):
  test_id(mansion.id)
  test_spaces(mansion.style, mansion.spaces)
  test_locked_spaces(mansion.style, mansion.get_locked_spaces())
  test_furniture(mansion.style, mansion.get_all_interactions())
  # TODO test mansion for more things
  # NO ROOM should have more than 1 clue spot
  #   instead, test the actual issue (all clues must be findable without unlocking any doors)
  # NO ROOM should have less than 2 items of furniture
  # NO ROOM should have more than 5 items of furniture
