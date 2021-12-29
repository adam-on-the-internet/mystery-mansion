from tasks.style_reader import read_furniture, read_interactions
import random

def get_clue_interactions(interactions):
  matching_interactions = []
  for interaction in interactions:
    if interaction.has_clue():
      matching_interactions.append(interaction)
  return matching_interactions

def get_non_clue_interactions(interactions):
  matching_interactions = []
  for interaction in interactions:
    if not interaction.has_clue():
      matching_interactions.append(interaction)
  return matching_interactions

def generate_interactions(style):
  interactions = read_interactions(style)
  random.shuffle(interactions)

  clue_interactions = get_clue_interactions(interactions)
  non_clue_interactions = get_non_clue_interactions(interactions)
  
  furniture = read_furniture(style)
  random.shuffle(furniture)

  # We set a max of 1 clue interaction per room.
  # If more than 2 clues are in locked rooms, the game can become unwinnable.
  # Placing 1 clue per room removes that possibility, as only 2 rooms are locked.
  clue_rooms = []
  for interaction in clue_interactions:
    furniture_index = 0
    selected = False
    while not selected:
      selected_furniture = furniture[furniture_index]
      if selected_furniture.selected_room not in clue_rooms:
        clue_rooms.append(selected_furniture.selected_room)
        interaction.furniture = furniture.pop(furniture_index)
        selected = True
      else:
        furniture_index = furniture_index + 1

  # set non-clue interactions
  for index, interaction in enumerate(non_clue_interactions):
    interaction.furniture = furniture[index]

  all_interactions = clue_interactions + non_clue_interactions
  return all_interactions
