
import numpy as np
import random as rd
class Field:
    '''Field class
    This class used for generating battle fields. Battle field it's 10x10 matix.
    This class have ships put method to put ships in matrix. Firstly matrix created by zeros
    but when we put ship, coors change to ones.'''
    def __init__(self):
        self.field = np.zeros((10, 10))

    def put_ship(self, length, coords, rotation):
        '''Put ship method. length - int, coords - list from x,y coords, rotation - int
        max length = 4,
        rotations: 0 - horizontal, 1 - vertical
        '''
        raw = coords[0]
        flag = False
        flag2 = False
        if rotation == 0 and length + coords[1] <= 10:
            for i in range(coords[1], length + coords[1]):
                if self.field[coords[0]][i] == 1:
                    return 1
            flag = True
            if flag:
                for i in range(coords[1],length+coords[1]):
                    self.field[coords[0]][i] = 1
            return 0
        elif rotation == 1 and length + coords[0] <= 10:
            for i in range(coords[0], length + coords[0]):
                if self.field[i][coords[1]] == 1:
                    return 1

            flag2 = True
            if flag2:
                for i in range(coords[0],length+coords[0]):
                    self.field[i][coords[1]] = 1
            return 0
        else:
            return 0


    def field_info(self):
        '''Info function to show matrix'''
        return self.field


class Opponent:
    '''Opponent class
    Opponent class that used do generate opponent ships positions and for opponent shootings
    '''
    def __init__(self):
        self.used = []
        self.opfield = Field()
    def shoot(self):
        '''Randon opponent shooting'''
        x1,y1 = rd.randint(0,9), rd.randint(0,9)
        if [x1, y1] not in self.used:
            self.used.append([x1, y1])
        else:
            self.shoot()
        return self.used[-1]


    def prepare_ships(self, pb):

        '''Method that allows generating opponent ships positions'''


        x = rd.randint(0, 9)
        y = rd.randint(0, 9)
        z = rd.randint(0, 1)
        tryed = self.opfield.put_ship(pb, [x, y], z)
        if tryed == 1:
            self.prepare_ships(pb)

        if self.opfield.put_ship(pb, [x, y], z) == None or self.opfield.put_ship(pb, [x, y], z) == 0:
            self.prepare_ships(pb)


        return self.opfield



