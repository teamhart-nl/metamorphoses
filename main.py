from categorical.CategoricalMapper import *
from enum import *

class DataType(Enum):
    Categorical = "Categorical"
    Numerical   = "Numerical"

if __name__ == '__main__':

    # TODO: make it possible to just enter this stuff
    gridWidth = 6
    gridHeight = 4

    # TODO:: make it possible to have different ranges for different categories (within categorical input prolly)
    minValue = 0
    maxValue = 5

    # TODO: make a user choose if they want to do numerical or categorical
    dataType = DataType.Categorical

    if dataType == DataType.Categorical:
        CategoricalMapper(
                gridWidth=gridWidth,
                gridHeight=gridHeight,
                minValue=minValue,
                maxValue=maxValue
        ).map()
    else:
        print("Numerical isn't implemented yet")


