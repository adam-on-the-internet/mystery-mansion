from tasks.game_initializer import initialize_game
from tasks.mansion_builder import setup_mansion
from tasks.mansion_saver import save_mansion

def generate_game(game_style):
  id = initialize_game()
  mansion = setup_mansion(id)
  save_mansion(mansion)
  return mansion