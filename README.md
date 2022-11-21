# Chess tournament

## General

This program is a **chess tournament manager**. It helps to create matches using
the **swiss tournament system.** The display is in french but the code is in english. It can easily be translated.

Several tournament can be created. For a tournament to be played, it needs 8
players. 
You can either create the player independently from the tournament, or create 
them directly in the tournament.

There is a list of player that is independent of the tournament list.

## Usage

When you first start the application, the player list and the tournament list is empty.

I advise that you first create the tournament, and then create the played inside of the tournament. Doing so, the players will also be added to the player database.

When 8 players are added to the tournament you can start it. The first round will be generated using the elo of the players. 

After you have inserted the result of the match (0, 0.5 or 1), the second round will be displayed.

You can go on until the tournament is over.  (4 rounds in this case)

The result will be displayed when the match is over.

## Reports

Different reports are available :

- List of all players
    - in alphabetical order
    - by ranking
- List of all players in a tournament :
    - by alphabetical order
    - by ranking
- List of all tournaments.
- List of all rounds of a tournament.
- List of all matches of a tournament.

## Database

You can save at any point the state of the application. For example after round 3 you can save the program and do the round 4 another day by reloading the save.
The database used is a tinyDB. The serialization is used to store all the information.

