from tasks.game_initializer import initialize_game
from tasks.clue_selector import setup_clues
from tasks.mansion_builder import setup_mansion
from tasks.mansion_saver import save_mansion

def generate_game():
  id = initialize_game()
  assets = setup_clues(id)
  mansion = setup_mansion(id, assets)
  save_mansion(mansion)
  return mansion