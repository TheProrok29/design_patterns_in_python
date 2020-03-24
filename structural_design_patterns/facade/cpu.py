class CPU:
    def __init__(self, cores, mhz, cache, socket):
        self.cores = cores
        self.mhz = mhz
        self.cache = cache
        self.socket = socket

    def freeze(self):
        print('Freezing processor.')

    def jump(self, position)
        print('Jumping to: ', position)

    def execute(self):
        print('Executing.')
