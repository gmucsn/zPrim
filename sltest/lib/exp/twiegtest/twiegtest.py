## Note: I mulled over whether object names should be an external parameter or not and decided against it - this may need to be changed in the future. The object names don't need to match the actual inworld names, however they do need to match *something* the app IDs them by.

import expGeneral, expObj

class obj_box(expObj.Object):
    def __init__(self,num):
        self.id = num
        self.address = ""

class Twiegtest(expGeneral.Experiment):
    def __init__(self, path):
        self.Sessions = []
        self.path = path
        self.name = "Twiegtest"
        self.objects = self.initializeObjects()
        
    def initializeObjects(self): # Keeping this long just to be safe.
        objects = {}
        for n in range(1,51):
            objects["Box "+str(n)] = obj_box(n)

def Experiment(path, **kwargs):
    return Twiegtest(path)