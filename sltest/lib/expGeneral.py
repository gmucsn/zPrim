from sessionGeneral import *

class Experiment:
    def __init__(self):
        self.Sessions = []
        
        ## Initialization of the actual experiment should always overwrite this!!
        self.path = ""
        self.paramFileTypes = {}
        self.objectNames = []
        self.objectTypes = []

    def populate_params(self,path):
    
        import glob, json
        paramFiles = [name.replace("\\","/") for name in glob.glob(path+"/*.txt")]
        #paramFiles = glob.glob(path+"/*.txt")
        self.paramFiles = paramFiles
        self.paramOptions = {}
        self.testVal = ""
        for filepath in paramFiles:
            obj = {}
            self.testVal = filepath
            f = open(filepath).read()
            obj = json.loads(f)
            try:
                obj = json.loads(f)
            except:
                self.testVal = "json error"
                continue
            self.paramOptions[obj["type"]] = {}
            self.paramOptions[obj["type"]][obj["name"]] = obj
            self.testVal = self.paramOptions[obj["type"]][obj["name"]]["players"]
        
    def registerSession(self,region):
        self.Sessions.append(Session(region))