class Region:
    def __init__(self,name,experiment = "N/A"):
        self.name = name
        self.census_uri = ""
        self.load_new(experiment)
        
    def load_new(self,experiment):
        self.experiment = experiment
        self.status = "Uninitialized"

class RegionManager:
    def __init__(self,experimentTypes):
        self.regions = {"TE"+str(i):Region("TE"+str(i)) for i in range(1,17)}
        