from math import sqrt, acos, pi

class Vector(object):

	def __init__(self, coordinates):
		try:
			if not coordinates:
				raise ValueError
			self.coordinates	= coordinates
			self.dimension		= len(coordinates)
			
		except ValueError:
			raise ValueError('The coordinates must be non empty')
			
		except TypeError:
			raise TypeError('The coordinates must be iterable')
	
	def __str__(self):
		return 'Vector : {}'.format(self.coordinates)

	def __eq__(self, coordinates):
		return self.coordinates == coordinates

	def add_vector(self, new_vector):
		return [i+j for i,j in 
			zip(self.coordinates,new_vector.coordinates)]

	def sub_vector(self, new_vector):
		return [i-j for i,j in 
			zip(self.coordinates,new_vector.coordinates)]

	def mul_vector(self, scalar):
		return [ round(i*scalar, 3) for i in self.coordinates ]

	def magnitude(self):
		return sqrt(sum([i**2 for i in self.coordinates]))

	def	normalization(self):
		m = self.magnitude()
		return self.mul_vector(1/m)

	def dot_product(self, new_vector):
		if self.coordinates == 0 or new_vector.coordinates == 0:
			return 0
		return round(sum([i*j for i,j in zip(self.coordinates, new_vector.coordinates)]), 3)

	def angle_in_rad(self, new_vector):
		dot_value	= self.dot_product(new_vector)
		mag_v		= self.magnitude()
		mag_w		= new_vector.magnitude()
		# arc cosine - acos
		return acos(dot_value / (mag_v * mag_w))

	def angle_in_degree(self, new_vector):
		angle_rad	= self.angle_in_rad(new_vector)
		scalar		= 180 / pi
		return scalar * angle_rad