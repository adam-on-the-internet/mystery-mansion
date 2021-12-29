from tasks.game_generator import generate_game
import datetime

def log_start_message(start_time):
  print("~ MANSION STARTED GENERATING  @ " + str(start_time))

def log_end_message(start_time, end_time):
  length = end_time - start_time
  print("~ MANSION FINISHED GENERATING @ " + str(end_time))
  print("~ generation took " + str(length))

# start
start_time = datetime.datetime.now()
log_start_message(start_time)

# run
style = "classic"
mansion = generate_game(style)
print()
print("Generated " + style + " mansion " + mansion.id)
print()

# end
end_time = datetime.datetime.now()
log_end_message(start_time, end_time)
