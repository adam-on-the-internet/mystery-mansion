import datetime

startTime = datetime.datetime.now()
print("~ MYSTERY MANSION STARTING @ " + str(startTime))

shuffleClueDeck()
hideMoney()
lockRooms()
setupFurniture()

endTime = datetime.datetime.now()
print("~ MYSTERY MANSION ENDING   @ " + str(endTime))
print("~ Script ran in " + str(endTime - startTime))
