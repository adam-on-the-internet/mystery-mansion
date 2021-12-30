from tasks.style_reader import read_rooms_setting, read_furniture_setting

def test_id(id):
  if id is None:
    print("ERR: ID must be set.")
  elif len(id) != 4:
    print("ERR: ID must be 4 characters.")

def test_spaces(style, spaces):
  expected = read_rooms_setting(style)
  if expected != len(spaces):
    print("ERR: Incorrect number of rooms generated.")

def test_furniture(style, spaces):
  expected = read_furniture_setting(style)
  furniture_count = 0
  for space in spaces:
    for interaction in space.interactions:
      furniture_count = furniture_count + 1
  if expected != furniture_count:
    print("ERR: Incorrect number of furniture generated.")

def test_mansion(mansion):
  test_id(mansion.id)
  test_spaces(mansion.style, mansion.spaces)
  test_furniture(mansion.style, mansion.spaces)
  # TODO test mansion for more things
