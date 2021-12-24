from csv import reader
import random

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
    
    return clues

def select_person(clues):
  people = []
  for clue in clues:
    if clue.get_is_person():
      people.append(clue.name)
  random.shuffle(people)
  selected_person = people[0]
  # TODO write

def select_item(clues):
  items = []
  for clue in clues:
    if clue.get_is_item():
      items.append(clue.name)
  random.shuffle(items)
  selected_item = items[0]
  # TODO write

def shuffle_cards(clues):
  random.shuffle(clues)
  # TODO write

def prepare_clue_deck():
  print("preparing clue deck...")
  clues = read_clues()
  select_person(clues)
  select_item(clues)
  shuffle_cards(clues)
