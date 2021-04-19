from categorical.CategoriesInputHandler import *
from categorical.relationships.RelationshipController import *
from categorical.mapping2d.Mapping2dController import *
from categorical.assignment.AreaAssignmentController import *

class CategoricalMapper:

    def __init__(self, gridWidth, gridHeight, patternWidth, patternHeight):

        self.gridWidth = gridWidth
        self.gridHeight = gridHeight

        self.patternWidth = patternWidth
        self.patternHeight = patternHeight

    def map(self):
        self.categories = CategoricalInputHandler().input()
        print("categories:\n", self.categories)

        self.relationships = RelationshipController(categories=self.categories).determineRelationships()
        print("relationships:")
        [print(self.relationships[i]) for i in range(len(self.relationships))]

        self.mapX, self.mapY = Mapping2dController(categories=self.categories,
                                                   relationships=self.relationships).getMapping()
        self.gridX, self.gridY = AreaAssignmentController(
                categories=self.categories,
                gridWidth=self.gridWidth,
                gridHeight=self.gridHeight,
                patternWidth=self.patternWidth,
                patternHeight=self.patternHeight,
                rawX=self.mapX,
                rawY=self.mapY
        ).assign()

        # TODO: allocate patterns



        

