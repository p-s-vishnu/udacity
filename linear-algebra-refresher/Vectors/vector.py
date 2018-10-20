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
		return Vector([i-j for i,j in 
					zip(self.coordinates,new_vector.coordinates)])

	def mul_vector(self, scalar):
		return Vector([ i*scalar for i in self.coordinates ])

	def magnitude(self):
		return sqrt(sum([i**2 for i in self.coordinates]))

	# Unit vector
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

	# A zero vector is both parallel and perpendicular to other vector
	def is_zero(self):
		return self.coordinates == 0

	# Vector 		= Vprojection + Vperpendicular
	# Projection 	= V . B_hat
	def projection(self, b):
		try:
			u 		= b.normalization()
			scalar	= self.dot_product(u)
			return u.mul_vector(scalar)
		except Exception as e:
			raise e


	# Vperpendicular= Vector - Vprojection
	def perpendicular(self, b):
		try:
			v_proj = self.projection(b)
			return self.sub_vector(v_proj)
		except Exception as e:
			raise e

	# Cross product 
	# Area of parallelogram = ||v||*||w|| sin(Theta)
	# Verification of cross product, multiply each cross product with 
	# each vectors, correct if result is zero
	
	def cross_product_3D(self, w):
		z1	= self.coordinates[1]*w.coordinates[2] - self.coordinates[2]*w.coordinates[1]
		z2	= self.coordinates[2]*w.coordinates[0] - self.coordinates[0]*w.coordinates[2]
		z3	= self.coordinates[0]*w.coordinates[1] - self.coordinates[1]*w.coordinates[0]
		return Vector((z1, z2, z3))

	def area_of_parallelogram(self, b):
		return self.cross_product_3D(b).magnitude()