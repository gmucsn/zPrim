#import glob

#__all__ = [name.split("\\")[1][0:-3] for name in glob.glob("./exp/*.py") if "__init__" not in name]
__all__ = ["twiegtest"]
#__all__ = []
#print os.walk("/exp")
#print str([name[0:-3] for name in os.listdir("/exp")])
#print str([name[0:-3] for name in os.listdir("/exp") if (name.endswith(".py") and "__init__" not in name)])

#__all__ = [name[0:-3] for name in os.listdir("/exp") if (name.endswith(".py") and "__init__" not in name)]