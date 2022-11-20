from data import *
from datetime import datetime, timedelta

class Filter():

    currentTime: datetime

    # datetime.datetime.fromtimestamp(timeStamp)
    def __init__(self, currentTime: datetime):
        self.currentTime = currentTime
    
    def evaluate(self, config: Config, report: Report) -> list:
        # Filter by date -> list of pathes (now() - lastClean > threshold)
        folders = list()

        for item in config.items:
            for entity in item.entities:
                if entity in report.table:
                    lastDirCleanup = datetime.fromtimestamp(report.table[entity])
                    if self.passDeltaThreshold(lastDirCleanup, item.delta):
                        folders.append(entity)
                else:
                    folders.append(entity)

        return folders

    def passDeltaThreshold(self, time: datetime, delta: timedelta) -> bool:
        return self.currentTime - time > delta