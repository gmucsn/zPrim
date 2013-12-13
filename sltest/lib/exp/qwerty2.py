import expGeneral, threading

class Hellobilly(expGeneral.Experiment):
	def __init__(self):
		self.particular = 1
		self.name = "hello billy!!"

def Experiment():
	return Hellobilly()