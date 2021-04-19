import pandas as pd
from math import *
from itertools import combinations
import copy
import matplotlib.pyplot as plt

class RegressionAgent:

    def __init__(self, categories, relationships):
        self.categories = categories
        self.nrCategories = len(categories)
        self.relationships = relationships

        self.learningRate = 0.05
        self.maxEpochs = 200

    def run(self):
        self.idealDistances = self._computeIdealDistance()
        self.x, self.y = self._initialPlacing()
        mses = []
        xs = [self.x]
        ys = [self.y]

        for epoch in range(self.maxEpochs):
            self.errorDf = self._createErrorTable(x=self.x, y=self.y)
            mse = self._getMSE(self.errorDf)
            mses.append(mse)

            if (epoch % 10 == 0):
                print ("Epoch", epoch)

            if len(mses) > 1:
                if mse > mses[-2]:
                    print("MSE is bigger than previous at epoch", epoch)
                    print("Error DF:\n", self.errorDf)
                    #self._plotCategories(self.x, self.y)
                    #self._plotMSEs(mses)
                    return xs[-2], ys[-2]

            self.largestContributor = self._findLargestErrorContributor()
            self._adjustCoordinates()
            xs.append(self.x)
            ys.append(self.y)

        #self._plotCategories(self.x, self.y)
        #self._plotMSEs(mses)
        return self.x, self.y


    def _computeIdealDistance(self):
        """
        Creates a matrix of ideal pairwise distances between categories: d(i,j) = 1 - c(i,j)
        """
        return 1.0 - self.relationships

    def _initialPlacing(self):
        """
        Places categories on a plane with a deterministic function
        f(c[i]) = (0, i/2)
        """
        return [0 for _ in range(self.nrCategories)], [i / 2.0 for i in range(self.nrCategories)]

    def _createErrorTable(self, x, y):
        """
        Creates a sorted table of pairwise distance different between current and ideal positions
        """
        errorDf = pd.DataFrame (columns=[
                "ideal-distance",
                "curr-distance",
                "error",
                "involved-categories"
        ])

        for c1, c2 in combinations(self.categories, r=2):
            p1x, p1y = self.__getPositionOf(c1, x, y)
            p2x, p2y = self.__getPositionOf(c2, x, y)

            idealDistance = self.__getIdealDistanceBetween(c1, c2)
            currDistance = self.__getCurrDistanceBetween(idealDistance, p1x, p1y, p2x, p2y)
            distanceError = self.__getDistanceError(idealDistance, currDistance)

            errorDf = errorDf.append (
                    {
                            "ideal-distance"     : idealDistance,
                            "curr-distance"      : currDistance,
                            "error"              : distanceError,
                            "involved-categories": c1 + "," + c2
                    },
                    ignore_index=True)

        errorDf = errorDf.sort_values(by=["error"], ascending=False).reset_index(drop=True)
        return errorDf

    def __getIndexOf(self, category):
        """
        Extracts the position of a catgory in the categories array
        """
        return self.categories.index(category)

    def __getPositionOf(self, category, x, y):
        """
        Extracts the current position of a category on a plane
        """
        index = self.__getIndexOf(category)
        return x[index], y[index]

    def __getIdealDistanceBetween(self, c1, c2):
        """
        Extracts the ideal distance between 2 categories
        """
        index1 = self.__getIndexOf(c1)
        index2 = self.__getIndexOf(c2)

        return self.idealDistances[index1][index2]

    def __getCurrDistanceBetween(self, idealDistance, p1x, p1y, p2x, p2y):
        """
        Calculates current distance between 2 categories
        """
        return sqrt ((p1x - p2x) ** 2 + (p1y - p2y) ** 2)

    def __getDistanceError(self, idealDistance, currDistance):
        """
        Outputs the squared difference betwen the current positions of 2 points and their ideal distance
        """
        return (currDistance - idealDistance) ** 2

    def _findLargestErrorContributor(self):
        """
        Determines the category that contributes to the error the most
        """
        cumErrors = self.__findCumulativeErrors()
        largestContributer = max(cumErrors, key=cumErrors.get)

        return largestContributer

    def __findCumulativeErrors(self):
        """
        Calculates total error for each category
        """
        cumErrors = {}
        dfSize = self.errorDf.shape[0]

        for i in range (dfSize):
            involvedCategories = str(self.errorDf.loc[i, "involved-categories"]).split (",")

            for category in involvedCategories:
                currErrorContribution = self.errorDf.loc[i, "error"] * (dfSize - i)

                if category in cumErrors:
                    cumErrors[category] += currErrorContribution
                else:
                    cumErrors[category] = currErrorContribution

        return cumErrors

    def _adjustCoordinates(self):
        """
        Adjusts the coordinate of the largest contributing category to the error
        """

        # finding the new position for lc
        lcIndex = self.__getIndexOf(self.largestContributor)
        xOffset, yOffset = self.__findBestOffsets(lcIndex)
        self.x[lcIndex] += xOffset
        self.y[lcIndex] += yOffset

    def __findBestOffsets(self, lcIndex):
        """
        Determines the best direction and corresponding offset for a category
        Best means minimal mse
        """
        dTheta = 0.05
        theta = 0

        mses = []

        xp = copy.deepcopy(self.x)
        yp = copy.deepcopy(self.y)

        # noinspection PyTypeChecker
        for i in range (floor (2 * pi / dTheta) + 1):
            currErrorDf = self._createErrorTable(x=xp, y=yp)
            mse = self._getMSE(currErrorDf)
            mses.append (mse)

            xp[lcIndex] = self.x[lcIndex] + self.learningRate * cos(theta)
            yp[lcIndex] = self.y[lcIndex] + self.learningRate * sin(theta)

            theta += dTheta

        minIndex = mses.index(min (mses))
        bestTheta = dTheta * (minIndex - 1)
        return self.learningRate * cos(bestTheta), self.learningRate * sin(bestTheta)

    def _getMSE(self, errorDf):
        """
        Calculates MSE
        """
        return sum(errorDf["error"]) / errorDf.shape[0]

    def _plotCategories(self, x, y):
        fig, ax = plt.subplots(figsize=(4, 4))

        ax.scatter(x, y, lw=10, c="#8800ff")
        c = 0
        for i, j in zip(x, y):
            text = self.categories[c] + "=(" + str(round (i, 2)) + ', ' + str(round (j, 2)) + ")"
            ax.text(i, j, text)
            c += 1
        ax.set_xlim([min(x) - 0.1, max (x) + 0.1])
        ax.set_ylim([min(y) - 0.1, max (y) + 0.1])

        plt.show()

    def _plotMSEs(self, mses):
        fig, ax = plt.subplots(figsize=(10, 2))
        ax.plot(mses, lw=3, c="#8800ff")
        plt.title("MSE evolution")

        plt.show()
