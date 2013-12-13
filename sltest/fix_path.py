import os, sys

# Default paths to add
for dir in ['lib','lib\\exp']:
	sys.path.append(os.path.join(os.path.dirname(__file__), dir))
	
def add_path(dir):
    # credit:  Nick Johnson of Google
    sys.path.append(os.path.join(os.path.dirname(__file__), dir))