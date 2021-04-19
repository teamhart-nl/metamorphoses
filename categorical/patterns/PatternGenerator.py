from itertools import product
import numpy as np

class PatternGenerator:

    def __init__(self):
        pass

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
            pattern = np.reshape(flatPattern, (self.patternWidth, self.patternHeight))
            patterns.append(pattern)

        return patterns

    def _getPatternDimensions(self):
        # TODO: give an option to input pattern dimensions
        self.patternWidth = 2
        self.patternHeight = 2

        # TODO: raise error if w−(wp−1) <= 0 OR h−(hp−1) <= 0



if __name__ == '__main__':
    ps = PatternGenerator().generate()
    for p in ps:
        print(p)
