class Car:
	def __init__(self,speed,unit):
		self.ms=speed
		self.su=unit
	def __str__(self):
		str1="Car with maximum speed of {} {}"
		return str1.format(self.ms.self.su)
class Boat:
	def __init__(self,speed):
		self.ms=speed
	def __str__(self):
		str1="Boat with the maximum speed of {} knots"
		return str1.format(self.ms)
