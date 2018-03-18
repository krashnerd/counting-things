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
        return ((desired % self._x_pwr) == 0)

    def get_factors(self, max):
        i=0
        while(i < max):
            yield self.coeff(i * self.x_pwr())
            i+=1

    def string_terms(self):
        def incl_expo(expo):
            return (" ^ %d" % expo if expo != 1 else "")

        return (str(abs(self._x_coeff))
         if abs(self._x_coeff) != 1 else "",incl_expo(self._x_pwr),incl_expo(self._pwr))



class BinExp(Series):
    def __init__(self, x_coeff, x_pwr, self_pwr):
        Series.__init__(self,x_coeff, x_pwr, self_pwr)
    
    def __str__(self):
        return "((1 " + oppoSign(-1 * self.x_coeff())+ " %sx%s)%s)" % self.string_terms()

    def get_solve_fn(self):

        xcoeff, xpwr, selfpwr, envchoose = (self._x_coeff,
            self._x_pwr, self._pwr, choose)

        def f(desired):
            if desired%xpwr != 0:
                return 0
            adj_term=desired//xpwr
            return int(math.pow(xcoeff,adj_term)) * envchoose(selfpwr,adj_term)

        return f

    def coeff(self, desired):
        if not (self.coeff_exists(desired)):
            return 0
        adj_term = desired // self._x_pwr

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

    def get_solve_fn(self):
        xcoeff = self._x_coeff
        xpwr = self._x_pwr
        selfpwr = self._pwr

        def fn(desired):
            if(desired%xpwr != 0):
                return 0
            choose_coeff = desired // xpwr
            return int(math.pow(xcoeff,
                choose_coeff)) * intSol(selfpwr, choose_coeff)

        return fn









    def coeff(self, desired):
        if not (self.coeff_exists(desired)):
            return 0
        else:
            choose_coeff = desired // self._x_pwr
            return int(math.pow(self._x_coeff,
                choose_coeff)) * intSol(self._pwr, choose_coeff)
