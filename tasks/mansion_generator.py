from tasks.clue_generator import generate_clues
from tasks.space_generator import generate_spaces
from tasks.models import MyMansion

def generate_mansion(style):
  assets = generate_clues(style)
  spaces = generate_spaces(assets, style)
  return MyMansion(style, assets, spaces, [], False, 0)
