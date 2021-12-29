from tasks.mansion_generator import generate_mansion
from tasks.mansion_saver import save_mansion

def generate_game(style):
  mansion = generate_mansion(style.lower())
  save_mansion(mansion)
  return mansion