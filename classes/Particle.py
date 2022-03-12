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
        for cord in updated_arr:
            if cord[0] == self.pos[0]:
                if cord[1] == self.pos[1]:
                    cord[2] += self.depT
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
        self.f_sensor = [1 + int(math.ceil(math.sin(self.PA+90+45))), 1 + int(math.ceil(math.cos(self.PA+90+45)))]
        self.fL_sensor = [1 + int(math.ceil(math.sin(self.PA+90+90))), 1 + int(math.ceil(math.cos(self.PA+90+45)))]
        self.fR_sensor = [1 + int(math.ceil(math.sin(self.PA+90))), 1 + int(math.ceil(math.cos(self.PA+90+45)))]
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