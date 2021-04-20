import copy
from math import *
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class ScalingAgent:

    def __init__(self, categories, gridWidth, gridHeight, patternWidth, patternHeight, rawX, rawY):
        self.categories = categories
        self.gridWidth = gridWidth
        self.gridHeight = gridHeight
        self.patternWidth = patternWidth
        self.patternHeight = patternHeight
        self.x = rawX
        self.y = rawY

    def assign(self):
        self._movePointsToGridCells()

        if len(self.dictCoords.items()) != len(self.categories):
            raise AssertionError("Some categories overlap on the grid")

        return self.dictCoords

    def _movePointsToGridCells(self):
        """
        Assigns categories to grid cells
        """
        self.__getScaledBoundingBox ()

        self.gridX = [round(i) + 1 for i in self.x]
        self.gridY = [round(j) + 1 for j in self.y]

        self.coords = [(self.gridY[i], self.gridX[i]) for i in range (len (self.x))]
        self.dictCoords = {}
        for i in range (len (self.categories)):
            self.dictCoords[self.coords[i]] = self.categories[i]

        self.__plotGrid()

    def __getScaledBoundingBox(self):
        """
        Prepares points to be places in grid areas
        """
        self.workingGridWidth = self.gridWidth - 1
        self.workingGridHeight = self.gridHeight - 1
        pointsWidth = abs(max(self.x) - min(self.x))
        pointsHeight = abs(max(self.y) - min(self.y))

        isHorizontalGrid = True if (self.workingGridWidth >= self.workingGridHeight) else False
        isHorizontalPlot = True if (pointsWidth >= pointsHeight) else False

        if isHorizontalGrid != isHorizontalPlot:
            self.x, self.y = self.__rotatePoints(self.x, self.y)
            pointsWidth = abs(max(self.x) - min(self.x))
            pointsHeight = abs(max(self.y) - min(self.y))

        self.x, self.y = self.__transformPoints(pointsWidth, pointsHeight)

    def __rotatePoints(self, x, y):
        """
        Rotates all points by 90 degrees
        """
        return y, x

    def __moveToZero(self, q):
        """
        Moves coordinates so that the minimal one is 0
        """
        minCoord = min(q)
        for i in range (len(q)):
            q[i] -= minCoord
        return q

    def __transformPoints(self, pointsWidth, pointsHeight):
        """
        Scales points so that they're kinda positioned on plane with the same dims as the grid
        """
        movedX = copy.deepcopy(self.x)
        movedY = copy.deepcopy(self.y)

        if min(self.x) != 0:
            movedX = self.__moveToZero(self.x)
        if min(self.y) != 0:
            movedY = self.__moveToZero(self.y)

        availableGridWidth = self.workingGridWidth - self.patternWidth + 1
        availableGridHeight = self.workingGridHeight - self.patternHeight + 1

        scaledX = [i * (availableGridWidth / pointsWidth) + floor(self.patternWidth / 2) for i in movedX]
        scaledY = [j * (availableGridHeight / pointsHeight) + floor(self.patternHeight / 2) for j in movedY]

        return scaledX, scaledY

    def __plotGrid(self):
        heatmap = [[1 if ((j, i) in self.coords) else 0 for i in range (1, self.gridWidth + 1)] for j in
                   range (1, self.gridHeight + 1)]
        annot = np.asarray (
                [[self.dictCoords[(j, i)] if ((j, i) in self.dictCoords) else "" for i in range (1, self.gridWidth + 1)] for j in
                 range (1, self.gridHeight + 1)])
        # So Sweet you are <3
        fig, ax = plt.subplots(figsize=(self.gridWidth, self.gridHeight))
        sns.heatmap(heatmap,
                    annot=annot,
                    vmin=0,
                    vmax=1,
                    cmap=["#ffffff", "#8800ff"],
                    square=False,
                    cbar=False,
                    xticklabels=False,
                    yticklabels=False,
                    fmt="",
                    linewidths=1,
                    linecolor="#8800ff",
                    ax=ax)
        ax.invert_yaxis()

        fig.show()

