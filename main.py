from categorical.CategoricalMapper import *
from enum import *

class DataType(Enum):
    Categorical = "Categorical"
    Numerical   = "Numerical"

if __name__ == '__main__':

    gridWidth = 5
    gridHeight = 5

    patternWidth = 2
    patternHeight = 2

    # TODO: make a user choose if they want to do numerical or categorical
    dataType = DataType.Categorical

    if dataType == DataType.Categorical:
        CategoricalMapper(
                gridWidth=gridWidth,
                gridHeight=gridHeight,
                patternWidth=patternWidth,
                patternHeight=patternHeight
        ).map()
    else:
        print("Numerical isn't implemented yet")


