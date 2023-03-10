import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline as spl
import matplotlib.pyplot as plt


class VoltageData:
        
    def __init__(self, x = [0, 0], y = [0, 0], e = [0, 0]):
        self.times = np.array(x, dtype = np.float64)
        self.voltages = np.array(y, dtype = np.float64)
        if len(self.times) == len(e):
            self.errors = np.array(e, dtype = np.float64)
        else:
            self.errors = np.zeros(len(self.times))
        self._values = np.stack((self.times, self.voltages, self.errors), axis = 1)
    
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
        spline = spl(self.times, self.voltages, k = order)
        return spline(time)
    
    def __repr__(self):
        s = ''
        for i in range(len(self._values)):
            s += (f'{i}: {self._values[i, 0]} {self._values[i, 1]} {self._values[i, 2]}\n')
        return s
    
    def debug_repr(self):
        for value in self._values:
            print(value)
            
    '''def plot(self, ax, rangex, rangey, colour):
        fig, bx = plt.subplots(1, ax)
        bx.set_xlim(rangex[0], rangex[1])
        bx.set_ylim(rangey[0], rangey[1])
        bx.set_xlabel('times')
        bx.set_ylabel('voltages')
        bx.plot(self.times, self.voltages, colour)'''
        

if __name__ == '__main__':
    volt = VoltageData.parse_line('sample_data_file_with_errs.txt')
    print(volt(5., 3))