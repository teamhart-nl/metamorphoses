from enum import *

class CategoriesInputType(Enum):
    Manual      = "Manual"
    Automatic   = "Automatic"

class CategoricalInputHandler:

    def __init__(self):
        # TODO: make an option to choose manual
        self.inputType = CategoriesInputType.Automatic

    def input(self):
        if self.inputType == CategoriesInputType.Automatic:
            return self._automaticCategories()
        else:
            return self._manualCategories()

    def _manualCategories(self):
        # TODO: make a user input a list of categories
        return self._automaticCategories()

    def _automaticCategories(self):
        return ["A", "B", "C", "D"]


if __name__ == '__main__':
    categories = CategoricalInputHandler().input()
    print("categories:", categories)