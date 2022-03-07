import math
from random import randint, sample
import numpy as np
from matplotlib import pyplot as plt
from scipy import ndimage
import matplotlib.animation as animation


class Environment:
    def __init__(self, pp, width, height):
        self.pp = pp
        self.width = width
        self.height = height
        self.area = width * height
        self.particles = []
        self.trail_map = []
        self.particle_map = []
        for i, ii in zip(self.trail_map, self.particle_map):
            i, ii = 0, 0

    def spawn(self):
        for i in range(int(self.area / self.pp)):
            pos_x = randint(self.width / 2 * -1, self.width / 2)
            pos_y = randint(self.height / 2 * -1, self.height / 2)
            p = Particle([pos_x, pos_y], 5)
            self.particles.append(p)

    def deposit_stage(self):
        for particle in self.particles:
            self.trail_map = particle.deposit_trail(self.trail_map)

    def motor_stage(self):
        for particle in self.particles:
            particle.move()

    def sensor_stage(self):
        for particle in sample(self.particles, 200):
            particle.make_sensors()


    def diffusion_operator(self, const=0.6, sigma=2):
        """
        applies a Gaussian filter to the entire trail map, spreading out chemoattractant
        const multiplier controls decay rate (lower = greater rate of decay, keep <1)
        Credit to: https://github.com/ecbaum/physarum/blob/8280cd131b68ed8dff2f0af58ca5685989b8cce7/species.py#L52
        """""
        self.trail_map = const * ndimage.gaussian_filter(self.trail_map, sigma)

class Particle:
    def __init__(self, pos: list, RA:int,  depT:int=5, SS:int=1, SO:int=9, PA=0):
        """
        :param pos: position, [x, y]
        :param depT: deposition amount of chemoattractant per step
        :param SS: step size
        :param RA: particle rotation angle
        :param SO: sensor offset
        :param PA: Particle Angle
        """
        self.pos = pos
        self.depT = depT
        self.SS = SS
        self.RA = RA
        self.PA = PA
        self.y = 1
        self.x = 0
        self.f_sensor = pos
        self.fL_sensor = pos
        self.fR_sensor = pos
        self.sensors = [self.f_sensor, self.fR_sensor, self.fL_sensor]
        self.SO = SO

    def deposit_trail(self, arr):
        """
        param arr: trail map
        return: updated trail map
        """
        updated_arr = arr
        updated_arr[0][self.pos[0]] += self.depT
        updated_arr[1][self.pos[1]] += self.depT
        return updated_arr

    def move(self):
        if self.PA == 90:
            self.pos[self.y] += self.SS
        elif self.PA == 45:
            self.pos[self.x] += self.SS
            self.pos[self.y] += self.SS
        elif self.PA == 360:
            self.pos[self.x] += self.SS
        elif self.PA == 305:
            self.pos[self.x] += self.SS
            self.pos[self.y] -= self.SS
        elif self.PA == 260:
            self.pos[self.y] -= self.SS
        elif self.PA == 225:
            self.pos[self.x] -= self.SS
            self.pos[self.y] -= self.SS
        elif self.PA == 180:
            self.pos[self.x] -= self.SS
        elif self.PA == 135:
            self.pos[self.x] -= self.SS
            self.pos[self.y] += self.SS

    def make_sensors(self):
        self.f_sensor = [1 + int(math.ceil(math.sin(self.RA+90+45))), 1 + int(math.ceil(math.cos(self.RA+90+45)))]
        self.fL_sensor = [1 + int(math.ceil(math.sin(self.RA+90+90))), 1 + int(math.ceil(math.cos(self.RA+90+45)))]
        self.fR_sensor = [1 + int(math.ceil(math.sin(self.RA+90))), 1 + int(math.ceil(math.cos(self.RA+90+45)))]
        self.sensors = [self.fL_sensor, self.f_sensor, self.fR_sensor]

    def sense(self):
        fL, f, fR = self.sensors

        if f > fL and f > fR:
            pass
        elif f < fL and f < fR:
            if randint(1, 2) == 1:
                self.PA += self.RA
            else:
                self.PA -= self.RA
        elif fL < fR:
            self.PA -= self.RA
        elif fR < fL:
            self.PA += self.RA
        else:
            pass

def scheduler(steps):
    """
    :param steps: amount of times the program runs
    """
    env = Environment(15, 200, 200)
    env.spawn()
    for i in range(steps):
        env.deposit_stage()
        env.motor_stage()
        env.sensor_stage()
        env.diffusion_operator()
        print(env.trail_map)

if __name__ == "__main__":
    scheduler(200)
