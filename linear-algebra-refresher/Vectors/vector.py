from math import sqrt, acos, pi
from decimal import Decimal

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
		if self.is_zero() or new_vector.is_zero():
			return 0
		return sum([i*j for i,j in zip(self.coordinates, new_vector.coordinates)])

	def angle_in_rad(self, new_vector):
		dot_value	= self.dot_product(new_vector)
		mag_v		= self.magnitude()
		mag_w		= new_vector.magnitude()
		# arc cosine - acos
		if self.is_zero() or new_vector.is_zero():
			return 0
		return acos(dot_value / (mag_v * mag_w))

	def angle_in_degree(self, new_vector):
		angle_rad	= self.angle_in_rad(new_vector)
		scalar		= 180. / pi
		return scalar * angle_rad

	def is_orthogonal(self, new_vector):
		return self.dot_product(new_vector) == 0 or self.is_zero() or new_vector.is_zero()

	def is_parallel(self, new_vector):
		angle_0		= (self.angle_in_degree(new_vector)  == 0)
		angle_180	= (self.angle_in_degree(new_vector)  == 180)

		return self.is_zero() or new_vector.is_zero() or angle_0 or angle_180

	def is_zero(self):
		return self.coordinates == 0