from categorical.areaassignment.ScalingAgent import *
from enum import *

class AssignmentOptions(Enum):
    ScalingAgent = "Scaling agent"

class AreaAssignmentController:

    def __init__(self, categories, gridWidth, gridHeight, patternWidth, patternHeight, rawX, rawY):
        self.categories = categories
        self.gridWidth = gridWidth
        self.gridHeight = gridHeight
        self.patternWidth = patternWidth
        self.patternHeight = patternHeight
        self.x = rawX
        self.y = rawY

        self.assignmentOption = AssignmentOptions.ScalingAgent

    def assign(self):
        return ScalingAgent(
                categories=self.categories,
                gridWidth=self.gridWidth,
                gridHeight=self.gridHeight,
                patternWidth=self.patternWidth,
                patternHeight=self.patternHeight,
                rawX=self.x,
                rawY=self.y).assign()


