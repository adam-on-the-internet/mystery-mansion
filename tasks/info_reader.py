from csv import reader

class MyFurniture:
  def __init__(self, game_code, name):
    self.game_code = game_code
    self.name = name

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

def read_furniture():
  with open("./info/furniture.csv", newline='') as furniture_file:
    furniture_reader = reader(furniture_file, delimiter=',')

    furniture = []

    for index, row in enumerate(furniture_reader):
      if index > 0 and len(row) > 0:
        game_code = row[0].strip()
        name = row[1].strip()
        myFurniture = MyFurniture(game_code, name)
        furniture.append(myFurniture)
    
    # TODO return 35 furniture
    
    return furniture

def read_clues():
  with open("./info/clues.csv", newline='') as clue_file:
    clue_reader = reader(clue_file, delimiter=',')

    clues = []

    for index, row in enumerate(clue_reader):
      if index > 0 and len(row) > 0:
        clue_type = row[0].strip()
        name = row[1].strip()
        myClue = MyClue(clue_type, name)
        clues.append(myClue)
    
    # TODO return 2 keys, 4 items, 4 people

    return clues
