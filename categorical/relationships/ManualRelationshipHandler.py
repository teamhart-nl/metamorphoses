from enum import *
from random import *
import numpy as np

class CategoriesInputType(Enum):
    Manual  = "Manual"
    Random  = "Random"

class ManualRelationshipHandler:

    def __init__(self, categories):
        self.categories = categories

        # TODO: make an option to choose manual
        self.inputType = CategoriesInputType.Random

    def input(self):
        if self.inputType == CategoriesInputType.Random:
            return self._randomRelationships()
        return self._manualRelationships()

    def _randomRelationships(self):
        nrCategories = len(self.categories)
        relationships = [[0.0 for _ in range(nrCategories)] for _ in range(nrCategories)]

        for i in range(nrCategories):
            for j in range(nrCategories):
                if (i == j):
                    relationships[i][j] = 1.0
                else:
                    relationships[i][j] = round(uniform(0.1, 0.9), 2)
                    relationships[j][i] = relationships[i][j]

        return np.array((relationships))

    def _manualRelationships(self):
        # TODO: make a user input similarities
        return self._randomRelationships()


if __name__ == '__main__':
    relationships = ManualRelationshipHandler(categories=["A", "B", "C", "D"]).input()
    print("relationships:")
    for i in range(len(relationships)):
        print(relationships[i])





