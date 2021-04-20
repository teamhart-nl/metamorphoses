
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


class GraphAgent:

    def __init__(self, categories, relationships):
        self.categories = categories
        self.nrCategories = len(categories)
        self.relationships = relationships
        self.idealDistances = self._computeIdealDistance()

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
        for (name, point) in loc.items():
            print(name, point)
            x.append(point[0])
            y.append(point[1])
        
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
            lookup[self.categories[i]] = distance_to
        
        return lookup