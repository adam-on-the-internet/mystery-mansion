from tasks.game_generator import generate_game
import datetime
import sys

def log_start_message(start_time):
  print("~ MANSION(S) STARTED GENERATING  @ " + str(start_time))

def log_end_message(start_time, end_time):
  length = end_time - start_time
  print("~ MANSION(S) FINISHED GENERATING @ " + str(end_time))
  print("~ generation took " + str(length))

# start
start_time = datetime.datetime.now()
log_start_message(start_time)

# take inputs
style = "classic"
count = 1
if len(sys.argv) > 1:
  style = sys.argv[1]
if len(sys.argv) > 2:
  count = sys.argv[2]
print()
print("STYLE: " + style)
print("COUNT: " + str(count))
print()

# generate mansion(s)
for x in range(int(count)):
  mansion = generate_game(style)
  print("* generated " + style + " mansion " + mansion.id + " *")
print()

# end
end_time = datetime.datetime.now()
log_end_message(start_time, end_time)
