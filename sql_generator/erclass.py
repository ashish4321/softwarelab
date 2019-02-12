#erclass for keeping state of all objects 

class entity:
	def __init__(self, columns):
		self.ncol = columns
		self.colname = []
		self.coltype = []