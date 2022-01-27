
class Comp():
    def __init__(self, chip_name, mgc):
        self.chip_name  = chip_name
        self.mgc = mgc

    def memory(self, func):
        def wrapper():
            print(0.1 * self.mgc + 6000)
            func()
        return wrapper
        
class Comp2(Comp):
    def __init__(self, chip_name, mgc,p):
        super().__init__(chip_name, mgc)
        self.p = p

    def memory(self, func):
        return super().memory(func)

    @memory
    def memory2(self):
        return (0.1 * self.mgc + 6000) + 0.5 * self.p

cmp = Comp2('Chip_1', 3000, 2)

cmp.memory2()
