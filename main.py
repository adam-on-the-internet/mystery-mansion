from tasks.clue_selector import setup_clues
from tasks.game_initializer import initialize_game
from tasks.mansion_builder import setup_mansion
import datetime

def log_start_message(start_time):
  print("~ MYSTERY MANSION STARTING @ " + str(start_time))
  print()

def log_end_message(start_time, end_time):
  length = end_time - start_time
  print()
  print("~ MYSTERY MANSION ENDING   @ " + str(end_time))
  print("~ Script ran in " + str(length))

# start
start_time = datetime.datetime.now()
log_start_message(start_time)

# run
id = initialize_game()
assets = setup_clues(id)
setup_mansion(id, assets)

# end
end_time = datetime.datetime.now()
log_end_message(start_time, end_time)