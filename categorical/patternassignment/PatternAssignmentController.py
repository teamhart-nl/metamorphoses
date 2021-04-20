from math import *
from itertools import product
import copy

class PatternAssignmentController:

    def __init__(self, allPatterns, patternWidth, patternHeight, gridCoords, minValue, maxValue):
        self.allPatterns = allPatterns
        self.patternWidth = patternWidth
        self.patternHeight = patternHeight
        self.gridCoords = gridCoords
        self.nrObjects = maxValue - minValue

    def assign(self):
        self._getAvailableCells()
        self._getAvailablePatterns()
        self._printAvailability()

        # TODO: actually assign objects to patterns if possible, otherwise give recommendations

    def _getAvailableCells(self):
        """
        Checks for each category if its cells overlap with other categories
        """
        self.originCoords = {}
        self.categoryAvailableCells = {}

        for coords1, c1 in self.gridCoords.items():
            for coords2, c2 in self.gridCoords.items ():
                if (c1 != c2):

                    c1Cells = set(self.__getCategoryCells(coords1))
                    c2Cells = set(self.__getCategoryCells(coords2))

                    c1xMin, c1yMin = self.__getOriginCell(coords1)
                    c2xMin, c2yMin = self.__getOriginCell(coords2)

                    if not (c1 in self.categoryAvailableCells):
                        self.categoryAvailableCells[c1] = c1Cells
                        self.originCoords[c1] = (c1xMin, c1yMin)
                    if not (c2 in self.categoryAvailableCells):
                        self.categoryAvailableCells[c2] = c2Cells
                        self.originCoords[c2] = (c2xMin, c2yMin)

                    overlap = c1Cells.intersection(c2Cells)

                    if len(overlap) > 0:
                        for coord in overlap:
                            if coord in self.categoryAvailableCells[c1]:
                                self.categoryAvailableCells[c1].remove(coord)
                            if coord in self.categoryAvailableCells[c2]:
                                self.categoryAvailableCells[c2].remove(coord)

    def _getAvailablePatterns(self):

        self.categoryAvailablePatterns = {}

        for c, coords in self.categoryAvailableCells.items():
            self.categoryAvailablePatterns[c] = copy.deepcopy(self.allPatterns)

            for pattern in self.allPatterns:
                self.__handlePattern(pattern, c, coords)

    def __handlePattern(self, pattern, c, coords):
        if len(self.categoryAvailablePatterns[c]) == 0:
            raise AssertionError("No available grid cells for a category")

        for i in range(self.patternWidth):
            for j in range(self.patternHeight):

                if (pattern[j][i] == 1) and not ((self.originCoords[c][0] + i, self.originCoords[c][1] + j) in self.categoryAvailableCells[c]):
                    self.categoryAvailablePatterns[c].remove(pattern)
                    return

    def __getCategoryCells(self, coords):
        yCenter = coords[0]
        xCenter = coords[1]

        xMin = xCenter - floor(self.patternWidth / 2)
        xMax = xCenter + floor(self.patternWidth / 2)
        if (self.patternWidth % 2 == 0):
            xMax -= 1

        yMin = yCenter - floor(self.patternHeight / 2)
        yMax = yCenter + floor (self.patternHeight / 2)
        if (self.patternHeight % 2 == 0):
            yMax -= 1

        allCells = list(product(range(xMin, xMax+1), range(yMin, yMax+1)))

        return allCells

    def __getOriginCell(self, coords):
        yCenter = coords[0]
        xCenter = coords[1]

        xMin = xCenter - floor (self.patternWidth / 2)
        yMin = yCenter - floor (self.patternHeight / 2)

        return xMin, yMin

    def _printAvailability(self):
        print()
        for c, patterns in self.categoryAvailablePatterns.items():
            print("For category {}, there are {}/{} patterns available, while nr objects = {}".format(
                    c,
                    len(patterns),
                    len(self.allPatterns),
                    self.nrObjects
            ))
            for p in patterns:
                print(p)
            print("\n")


