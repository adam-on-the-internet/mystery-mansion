from tasks.clue_selector import prepare_clue_deck
from tasks.game_file_writer import initialize_game_file
import datetime

start_time = datetime.datetime.now()
print("~ MYSTERY MANSION STARTING @ " + str(start_time))
print()

id = initialize_game_file()
prepare_clue_deck(id)
# hideMoney()
# setupFurniture()
# lockRooms()

end_time = datetime.datetime.now()
print()
print("~ MYSTERY MANSION ENDING   @ " + str(end_time))
print("~ Script ran in " + str(end_time - start_time))
