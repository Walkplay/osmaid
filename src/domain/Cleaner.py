import os
import shutil

class Cleaner():

    pathCollection:list

    def __init__(self, pathCollection:list):
        self.pathCollection = pathCollection
    
    def clean(self):

        for path in self.pathCollection:
            if not os.path.exists(path):
                continue
            
            print(f"Clean {path}")
            if os.path.isfile(path):
                os.remove(path)
            elif os.path.isdir(path):
                try:
                    shutil.rmtree(path, False, self.onError)        
                except FileExistsError as exc:
                    print(exc)

    def onError(self, func, path, exc_info):

        pass