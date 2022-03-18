import math
from random import randint, sample
from scipy import ndimage
from classes.Environment import Environment
from classes.Particle import Particle


def scheduler(steps, size):
    env = Environment(15, size)
    env.spawn()
    for i in range(steps-1):
        env.motor_stage()
        env.deposit_stage()
        env.sensor_stage()
        print(env.particle_map())


if __name__ == "__main__":
    scheduler(200, 20)
