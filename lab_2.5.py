class Point3D():

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def _sum(self, x,y,z):
        self.x += x
        self.y += y
        self.z += z
    def _raz(self, x,y,z):
        self.x -= x
        self.y -= y
        self.z -= z
    def _del(self, x,y,z):
        self.x /= x
        self.y /= y
        self.z /= z
    def _umn(self, x,y,z):
        self.x *= x
        self.y *= y
        self.z *= z
    
    def _print(self):
        return self.x,self.y,self.z

dot = Point3D(1,11,1)

dot._sum(1,0,0)

print(dot._print())
    