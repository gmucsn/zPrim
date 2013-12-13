class Session:
    def __init__(self,region = "??"):
        self.status = "Uninitialized"
        self.region = region
        
    def census(self):
        self.status = "Initialized"
        
    def start(self):
        self.status = "Active"
        
    def stop(self):
        self.status = "Inactive"