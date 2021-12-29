from csv import reader
from models.asset import MyAsset
from models.interaction import MyInteraction
from models.clue import MyClue
from models.furniture import MyFurniture
from models.space import MySpace
from models.room import MyRoom
import random

def get_style_file_path(style, file):
  return "./style/" + style + "/" + file + ".csv"

def read_assets(style):
  file_path = get_style_file_path(style, "assets")
  with open(file_path, newline='') as asset_file:
    asset_reader = reader(asset_file, delimiter=',')
    assets = []
    for index, row in enumerate(asset_reader):
      if index > 0 and len(row) > 0:
        name = row[0].strip()
        asset_type = row[1].strip()
        myAsset = MyAsset(name, asset_type, '')
        assets.append(myAsset)
    return assets  

def read_interactions(style):
  file_path = get_style_file_path(style, "interactions")
  with open(file_path, newline='') as interaction_file:
    interaction_reader = reader(interaction_file, delimiter=',')
    interactions = []
    for index, row in enumerate(interaction_reader):
      if index > 0 and len(row) > 0:
        interaction_type = row[0].strip()
        name = row[1].strip()
        requirement = row[2].strip()
        hint = row[3].strip()
        myInteraction = MyInteraction(interaction_type, name, requirement, hint, '', False, 0, [])
        interactions.append(myInteraction)
    return interactions  

def read_spaces(style):
  file_path = get_style_file_path(style, "spaces")
  with open(file_path, newline='') as space_file:
    space_reader = reader(space_file, delimiter=',')
    spaces = []
    for index, row in enumerate(space_reader):
      if index > 0 and len(row) > 0:
        coordinates = row[0].strip().split("|")
        game_code = row[1].strip()
        name = row[2].strip()
        can_be_locked = row[3].strip() == "true"
        mySpace = MySpace(coordinates, game_code, name, can_be_locked, False, '', '', False)
        spaces.append(mySpace)
    return spaces

def read_rooms(style):
  file_path = get_style_file_path(style, "rooms")
  with open(file_path, newline='') as room_file:
    room_reader = reader(room_file, delimiter=',')
    rooms = []
    for index, row in enumerate(room_reader):
      if index > 0 and len(row) > 0:
        name = row[0].strip()
        myRoom = MyRoom(name)
        rooms.append(myRoom)
    return rooms[:9] 

def read_furniture(style):
  file_path = get_style_file_path(style, "furniture")
  with open(file_path, newline='') as furniture_file:
    furniture_reader = reader(furniture_file, delimiter=',')
    furniture = []
    for index, row in enumerate(furniture_reader):
      if index > 0 and len(row) > 0:
        game_code = row[0].strip()
        name = row[1].strip()
        rooms = row[2].strip()
        linked_code = row[3].strip()
        linked_text = row[4].strip()
        available_rooms = rooms.split("|")
        random.shuffle(available_rooms)
        selected_room = available_rooms[0].strip()
        myFurniture = MyFurniture(game_code, name, rooms, linked_code, linked_text, selected_room)
        furniture.append(myFurniture)
    return furniture[:35]

def read_clues(style):
  file_path = get_style_file_path(style, "clues")
  with open(file_path, newline='') as clue_file:
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
