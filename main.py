from tasks.clue_selector import setup_clues
from tasks.game_initializer import initialize_game
from tasks.mansion_builder import setup_mansion
import datetime

start_time = datetime.datetime.now()
print("~ MYSTERY MANSION STARTING @ " + str(start_time))
print()

id = initialize_game()
assets = setup_clues(id)
setup_mansion(id, assets)

end_time = datetime.datetime.now()
print()
print("~ MYSTERY MANSION ENDING   @ " + str(end_time))
print("~ Script ran in " + str(end_time - start_time))
