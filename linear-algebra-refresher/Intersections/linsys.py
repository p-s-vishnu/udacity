from decimal import Decimal, getcontext
from copy import deepcopy

import sys
sys.path.append('D:/Github/udacity/linear-algebra-refresher/Vectors')
from vector import Vector
from plane import Plane

getcontext().prec = 30


class LinearSystem(object):

    ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG = 'All planes in the system should live in the same dimension'
    NO_SOLUTIONS_MSG = 'No solutions'
    INF_SOLUTIONS_MSG = 'Infinitely many solutions'

    def __init__(self, planes):
        try:
            d = planes[0].dimension
            for p in planes:
                assert p.dimension == d

            self.planes = planes
            self.dimension = d

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)


    def swap_rows(self, row1, row2):
        swap[row1], swap[row2] = swap[row2], swap[row1]


    def multiply_coefficient_and_row(self, coefficient, row):
        normal      = self.normal_vector
        constant    = self.constant_term

        self[row] = Plane(normal_vector = normal.mul_vector(coefficient), constant_term = constant * coefficient)

    def add_multiple_times_row_to_row(self, coefficient, row_to_add, row_to_be_added_to):
        n1, k1  = self[row_to_add].normal_vector        , self[row_to_add].constant_term
        n2, k2  = self[row_to_be_added_to].normal_vector, self[row_to_be_added_to].constant_term

        new_n   = n1.mul_vector(coefficient).add_vector(n2)
        new_k   = (k1 * coefficient) + k2

        self[row_to_be_added_to] = Plane(normal_vector = new_k, constant_term = new_n)

    def compute_triangular_form(self):
        system = deepcopy(self)

        m = len(system)
        n = system.dimension

        j = 0
        for i in range(m):
            while j < n:
                c = MyDecimal(system[i].normal_vector[j])
                if c.is_near_zero():
                    swap_success = system.swap_with_below_if_able(i,j) 
                    if not swap_success:
                        j += 1
                        continue

                    system.clear_coeff_below(i,j)
                    j += 1
                    break
        return system

    def swap_with_below_if_possible(self, row, col) :
        num_equations = len(self)

        for k in range(row+1, num_equations):
            coefficient = MyDecimal(self[k].normal_vector[col])
            if not coefficient.is_near_zero():
                self.swap_rows(row, k)
                return True

        return False

    def clear_coeff_below(self, row, col):
        n = len(self)
        beta = MyDecimal(self[row].normal_vector[col])

        for k in range(row+1, num_equations):
            n = self[k].normal_vector
            gamma = n[col]
            alpha = -gamma/beta
            self.add_multiple_times_row_to_row(alpha, row, k)

    def compute_rref(self):
        tf = self.compute_triangular_form()

        return tf
        
    def indices_of_first_nonzero_terms_in_each_row(self):
        num_equations = len(self)
        num_variables = self.dimension

        indices = [-1] * num_equations

        for i,p in enumerate(self.planes):
            try:
                indices[i] = p.first_nonzero_index(p.normal_vector)
            except Exception as e:
                if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                    continue
                else:
                    raise e

        return indices


    def __len__(self):
        return len(self.planes)


    def __getitem__(self, i):
        return self.planes[i]


    def __setitem__(self, i, x):
        try:
            assert x.dimension == self.dimension
            self.planes[i] = x

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)


    def __str__(self):
        ret = 'Linear System:\n'
        temp = ['Equation {}: {}'.format(i+1,p) for i,p in enumerate(self.planes)]
        ret += '\n'.join(temp)
        return ret


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps


p0 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
p1 = Plane(normal_vector=Vector(['0','1','0']), constant_term='2')
p2 = Plane(normal_vector=Vector(['1','1','-1']), constant_term='3')
p3 = Plane(normal_vector=Vector(['1','0','-2']), constant_term='2')

s = LinearSystem([p0,p1,p2,p3])

print (s.indices_of_first_nonzero_terms_in_each_row())
print ('{},{},{},{}'.format(s[0],s[1],s[2],s[3]))
print (len(s))
print (s)

s[0] = p1
print (s)

print (MyDecimal('1e-9').is_near_zero())
print (MyDecimal('1e-11').is_near_zero())