import math
from random import randint, sample
from scipy import ndimage
from classes.Environment import Environment
from classes.Particle import Particle


def scheduler(steps, size):
    env = Environment(15, size)
    env.spawn()
    for i in range(steps):
        env.deposit_stage()
        env.sensor_stage()
        env.motor_stage()
        if i % 2 != 0:
            env.diffusion_operator()
    print(env.trail_map)

if __name__ == "__main__":
    scheduler(200, 20)
