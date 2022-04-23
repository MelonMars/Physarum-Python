import math
from random import randint, sample
from scipy import ndimage
from classes.Environment import Environment
from classes.Particle import Particle

nsteps = 0


def scheduler(steps, size):
    global nsteps
    env = Environment(15, size)
    env.spawn()
    while nsteps < steps:
        env.motor_stage()
        env.deposit_stage()
        env.sensor_stage()
        nsteps += 1


if __name__ == "__main__":
    nsteps += 1
    scheduler(200, 20)
