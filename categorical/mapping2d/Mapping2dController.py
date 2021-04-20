from categorical.mapping2d.RegressionAgent import *
from categorical.mapping2d.GraphAgent import *
from enum import *

class Mapping2dOptions(Enum):
    RegressionAgent = "Regression agent"
    GraphAgent      = "Graph agent"

class Mapping2dController:

    def __init__(self, categories, relationships, agent=Mapping2dOptions.RegressionAgent):
        self.categories = categories
        self.relationships = relationships

        self.mapping2dOption = agent

    def getMapping(self):
        if self.mapping2dOption == Mapping2dOptions.RegressionAgent:
            return RegressionAgent(categories=self.categories, relationships=self.relationships).run()
        elif self.mapping2dOption == Mapping2dOptions.GraphAgent:
            return GraphAgent(categories=self.categories, relationships=self.relationships).run()
        else:
            raise ValueError("Unrecognized mapping agent")