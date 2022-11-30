import numpy as np
import scipy.stats as ss
from scipy.interpolate import InterpolatedUnivariateSpline as sp

'''--- Goal
Create a ProbabilityDensityFunction class that is capable of throwing
preudo-random number with an arbitrary distribution.

(In practice, start with something easy, like a triangular distribution---the
initial debug will be easier if you know exactly what to expect.)


--- Specifications
- the signature of the constructor should be __init__(self, x, y), where
  x and y are two numpy arrays sampling the pdf on a grid of values, that
  you will use to build a spline
- [optional] add more arguments to the constructor to control the creation
  of the spline (e.g., its order)
- the class should be able to evaluate itself on a generic point or array of
  points
- the class should be able to calculate the probability for the random
  variable to be included in a generic interval
- the class should be able to throw random numbers according to the distribution
  that it represents
- [optional] how many random numbers do you have to throw to hit the
  numerical inaccuracy of your generator?'''

class ProbabilityDensityFunction:
    '''
    '''

    def __init__(self, x, y, order):
        '''Constructor'''
        if type(x) == 'numpy.ndarray' and type(y) == 'numpy.ndarray':
            self.x = x
            self.y = y
        
        self.order = order

    def pdf(self, point):
        probability = sp(self.x, self.y, k = self.order)
        return probability(point)
    
    def cdf(self, point1, point2):
        if point2 > point1:
            return sp.integral(point1, point2)
        else:
            return sp.integral(point2, point1)
    
    def random_numbers(self, how_many_random_points, beginning, end):
        rnd = (beginning - end) * np.random.random_sample - beginning
        output = np.array()
        if pdf(rnd) <= 
        return np.random.random_sample()


class TriangularDistribution(ProbabilityDensityFunction):
    '''
    '''

    def __init__(self):
        self.x = ProbabilityDensityFunction(x)
        self.y = ss.triang(ProbabilityDensityFunction(y))




if __name__ == '__main__':
    x = np.linspace(-1., 1., 100)
    y = ss.triang(x)
    ejemplo=  ProbabilityDensityFunction.random_numbers(x, y)
