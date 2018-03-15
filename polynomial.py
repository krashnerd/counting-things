import math
fct = math.factorial

def choose(x, y):
	return fct(x)//(fct(y)*fct(x-y))

def intSol(factors, wanted):
	return choose(factors + wanted - 1, wanted)

# class Term:
# 	def __init__(self, coeff, pwr):
# 		self._coeff=coeff
# 		self._pow=pwr

# 	def __add__(self, other):
# 		if !isinstance(other, Term):
# 			return NotImplemented
# 		if self._pow==other._pow:
# 			return [Term(self._coeff+other._coeff,self._pwr)]
# 		else:
# 			return [self, other]

# 	def __sub__(self, other):
# 		if !isinstance(other, Term):
# 			return NotImplemented

# 	def __mul__(self, other):
# 		if !isinstance(other, Term):
# 			return NotImplemented

# 	def __div__(self, other):
# 		if !isinstance(other, Term):
# 			return NotImplemented

class GeoSeries:
	def __init__(self, x_coeff, x_pwr, self_pwr):
		self._x_coeff=x_coeff
		self._x_pwr=x_pwr
		self._pwr=self_pwr

	def canMult(self, other):
		return isinstance(other, GeoSeries) && other._x_pwr == self._x_pwr

	# def __add__(self, other_geo):
	# 	if isinstance

	def coeff(self, desired):
		if desired % self._x_pwr != 0:
			return 0
		else:
			choose_coeff = desired // self._x_pwr
			return x_coeff * intSol(self._pwr, choose_coeff) 

# class Poly:
# 	def __init__(self):
# 		geo_series = []
# 		finSums = []

# 	def 

# class finite_sum()
