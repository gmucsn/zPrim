## This should keep track of all experiments that can be run.

import importlib, glob, sys, os
import fix_path

class ExperimentManager:
    def __init__(self):
        root = os.path.dirname(__file__)
        self.test = glob.glob(root+"/*.py")
        self.expTypes = [name.split("\\")[-1][0:-3] for name in glob.glob(root+"/exp/*/*.py")]
        self.experiments = {}
        for type in self.expTypes: # The imports will probably create scoping issues later since they're not global, I'll deal with that when the time comes. Probably be having the initialization return something to the global space that will give details on what to import.
            print type
            fix_path.add_path('lib\\exp\\'+type)
            print sys.path
            importlib.import_module(type)
            newexp = sys.modules[type].Experiment("./lib/exp/"+type)
            self.experiments[newexp.name] = newexp
        for experiment in self.experiments.itervalues(): # Add subdirectories for each 
            experiment.populate_params(experiment.path)