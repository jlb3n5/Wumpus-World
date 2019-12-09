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
#         Has a map as part of its data. Calls map reset method if player wants to play
#         again
#      5. Main program makes a WumpusWorld object. Handles user input with try and excepts
#         and uses input to call methods and afterward report responses to the user
#
########################
from Map import Map, Cell, OffMapError

class WumpusWorld(object):
    """ contains a map, records player movement & current game state"""
    def __init__(self):
        self.worldmap = Map()
        self.WumpusAlive = True
        self.playerAlive = True
        self.playerHasGold = False
        self.playerHasArrow = True
        self.playerMoves = 0
        self.r = 0
        self.c = 0
        self.playerRowCol = self.worldmap.grid[self.r][self.c]
        
    def stepEast(self):
        self.playerMoves += 1
        self.r += 1
        if 0 <= self.r <= 4:
            self.playerRowCol = self.worldmap.grid[self.r][self.c]
        else:
            self.r -= 1
            print("You feel a bump as you walk into a wall.")
            

    def stepWest(self):       
        self.playerMoves += 1
        self.r -= 1
        if 0 <= self.r <= 4:
            self.playerRowCol = self.worldmap.grid[self.r][self.c]
        else:
            self.r += 1
            print("You feel a bump as you walk into a wall.")
            
            
    def stepSouth(self):
        self.playerMoves += 1
        self.c -= 1
        if 0 <= self.c <= 4:
            self.playerRowCol = self.worldmap.grid[self.r][self.c]
        else:
            self.c += 1
            print("You feel a bump as you walk into a wall.")


    def stepNorth(self):
        self.playerMoves += 1
        self.c += 1
        if 0 <= self.c <= 4:
            self.playerRowCol = self.worldmap.grid[self.r][self.c]
        else:
            self.c -= 1
            print("You feel a bump as you walk into a wall.")

    
    def grab(self,g):
        self.playerMoves += 1
        if g.upper() == "GRAB":
            if self.playerRowCol.hasGold == False:
                print("You do not pick up anything")
            if self.playerRowCol.hasGold == True:
                self.grabGold()
                self.playerRowCol.hasGold = False
                self.playerHasGold = True

    def grabGold(self):
        print("You pick up a pile of gold.")
            

    def fire(self,direction):
        self.playerHasArrow = False
        try:
            if direction.upper() == 'NORTH':
                if self.worldmap.grid[self.r][self.c+1].hasWumpus == True:
                    self.WumpusAlive = False
                    print("You hear a horrible scream")
                if self.worldmap.grid[self.r][self.c+2].hasWumpus == True:
                    self.WumpusAlive = False
                    print("You hear a horrible scream")
                if self.worldmap.grid[self.r][self.c+3].hasWumpus == True:
                    self.WumpusAlive = False
                    print("You hear a horrible scream")
                if self.worldmap.grid[self.r][self.c+4].hasWumpus == True:
                    self.WumpusAlive = False
                    print("You hear a horrible scream")
            if direction.upper() == 'SOUTH':
                if self.worldmap.grid[self.r][self.c-1].hasWumpus == True:
                    self.WumpusAlive = False
                    print("You hear a horrible scream")
                if self.worldmap.grid[self.r][self.c-2].hasWumpus == True:
                    self.WumpusAlive = False
                    print("You hear a horrible scream")
                if self.worldmap.grid[self.r][self.c-3].hasWumpus == True:
                    self.WumpusAlive = False
                    print("You hear a horrible scream")
                if self.worldmap.grid[self.r][self.c-4].hasWumpus == True:
                    self.WumpusAlive = False
                    print("You hear a horrible scream")
            if direction.upper() == 'EAST':
                if self.worldmap.grid[self.r+1][self.c].hasWumpus == True:
                    self.WumpusAlive = False
                    print("You hear a horrible scream")
                if self.worldmap.grid[self.r+2][self.c].hasWumpus == True:
                    self.WumpusAlive = False
                    print("You hear a horrible scream")
                if self.worldmap.grid[self.r+3][self.c].hasWumpus == True:
                    self.WumpusAlive = False
                    print("You hear a horrible scream")
                if self.worldmap.grid[self.r+4][self.c].hasWumpus == True:
                    self.WumpusAlive = False
                    print("You hear a horrible scream")
            if direction.upper() == 'WEST':
                if self.worldmap.grid[self.r-1][self.c].hasWumpus == True:
                    self.WumpusAlive = False
                    print("You hear a horrible scream")
                if self.worldmap.grid[self.r-2][self.c].hasWumpus == True:
                    self.WumpusAlive = False
                    print("You hear a horrible scream")
                if self.worldmap.grid[self.r-3][self.c].hasWumpus == True:
                    self.WumpusAlive = False
                    print("You hear a horrible scream")
                if self.worldmap.grid[self.r-4][self.c].hasWumpus == True:
                    self.WumpusAlive = False
                    print("You hear a horrible scream")                   
        except IndexError:
            OffMapError()

    def canClimb(self):
        self.playerMoves += 1
        if self.playerRowCol == self.worldmap.grid[0][0]:
            print("You climb out of Wumpus World")
            self.playerAlive = False
        else:
            print("You cannot climb up from here")

    def feelBreeze(self):
        if self.playerRowCol.hasBreeze == True:
            print("You feel a breeze.")

    def smellStench(self):
        if self.playerRowCol.hasStench == True:
            print("You smell a terrible stench.")

    def seeGlint(self):
        if self.playerRowCol.hasGold == True:
            print("You see a glint of something that looks like gold.")

    def hasWumpus(self):
        if self.playerRowCol.hasWumpus == True and self.WumpusAlive == True:
            self.playerAlive = False
            print("There is a live Wumpus here!")
            print()
            print("Game Over")
            print("Score is 0")
        if self.playerRowCol.hasWumpus == True and self.WumpusAlive == False:
            print("There is a dead Wumpus here!")
            
    def hasPit(self):
        if self.playerRowCol.hasPit == True:
            self.playerAlive = False
            print("You have fallen into a pit.")
            print()
            print("Game Over")
            print("Score is 0")
            
                
