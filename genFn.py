""" GenFn.py:
Automated generator of generating function to solve given 
integer solution problem
"""
from factors import *
from GeoSeries import *

# class var:
# 	"""Single m_i for an integer solution problem"""
# 	def __init__(self, min_, max_, excluded, step=1):
# 		self._pow = 1
# 		self._inf = _min != None && _max != None

# 		if :
# 			self._inf = True

# 		self._min=min_,self._max=max_
# 		self._exc = excluded



factors = FactorList()

add_f = factors.add_factor
#add_f(GeoSeries(1,1,4))

factors.add_fin_poly(0, 6, 4)
print(factors)

print(factors.solve(9))
print(choose(12, 9))

# 	def __init__(self, ):
