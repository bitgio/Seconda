
class Particle:

    def __init__(self, mass, charge, name, momentum = 0.):
        self._mass = float(mass)
        self._charge = float(charge)
        self._name = str(name)
        self._momentum = float(momentum)

    @property
    def mass(self):
        return self._mass

    @property
    def charge(self):
        return self._charge

    @property
    def name(self):
        return self._name

    @property
    def momentum(self):
        return self._momentum

    @property
    def energy(self):
        return (self._momentum**2 + self._mass**2)**(1/2)

    @property
    def beta(self):
        return abs(self._momentum / self._mass)

    @property
    def gamma(self):
        return (1 - self.beta**2)**(-1/2)

    @momentum.setter
    def momentum(self, momentum):
        if momentum >= 0:
            self._momentum = momentum
        else:
            print('Momentum must be set positive.')

    @energy.setter
    def energy(self, energy):
        if energy >= abs(self._mass):
            self._momentum = (energy**2 - self._mass**2)**(1/2)
        else:
            print('This value is not physical: energy must be set positive and larger than the value of the mass.')

    @beta.setter
    def beta(self, beta):
        if beta >= 0 and beta < 1:
            self._momentum = beta * self._mass
        else:
            print('This value is not physical: beta must be set between 0 and 1.')

    @gamma.setter
    def gamma(self, gamma):
        if gamma >= 1:
            self._momentum = self._mass * (1 - gamma**(- 2))**(1/2)
        else:
            print('This value is not physical: gamma must be set larger than 1.')

    def info(self):
        print(f'The mass of {self._name} is {self._mass} MeV/c^2, its charge {self._charge} C. Its momentum is {self._momentum} MeV/c, its energy {self.energy} MeV/c^2. Its beta is {self.beta} and its gamma is {self.gamma}.')

                                                

class Alpha(Particle):
    def __init__(self, momentum = 0.):
        Particle.__init__(self, 3727.379, 2, 'α', momentum)


class Proton(Particle):
    def __init__(self, momentum = 0.):
        Particle.__init__(self, 938.272, 1, 'p', momentum)
        
        
if __name__ == '__main__':
    p = Proton(5.0)
    print(p.gamma)