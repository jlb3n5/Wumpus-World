#########################
#
# CS 101
# Program 8
# Justin Balino
# jlb3n5@mail.umkc.edu
#
# Problem: Write a puzzle game, called Wumpus World
#
# Algorithm:
#      1. Help menu of what actions can be used and what format.
#      2. Cell class model one square in the map.
#      3. Map class contains a 2-dimensional list of Cells; methods: isBreezy, isSmelly
#         hasWumpus, hasPit, reset. Anything off the map raises an OffMapError
#      4. WumpusWorld class plays a game of WumpusWorld. Keeps track of player location,
#         and info like whether the player has fired the crossbow or grabbed the gold.
#         Has a map as part of its data.
#      5. Main program makes a WumpusWorld object. Handles user input with try and excepts
#         and uses input to call methods and afterward report responses to the user
#
########################
# Game Summary
print("Game Summary")
print()
print("Wumpus World is a 5x5 grid, with cells numbered from 0,0 to 4,4. The player always starts")
print("in the lower left-hand corner (cell 0,0), and the starting cell is always safe. Somewhere")
print("(randomly placed anywhere but 0,0) is the Wumpus, a fierce beast, does not move, that will")
print("eat the player if that cell is entered. Somewhere is a pile of gold, which the player is")
print("trying to receive. About 20% of the squares (other than 0,0) are pits; stepping into a pit")
print("means the player dies (loses the game). The player has a crossbow, but only one arrow. If")
print("the player shoots, the arrow will travel in a straight line until it hits a wall, or the")
print("Wumpus.")
print()
print()
# Player Senses
print("Player Senses")
print()
print("If there is a pit in an adjacent cell, the player will feel a breeze.")
print("If the Wumpus is in an adjacent cell, the player will smell a stench.")
print("If the gold is in the same cell as the player, the player will notice a glint.")
print("If the player tries walking off the edge of the map, the player will hit a wall and feel")
print("a bump, but not actually move.")
print("If the player successfully shoots the Wumpus, the Wumpus will emit a scream that can be")
print("heard from anywhere in Wumpus World")
print()
print()
# Game Actions
print("Game Actions")
print()
print("The following actions all counts as a move.")
print("North | South | East | West : Move one square in specified direction")
print("Grab : If the player is in the square with the gold, this picks up the gold")
print("Fire [direction] : Where [direction] is exactly one of North, South, East, West:")
print("fire the arrow in the specified direction.")
print("Climb : If the player is at 0,0, this takes the player out of Wumpus World, with or")
print("without the gold, and ends the game. No effect if anywhere else")
print()
print()
# Game Scoring
print("Game Scoring")
print()
print("+1000 Climbed out with gold")
print("+100 Climbed out without gold")
print("-10 Fired weapon")
print("-1 per move")
print("Score 0 if the player died")
print()
print()

from Map import Map, Cell, OffMapError
from Wumpus import WumpusWorld

W = WumpusWorld()
score = 0
W.feelBreeze()
W.smellStench()
while W.playerAlive == True:
    choice = input("> ")
    if choice.upper() == "NORTH":
        W.stepNorth()
        W.seeGlint()
        W.feelBreeze()
        W.smellStench()
        W.hasWumpus()
        W.hasPit()
    if choice.upper() == "SOUTH":
        W.stepSouth()
        W.seeGlint()
        W.feelBreeze()
        W.smellStench()
        W.hasWumpus()
        W.hasPit()
    if choice.upper() == "EAST":
        W.stepEast()
        W.seeGlint()
        W.feelBreeze()
        W.smellStench()
        W.hasWumpus()
        W.hasPit()
    if choice.upper() == "WEST":
        W.stepWest()
        W.seeGlint()
        W.feelBreeze()
        W.smellStench()
        W.hasWumpus()
        W.hasPit()
    if choice.upper() == "CLIMB":
        W.canClimb()
        if W.playerHasGold == True and W.playerHasArrow == True and W.playerRowCol == W.worldmap.grid[0][0]:
            print()
            print("Game Over")
            print("Score: ",(score+1000-W.playerMoves))
            W.playerAlive = False
        if W.playerHasGold == True and W.playerHasArrow == False and W.playerRowCol == W.worldmap.grid[0][0]:
            print()
            print("Game Over")
            print("Score: ",(score+1000-W.playerMoves-10))
            W.playerAlive = False
        if W.playerHasGold == False and W.playerHasArrow == True and W.playerRowCol == W.worldmap.grid[0][0]:
            print()
            print("Game Over")
            print("Score: ",(score+100-W.playerMoves))
            W.playerAlive = False
        if W.playerHasGold == False and W.playerHasArrow == False and W.playerRowCol == W.worldmap.grid[0][0]:
            print()
            print("Game Over")
            print("Score: ",(score+100-W.playerMoves-10))
    if choice.upper() == "FIRE NORTH":
        if W.playerHasArrow == False:
            print("You try to fire but are out of arrows")
            W.playerMoves += 1
        if W.playerHasArrow == True:
            W.fire("North")
    if choice.upper() == "FIRE SOUTH":
        if W.playerHasArrow == False:
            print("You try to fire but are out of arrows")
            W.playerMoves += 1
        if W.playerHasArrow == True:
            W.fire("South")
    if choice.upper() == "FIRE EAST":
        if W.playerHasArrow == False:
            print("You try to fire but are out of arrows")
            W.playerMoves += 1
        if W.playerHasArrow == True:
            W.fire("East")
    if choice.upper() == "FIRE WEST":
        if W.playerHasArrow == False:
            print("You try to fire but are out of arrows")
            W.playerMoves += 1
        if W.playerHasArrow == True:
            W.fire("West")
    if choice.upper() == "GRAB":
        W.grab("grab")



