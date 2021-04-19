from categorical.mapping2d.RegressionAgent import *
from categorical.mapping2d.GraphAgent import *
from enum import *

class Mapping2dOptions(Enum):
    RegressionAgent = "Regression agent"
    GraphAgent      = "Graph agent"

class Mapping2dController:

    def __init__(self, categories, relationships):
        self.categories = categories
        self.relationships = relationships

        # TODO: make it possible to choose the graph option
        self.mapping2dOption = Mapping2dOptions.RegressionAgent

    def getMapping(self):
        if self.mapping2dOption == Mapping2dOptions.RegressionAgent:
            return RegressionAgent(categories=self.categories, relationships=self.relationships).run()
        # TODO: put GraphAgent here
        print("GraphAgent not implemented yet")
        return RegressionAgent(categories=self.categories, relationships=self.relationships).run()