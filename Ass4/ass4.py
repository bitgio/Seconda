import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline as spl
import matplotlib.pyplot as plt


class VoltageData:
        
    def __init__(self, x = [0, 0], y = [0, 0], e = [0, 0]):
        self.times = np.array(x, dtype = 'float64')
        self.voltages = np.array(y, dtype = 'float64')
        self.errors = np.array(e, dtype = 'float64')
        self.values = np.stack((self.times, self.voltages, self.errors), axis = 1)
      
    def parse_line(self, path):
        t, v, e = [], [], []
        with open(path) as data_file:
            for line in data_file:
                if not line.startswith('#'):
                    values = line.strip('\n').split(' ')
                    t.append(float(values[0]))
                    v.append(float(values[1]))
                    e.append(float(values[2]))
        self.times = np.array(t, dtype = 'float64')
        self.voltages = np.array(v, dtype = 'float64')
        self.errors = np.array(e, dtype = 'float64')
        self.values = np.stack((self.times, self.voltages, self.errors), axis = 1)          
        
    def __len__(self):
        return len(self.values)
    
    def __iter__(self):
        return iter(self.values)
    
    def __repr__(self, index):
        return (f'{index}, {self.values[index]}')
    
    def __call__(self, time, order):
        spline = spl(self.times, self.voltages, order)
        return spline(time)
    
    def debug_repr(self):
        for value in self.values:
            print(value)
            
    def plot(self, ax, rangex, rangey, colour):
        fig, bx = plt.subplots(1, ax)
        bx.set_xlim(rangex[0], rangex[1])
        bx.set_ylim(rangey[0], rangey[1])
        bx.set_xlabel('times')
        bx.set_ylabel('voltages')
        bx.plot(self.times, self.voltages, colour)
        

if __name__ == '__main__':
    volt = VoltageData(np.ones(3), y = np.zeros(3), e = np.zeros(3))
    print(type(volt.times))
    print(volt.values[:, 0:1])