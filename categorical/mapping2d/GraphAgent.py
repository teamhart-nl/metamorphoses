
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from itertools import combinations
from math import sqrt


class GraphAgent:

    def __init__(self, categories, relationships):
        self.categories = categories
        self.nrCategories = len(categories)
        self.relationships = relationships
        self.idealDistances = self._computeIdealDistance()
        self.distanceLookUp = self._getIdealDistanceLookUp()

        print(self.distanceLookUp)

        if nx.__version__ != '1.11':
            print("please instal networkx version 1.11")
            print("!pip install networkx==1.11")
            
    def run(self):
        G = nx.Graph()

        for i in range(len(self.relationships)):
            for j in range(len(self.relationships[i])):
                if i < j:
                    G.add_edge(self.categories[i], self.categories[j], weight=self.relationships[i][j])
                
        loc = nx.drawing.fruchterman_reingold_layout(G, iterations=100000)

        x = []
        y = []
        print("Point Positions")
        for (name, point) in loc.items():
            print(name, point)
            x.append(point[0])
            y.append(point[1])
        
        print("Result Table")
        errorDF = self._createErrorTable(loc)
        print(errorDF)

        return (x, y)

    def _computeIdealDistance(self):
        """
        Creates a matrix of ideal pairwise distances between categories: d(i,j) = 1 - c(i,j)
        """
        return 1.0 - self.relationships

    def _getIdealDistanceLookUp(self):
        """
        Creates a nested dictionary of ideal pairwise distances between categories
        """
        
        lookup = {}
        for i in range(len(self.idealDistances)):
            from_node = self.categories[i]
            distance_to = {}
            for j in range(len(self.idealDistances[i])):
                distance_to[self.categories[j]] = self.idealDistances[i][j]
            lookup[from_node] = distance_to
        
        return lookup

    def _createErrorTable(self, loc):
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
            p1x, p1y = loc[c1]
            p2x, p2y = loc[c2]

            idealDistance = self.distanceLookUp[c1][c2]
            currDistance = sqrt((p1x - p2x) ** 2 + (p1y - p2y) ** 2)
            distanceError = (currDistance - idealDistance)**2

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