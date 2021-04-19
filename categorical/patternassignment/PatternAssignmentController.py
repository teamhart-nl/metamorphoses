
class PatternAssignmentController:

    def __init__(self, patterns, minValue, maxValue):
        self.allPatterns = patterns
        self.minValue = minValue
        self.maxValue = maxValue

        # TODO: get available patterns out of all and see how they correspond to range