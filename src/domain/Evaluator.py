from domain.Filter import Filter
from data import *
import re

class Evaluator():

    config: Config
    cleanDate: Report
    filter : Filter

    def __init__(self, filter: Filter, config: Config, cleanDate: Report):
        self.filter = filter
        self.config = config
        self.cleanDate = cleanDate
    
    # Evaluate folders to clean
    def evaluate(self) -> list:
        filtered = self.filter.evaluate(self.config, self.cleanDate)
        # Filter by date -> list of pathes (now() - lastClean > threshold)
        # Populate list if regex
        return filtered
    