from tasks.clue_selector import setup_clues
from tasks.game_initializer import initialize_game
from tasks.mansion_builder import setup_mansion

def generate_game():
  id = initialize_game()
  assets = setup_clues(id)
  return setup_mansion(id, assets)