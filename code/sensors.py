"""

class for sensor blocks

"""

class Sensor:
	def __init__(self, location):
		# whether sensor is activated
		self.activated = False
		# store its own location
		self.location = location
		# store locations of surrounding blocks
		# to check if should be activated
		d = [-1, 0, 1]
		self.surround = []
		for dx in d:
			for dy in d:
				for dz in d:
					self.surround.append((location[0] + dx, 
						location[1] + dy, location[2] + dz))

	def check_status(self, circuit, elech):
		for i in self.surround:
			if i in circuit and circuit[i] == elech:
				self.activated = True
