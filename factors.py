from GeoSeries import *
import numbers

class FactorList:
	def __init__(self):
		self._binomials = []
		self._geometrics = []
		self._outside_coeff = 1
		self._outside_x = 0

	def __repr__(self):
		return str(self)

	def __str__(self):
		return ("" if self._outside_x == 0 else "x ^ %d * " % self._outside_x) + " * ".join(map(str, self.all_facts()))

	def all_facts(self):
		return self._binomials+self._geometrics

	def add_factor(self, factor):
		"""Adding in a factor to the list of factor. Currently
		only implemented for binomial expansions and closed-form geometric 
		series."""

		#f_list: the list of factors that is of the same type as the one we want\
		if(isinstance(factor, Series)):
			if(isinstance(factor, GeoSeries)):
				f_list = self._geometrics
			elif(isinstance(factor, BinExp)):
				f_list = self._binomials
		else:
			return NotImplementedError

		i=0

		# Skips over factors where x is raised to a higher power.
		while (i < len(f_list) and factor.x_pwr() < f_list[i].x_pwr()):
			i+=1

		# Goes through linearly based on the exponent of x, sees if the factor already exists.
		while (i < len(f_list) and factor.x_pwr() == f_list[i].x_pwr()):

			#If factor with like terms exists, multiply them together.
			if f_list[i].canMult(factor):
				var = f_list[i] * factor
				f_list[i] = f_list[i] * factor
				return
			i += 1

		f_list.insert(i, factor)
	
	def inclConst(self, coeff):
		self._outside_coeff *= coeff

	def add_outside_x(self, expo):
		self._outside_x += expo

	def add_fin_poly(self, min_x, max_x, poly_expo = 1, skip = 1, excl = []):
		"""Min: lowest power of x, max: highset power of x, poly_expo:
		what power the polynomial is raised to"""

		#factor out minimum value of x
		self.add_outside_x(min_x * poly_expo)
		max_x -= min_x
		min_x = 0

		count = min_x//skip + 1 # how many nonzero terms in polynomial

		self.add_factor(BinExp(-1, skip * (max_x+1), poly_expo))
		self.add_factor(GeoSeries(1, skip, poly_expo))



	def solve(self, which_coeff):
		"""go from arbitrarily long list of factors to desired coefficient"""
		def recurSolve(desired, lst):
			"""Recursively solve for all coefficients"""
			if(desired < 0):
				return 0
			if(lst==None):
				lst=self.all_facts()
			if(len(lst)==0):
				return 0

			get_curr_coeff, pwr = lst[0].get_solve_fn(), lst[0].x_pwr()

			if(len(lst)==1):
				return self._outside_coeff * get_curr_coeff(desired)

			else:
				res=0
				doneZero=False
				for i in range(0, desired + 1, lst[0].x_pwr()):
					res += get_curr_coeff(i) * recurSolve(desired - i, lst[1:])
				return res


		which_coeff -= self._outside_x
		return recurSolve(which_coeff,self.all_facts())
		




	def add_binexp(factor):
		pass
		





