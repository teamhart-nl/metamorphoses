from categorical.patterns.PatternGenerator import *
from categorical.CategoriesInputHandler import *
from categorical.relationships.RelationshipController import *
from categorical.mapping2d.Mapping2dController import *
from categorical.assignment.AreaAssignmentController import *

class CategoricalMapper:

    def __init__(self, gridWidth, gridHeight):

        self.gridWidth = gridWidth
        self.gridHeight = gridHeight

    def map(self):

        patternGenerator = PatternGenerator()
        self.patterns = patternGenerator.generate()
        self.patternWidth, self.patternHeight = patternGenerator.getPatternDimensions()

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



        

