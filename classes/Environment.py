class Environment:
    def __init__(self, pp, size):
        self.pp = pp
        self.size = size
        self.area = size**2
        print(self.area)
        self.particles = []
        self.trail_map = [[0, 0, 0] for i in range(size)]


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
            particle.sense()


    def diffusion_operator(self, const=0.6, sigma=2):
        """
        applies a Gaussian filter to the entire trail map, spreading out chemoattractant
        const multiplier controls decay rate (lower = greater rate of decay, keep <1)
        Credit to: https://github.com/ecbaum/physarum/blob/8280cd131b68ed8dff2f0af58ca5685989b8cce7/species.py#L52
        """""
        self.trail_map = const * ndimage.gaussian_filter(self.trail_map, sigma)