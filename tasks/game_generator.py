from tasks.mansion_generator import generate_mansion
from tasks.mansion_tester import is_mansion_valid
from tasks.mansion_saver import save_mansion

def generate_game(style):
  waiting_for_valid_game = True
  mansion = None
  
  while waiting_for_valid_game:
    mansion = generate_mansion(style.lower())
    is_valid = is_mansion_valid(mansion)
    if is_valid:
      # stop & submit when we get a valid mansion, else we keep trying to generate one
      waiting_for_valid_game = False

  save_mansion(mansion)
  return mansion