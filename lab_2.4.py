import math as mt

class Ball():
    def __init__(self,rad):
        self.rad = rad
    def serch_s(self):
        return 4 * mt.pi * mt.pow(self.rad,2)
    def serch_v(self):
        return 4/3 * mt.pi * mt.pow(self.rad,3)

ball = Ball(4)
print('Площать шара', ball.serch_s())
print('Объем шара', ball.serch_s())