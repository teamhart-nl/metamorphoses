from categorical.relationships.ManualRelationshipHandler import *
from categorical.relationships.NaturalOccurenceHandler import *
from enum import *

class RelationshipOptions(Enum):
    ManualHandler           = "Manual handler"
    NaturalOccurentHandler  = "Natural Occurence handler"

class RelationshipController:
    def __init__(self, categories):
        self.categories = categories

        # TODO: make it possible to choose the option
        self.relationshipOption = RelationshipOptions.ManualHandler

    def determineRelationships(self):
        if self.relationshipOption == RelationshipOptions.ManualHandler:
            return ManualRelationshipHandler(categories=self.categories).input()
        # TODO: put NaturalOccurenceHandler here
        print("NaturalOccurenceHandler not implemented yet")
        return ManualRelationshipHandler(categories=self.categories).input()