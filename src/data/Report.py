from dataclasses import dataclass

@dataclass 
class Report():
    lastRun : float
    table : dict

    def update(self, folders:list, timeStamp:float):
        self.lastRun = timeStamp
        for folder in folders:
            self.table[folder] = timeStamp