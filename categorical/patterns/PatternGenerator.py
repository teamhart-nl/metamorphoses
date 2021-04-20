from itertools import product
import numpy as np

class PatternGenerator:

    def __init__(self, gridWidth, gridHeight):
        self.gridWidth = gridWidth
        self.gridHeight = gridHeight

    def generate(self):
        self._getPatternDimensions()
        return self._getAllPermutations()
        # TODO: add capabilities for more grid params (like intensity, timinds etc)

    def getPatternDimensions(self):
        return self.patternWidth, self.patternHeight

    def _getAllPermutations(self):
        """
        For now assumes firing motors at the same time with the same intensity for the same amount of time
        """
        patternLen = self.patternWidth * self.patternHeight
        patterns = []

        for flatPattern in product([1,0], repeat=patternLen):
            if not sum(flatPattern) == 0:
                pattern = np.reshape(flatPattern, (self.patternHeight, self.patternWidth))
                patterns.append(pattern.tolist())

        return patterns

    def _getPatternDimensions(self):
        # TODO: give an option to input pattern dimensions
        self.patternWidth = 3
        self.patternHeight = 2

        # TODO: raise error if w−(wp−1) <= 0 OR h−(hp−1) <= 0
        if (self.gridWidth - (self.patternWidth-1) <= 0) or (self.gridHeight - (self.patternHeight-1) <= 0):
            print("The pattern is too big for the grid")



if __name__ == '__main__':
    ps = PatternGenerator().generate()
    for p in ps:
        print(p)
