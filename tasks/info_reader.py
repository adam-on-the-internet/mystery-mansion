from csv import reader
import random

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
    return self.furniture.name + " : " + self.name + self.requirement_message() + self.hint_message()

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
    return self.room.name + self.locked_message() + " (" + self.game_code + ")"

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

def read_assets():
  with open("./info/assets.csv", newline='') as asset_file:
    asset_reader = reader(asset_file, delimiter=',')
    assets = []
    for index, row in enumerate(asset_reader):
      if index > 0 and len(row) > 0:
        name = row[0].strip()
        asset_type = row[1].strip()
        myAsset = MyAsset(name, asset_type, '')
        assets.append(myAsset)
    return assets  

def read_interactions():
  with open("./info/interactions.csv", newline='') as interaction_file:
    interaction_reader = reader(interaction_file, delimiter=',')
    interactions = []
    for index, row in enumerate(interaction_reader):
      if index > 0 and len(row) > 0:
        interaction_type = row[0].strip()
        name = row[1].strip()
        requirement = row[2].strip()
        hint = row[3].strip()
        myInteraction = MyInteraction(interaction_type, name, requirement, hint, '')
        interactions.append(myInteraction)
    return interactions  

def read_spaces():
  with open("./info/spaces.csv", newline='') as space_file:
    space_reader = reader(space_file, delimiter=',')
    spaces = []
    for index, row in enumerate(space_reader):
      if index > 0 and len(row) > 0:
        game_code = row[0].strip()
        name = row[1].strip()
        can_be_locked = row[2].strip() == "true"
        mySpace = MySpace(game_code, name, can_be_locked, False, '', '')
        spaces.append(mySpace)
    return spaces

def read_rooms():
  with open("./info/rooms.csv", newline='') as room_file:
    room_reader = reader(room_file, delimiter=',')
    rooms = []
    for index, row in enumerate(room_reader):
      if index > 0 and len(row) > 0:
        name = row[0].strip()
        myRoom = MyRoom(name)
        rooms.append(myRoom)
    return rooms[:9] 

def read_furniture():
  with open("./info/furniture.csv", newline='') as furniture_file:
    furniture_reader = reader(furniture_file, delimiter=',')
    furniture = []
    for index, row in enumerate(furniture_reader):
      if index > 0 and len(row) > 0:
        game_code = row[0].strip()
        name = row[1].strip()
        rooms = row[2].strip()
        available_rooms = rooms.split("|")
        random.shuffle(available_rooms)
        selected_room = available_rooms[0].strip()
        myFurniture = MyFurniture(game_code, name, rooms, selected_room)
        furniture.append(myFurniture)
    return furniture[:35]

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
    sorted_clues = []
    key_count = 0
    item_count = 0
    person_count = 0
    for clue in clues:
      if clue.get_is_key() and key_count < 2:
        sorted_clues.append(clue)
        key_count = key_count + 1
      elif clue.get_is_item() and item_count < 4:
        sorted_clues.append(clue)
        item_count = item_count + 1
      elif clue.get_is_person() and person_count < 4:
        sorted_clues.append(clue)
        person_count = person_count + 1
    return sorted_clues
