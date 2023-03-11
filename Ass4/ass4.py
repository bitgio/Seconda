import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline as spl
import matplotlib.pyplot as plt


class VoltageData:
        
    def __init__(self, x = [0, 0], y = [0, 0], e = [0, 0]):
        self._times = np.array(x, dtype = np.float64)
        self._voltages = np.array(y, dtype = np.float64)
        if len(e) == len(self._times):
            self._errors = np.array(e, dtype = np.float64)
        else:
            self._errors = np.zeros(len(self._times))
        self._values = np.stack((self._times, self._voltages, self._errors), axis = 1)
    
    @property
    def times(self):
        return self._times
    
    @property
    def voltages(self):
        return self._voltages
    
    @property
    def errors(self):
        return self._errors
    
    @classmethod  
    def parse_line(cls, path):
        times, voltages, errors = np.loadtxt(path, unpack = True)
        return cls(times, voltages, errors)
    
    def __getitem__(self, index):
        return self._values[index]
    
    def __len__(self):
        return len(self._values)
    
    def __iter__(self):
        return iter(self._values)
    
    def __call__(self, time, order):
        spline = spl(self._times, self._voltages, k = order)
        return spline(time)
    
    def __repr__(self):
        s = ''
        for i in range(len(self._values)):
            s += (f'{i}: {self._values[i, 0]} {self._values[i, 1]} {self._values[i, 2]}\n')
        return s
    
    def debug_repr(self):
        for value in self._values:
            print(value)
            
    def plot(self, ax = None, tit = '', rangex = [None, None], rangey = [None, None], colour = None):
        plt.axes(arg = ax, xlabel = 'times', title = tit, xlim = (rangex[0], rangex[1]), ylabel = 'voltages', ylim = (rangey[0], rangey[1]))
        plt.errorbar(self._times, self._voltages, yerr = self._errors, ecolor = colour, fmt = 'o')
        plt.show()        


if __name__ == '__main__':
    #x = np.array([1., 2., 3., 4., 5.])
    #y = np.random.rand(5)
    #v = VoltageData(x, y)
    v = VoltageData.parse_line('sample_data_file_with_errs.txt')
    print(v(5., 3))
    v.plot(tit = 'Prova')