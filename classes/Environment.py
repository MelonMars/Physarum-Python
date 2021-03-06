from random import randint, sample
from scipy import ndimage
from classes.Particle import Particle


class Environment:
    def __init__(self, pp, size):
        self.pp = pp
        self.size = size
        self.area = size ** 2
        self.particles = []
        self.trail_map = []
        for i in range(size):
            for ii in range(size):
                self.trail_map.append([i, ii, 0])

    def spawn(self):
        for i in range(int(self.area / self.pp)):
            pos_x = randint(0, self.size)
            pos_y = randint(0, self.size)
            p = Particle([pos_x, pos_y], randint(0, 360))
            self.particles.append(p)

    def deposit_stage(self):
        for particle in self.particles:
            self.trail_map = particle.deposit_trail(self.trail_map)

    def motor_stage(self):
        for particle in self.particles:
            particle.move()

    def sensor_stage(self):
        for particle in sample(self.particles, self.size):
            particle.make_sensors(self.trail_map)
            particle.sense()

    def particle_map(self):
        particle_map = []
        for particle in self.particles:
            particle_map.append([particle.pos, particle.PA])
        return particle_map

    """
        def diffusion_operator(self, const=0.6, sigma=2):
    
        applies a Gaussian filter to the entire trail map, spreading out chemoattractant
        const multiplier controls decay rate (lower = greater rate of decay, keep <1)
        Credit to: https://github.com/ecbaum/physarum/blob/8280cd131b68ed8dff2f0af58ca5685989b8cce7/species.py#L52
        
        self.trail_map = const * ndimage.gaussian_filter(self.trail_map, sigma)
    """
