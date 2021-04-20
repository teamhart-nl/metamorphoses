from categorical.patterns.PatternGenerator import *
from categorical.CategoriesInputHandler import *
from categorical.relationships.RelationshipController import *
from categorical.mapping2d.Mapping2dController import *
from categorical.areaassignment.AreaAssignmentController import *
from categorical.patternassignment.PatternAssignmentController import *

class CategoricalMapper:

    def __init__(self, gridWidth, gridHeight, minValue, maxValue):

        self.gridWidth = gridWidth
        self.gridHeight = gridHeight

        self.minValue = minValue
        self.maxValue = maxValue

    def map(self):

        patternGenerator = PatternGenerator(gridWidth=self.gridWidth, gridHeight=self.gridHeight)
        self.patterns = patternGenerator.generate()
        self.patternWidth, self.patternHeight = patternGenerator.getPatternDimensions()

        self.categories = CategoricalInputHandler().input()
        print("categories:\n", self.categories)

        self.relationships = RelationshipController(categories=self.categories).determineRelationships()
        print("relationships:")
        [print(self.relationships[i]) for i in range(len(self.relationships))]

        self.mapX, self.mapY = Mapping2dController(categories=self.categories,
                                                   relationships=self.relationships).getMapping()
        self.gridCoords = AreaAssignmentController(
                categories=self.categories,
                gridWidth=self.gridWidth,
                gridHeight=self.gridHeight,
                patternWidth=self.patternWidth,
                patternHeight=self.patternHeight,
                rawX=self.mapX,
                rawY=self.mapY
        ).assign()

        print(self.gridCoords)

        PatternAssignmentController(
                allPatterns=self.patterns,
                patternWidth=self.patternWidth,
                patternHeight=self.patternHeight,
                gridCoords=self.gridCoords,
                minValue=self.minValue,
                maxValue=self.maxValue
        ).assign()



        

