# Mystery Mansion

An app to assist with the game "Electronic Talking Mystery Mansion".
That game features a specialized Electronic Device called the "Talking Organizer".
This app was created in part to replace that Electronic Component, in case it ever stops working or batteries are unavailable.

## Actions

### Play a Game

Run "python play-game.py" to randomly generate a Mansion and then immediately play through that game from the command-line.

When playing a game, you'll have a few options with prompts:

- Step 1: Choose a Style. Enter 1 for CLASSIC or 2 for SEQUEL. (more about these under "Styles")
- Step 2: Choose whether to use a virtual Clue Deck. If you do not have the physical game, the Virtual Deck will help.
- Step 3: Choose whether to use text-to-speech. This feature adds some flair and attempts to mimick the original game's "Talking Organizer" (sadly, without voice-acting).

### Generate a Game

Run "python generate-game.py" to randomly generate a Mansion without playing the game. Mansions are created locally under the _mansions directory.

When generating a game you can include one or two optional command line arguments:

- style: "classic" or "sequel" (more about these under "Styles")
- number: how many mansions you want to generate

## Styles

### Classic

The Classic version, a near-replication of the original board game's electronic game companion.

### Sequel

The Sequel version, which was created for this application with the aim of experimenting and creating a version that would be easier to replicate in the browser or otherwise.
In order to optimize the game, we removed some of the gimmicks such as duplicate items (like Black Armchair #1 & #2 that are hard to distinguish and have special features) and odd furniture and room code patterns.
The Sequel plays the same (same interactions, number of furniture items, number of clues, etc) but has different furniture, rooms, and codes.

## Technical Details

This a Python 3 Application. 

The application reads comma-serparated value (.csv) files and writes markdown (.md) files with the game settings.
