from tasks.clue_selector import prepare_clue_deck

import datetime

start_time = datetime.datetime.now()
print("~ MYSTERY MANSION STARTING @ " + str(start_time))

# prepare_game_file()
prepare_clue_deck()
# hideMoney()
# lockRooms()
# setupFurniture()

end_time = datetime.datetime.now()
print("~ MYSTERY MANSION ENDING   @ " + str(end_time))
print("~ Script ran in " + str(end_time - start_time))
