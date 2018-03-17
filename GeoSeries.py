import math

def choose(x, y):
	fct = math.factorial
	if(y > x):
		return 0
	return fct(x)//(fct(y)*fct(x-y))

def intSol(factors, wanted):
	return choose(factors + wanted - 1, wanted)

def oppoSign(num):
	return ('+' if num < 1 else '-')

class Series:
	def __init__(self, x_coeff, x_pwr, self_pwr):
		self._x_coeff=x_coeff
		self._x_pwr=x_pwr
		self._pwr=self_pwr

	def __repr__(self):
		return str(self)

	def x_pwr(self):
		return self._x_pwr

	def x_coeff(self):
		return self._x_coeff

	def pwr(self):
		return self._pwr

	def coeff_exists(self, desired):
		return ((desired % self._x_coeff) == 0)

	def get_factors(self, max):
		i=0
		while(i < max):
			yield self.coeff(i * self.x_pwr())
			i+=1

	def string_terms(self):
		def inclExpo(expo):
		 	return (" ^ %d" % expo if expo != 1 else "")
		return (str(abs(self._x_coeff))
		 if abs(self._x_coeff) != 1 else "",inclExpo(self._x_pwr),inclExpo(self._pwr))


class BinExp(Series):
	def __init__(self, x_coeff, x_pwr, self_pwr):
		Series.__init__(self,x_coeff, x_pwr, self_pwr)
	
	def __str__(self):
		return "((1 " + oppoSign(-1 * self.x_coeff())+ " %sx%s)%s)" % self.string_terms()



	def coeff(self, desired):
		if not (self.coeff_exists(desired)):
			return 0
		adj_term = choose_coeff = desired // self._x_pwr

		if adj_term > self._pwr:
			return 0

		return int(math.pow(self._x_coeff,
			adj_term)) * choose(self._pwr,adj_term)

 	def canMult(self, other):
		return (isinstance(other, BinExp) and other._x_pwr == self._x_pwr
			and other._x_coeff == self._x_coeff)



	def __mul__(self, other):
		if self.canMult(other):
			return BinExp(self._x_coeff, self._x_pwr, self._pwr+other._pwr)
		else:
			return NotImplemented

class GeoSeries(Series):

	def __init__(self, x_coeff, x_pwr, self_pwr):
		Series.__init__(self,x_coeff, x_pwr, self_pwr)

	def canMult(self, other):
		return (isinstance(other, GeoSeries) and other._x_pwr == self._x_pwr
			and other._x_coeff == self._x_coeff)

	def __str__(self):
		return "((1 / (1 "+oppoSign(self.x_coeff()) + " %sx%s))%s)" % self.string_terms()

	def __mul__(self, other):
		if self.canMult(other):
			return GeoSeries(self._x_coeff, self._x_pwr, self._pwr+other._pwr)
		else:
			return NotImplemented

	# def __add__(self, other_geo):
	# 	if isinstance

	def coeff(self, desired):
		if not (self.coeff_exists(desired)):
			return 0
		else:
			choose_coeff = desired // self._x_pwr
			return int(math.pow(self._x_coeff,
				choose_coeff)) * intSol(self._pwr, choose_coeff)

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



# class Poly:
# 	def __init__(self):
# 		geo_series = []
# 		finSums = []

# 	def 

# class finite_sum()
