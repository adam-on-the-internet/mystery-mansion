from tasks.game_file_writer import add_line_to_file
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

def select_person(clues, id):
  people = []
  for clue in clues:
    if clue.get_is_person():
      people.append(clue.name)
  random.shuffle(people)
  selected_person = people[0]
  add_line_to_file("Selected Person: " + selected_person, id)

def select_item(clues, id):
  items = []
  for clue in clues:
    if clue.get_is_item():
      items.append(clue.name)
  random.shuffle(items)
  selected_item = items[0]
  add_line_to_file("Selected Item: " + selected_item, id)

def shuffle_cards(clues, id):
  clue_deck = []

  for clue in clues:
    clue_deck.append(clue.name)

  random.shuffle(clue_deck)
  add_line_to_file("Clue Deck: " + str(clue_deck), id)

def prepare_clue_deck(id):
  print("preparing clue deck...")
  add_line_to_file("## Clue Setup", id)
  clues = read_clues()
  select_person(clues, id)
  select_item(clues, id)
  shuffle_cards(clues, id)
