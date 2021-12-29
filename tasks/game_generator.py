from tasks.mansion_builder import setup_mansion
from tasks.mansion_saver import save_mansion

def generate_game(style):
  mansion = setup_mansion(style)
  save_mansion(mansion)
  return mansion