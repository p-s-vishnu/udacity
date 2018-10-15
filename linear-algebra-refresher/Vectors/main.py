from vector import Vector

#test equal
test_vec		= Vector((1,2,3))
test_vec1		= Vector((1,2,3))
# print('Check if equal : ', test_vec == test_vec1)

# Add operation
a = Vector((8.218, -9.341))
b = Vector((-1.129, 2.111))
# print('Sum of 2 Vec :', a.add_vector(b))

# Subtract
c = Vector((7.119, 8.215))
d = Vector((-8.223, 0.878))
# print('Diff of 2 Vec :', c.sub_vector(d))

# Scalar mul
# print('Scalar mul :', d.mul_vector(2))

# magnitude
e = Vector((-0.221, 7.437))
f = Vector((8.813, -1.331, -6.247))
# print(e,e.magnitude())
# print(f,f.magnitude())

# normalization
g = Vector((5.581, -2.136)) 
h =	Vector((1.996, 3.108, -4.554))
# print(g,g.normalization())
# print(h.normalization())

# Dot product (Inner product)
v1 = Vector((7.887, 4.138))
w1 = Vector((-8.802, 6.776))
# print(v1.dot_product(w1))

v2 = Vector((-5.955, -4.904, -1.874))
w2 = Vector((-4.496, -8.755, 7.103))
# print(v2.dot_product(w2))

# Angle in radians
v = Vector((3.183, -7.627))
w = Vector((-2.668, 5.319))
print(v.angle_in_rad(w))

# Angle in degree
v = Vector((7.35, 0.221, 5.188))
w = Vector((2.751, 8.259, 3.985))
print(v.angle_in_degree(w))