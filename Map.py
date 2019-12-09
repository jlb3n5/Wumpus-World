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
#########################
import random

class OffMapError(Exception):
    """Raised if attempt is off the map"""
    def __init__(self):
        pass

class Cell(object):
    """Models one square in the map"""
    def __init__(self):
        self.hasWumpus = self.hasGold = self.hasPit = self.hasBreeze = self.hasStench = False

class Map(object):
    """Manages map, assigns values to cells, reports status of map cells"""
    def __init__(self):
        grid = list()
        for j in range(5):
            row = tuple([Cell() for j in range(5)])
            grid.append(row)
        self.grid = tuple(grid)
        self.reset()

    def onGrid(self, r, c):
        if 0 <= r <= 4 and 0 <= c <= 4:
            return True
        else:
            return False

    def offGrid(self, r, c):
        return not self.OnGrid(r,c)

    def hasWumpus(self, r, c):
        if self.OnGrid(r,c):
            return self.grid[r][c].hasWumpus
        else:
            raise OffMapError()
        
    def isSmelly(self, r, c):
        if self.OnGrid(r,c):
            return self.grid[r][c].hasStench
        else:
            raise OffMapError()
        
    def isBreezy(self, r, c):
        if self.OnGrid(r,c):
            return self.grid[r][c].hasBreeze
        else:
            raise OffMapError()

    def hasPit(self, r, c):
        if self.OnGrid(r,c):
            if not self.grid[0][0]:
                return self.grid[r][c].hasPit
        else:
            raise OffMapError()
    
    def reset(self):
        """Placing the gold, wumpus, and pits"""
        # placing gold
        goldPlaced = False
        while goldPlaced == False:
            coords = (random.randint(0,4), random.randint(0,4))
            if coords != (0,0):
                r = coords[0]
                c = coords[1]
                self.grid[r][c].hasGold = True
                self.grid[r][c].isGlinty = True
                goldPlaced = True
                
        # placing Wumpus        
        wumpusPlaced = False
        while wumpusPlaced == False:
            coords = (random.randint(0,4), random.randint(0,4))
            if coords != (0,0):
                r = coords[0]
                c = coords[1]
                self.grid[r][c].hasWumpus = True
                wumpusPlaced = True

        # placing pits
        for r in range(5):
            for c in range(5):
                pitchance = random.randint(1,11)
                if pitchance <= 2:
                    self.grid[r][c].hasPit = True
                    self.grid[0][0].hasPit = False
                    
        # places with stench
        try:
            for r in range(5):
                for c in range(5):
                    if self.grid[r][c].hasWumpus == True:
                        self.grid[r+1][c].hasStench = True
        except IndexError:
            OffMapError()
            
        try:
            for r in range(5):
                for c in range(5):
                    if self.grid[r][c].hasWumpus == True:
                        self.grid[r][c+1].hasStench = True
        except IndexError:
            OffMapError()
            
        try:
            for r in range(5):
                for c in range(5):
                    if self.grid[r][c].hasWumpus == True:
                        self.grid[r-1][c].hasStench = True
        except IndexError:
            OffMapError()
                        
        try:
            for r in range(5):
                for c in range(5):
                    if self.grid[r][c].hasWumpus == True:
                        self.grid[r][c-1].hasStench = True
        except IndexError: 
            OffMapError()
        
        # places with breeze
        try:
            for r in range(5):
                for c in range(5):
                    if self.grid[r][c].hasPit == True:
                        if self.grid[r][c-1].hasPit == False:
                            self.grid[r][c-1].hasBreeze = True
        except IndexError:
            OffMapError()
            
        try:
            for r in range(5):
                for c in range(5):
                    if self.grid[r][c].hasPit == True:
                        if self.grid[r][c+1].hasPit == False:
                            self.grid[r][c+1].hasBreeze = True
        except IndexError:
            OffMapError()
            
        try:
            for r in range(5):
                for c in range(5):
                    if self.grid[r][c].hasPit == True: 
                        if self.grid[r-1][c].hasPit == False:
                            self.grid[r-1][c].hasBreeze = True
        except IndexError:
            OffMapError()
            
        try:
            for r in range(5):
                for c in range(5):
                    if self.grid[r][c].hasPit == True:
                        if self.grid[r+1][c].hasPit == False:
                            self.grid[r+1][c].hasBreeze = True
        except IndexError: 
            OffMapError()
