from PIL import Image
from functions import memory
from functions import jmp

class Cursor:
    def __init__(self):
        self.position = (0, 0)
        self.canvas = (0, 0)
        self.mem = (0, 0)
        self.op = 0
        self.dir = (1, 0)
    def move(self):
        self.position = (self.position[0] + self.dir[0], self.position[1] + self.dir[1])
        if self.position[0] >= 256:
            self.position = (0, self.position[1] + self.dir[1])
        if self.position[1] >= 256:
            self.position = (self.position[0] + self.dir[0], 0)

    def store(self, pixels):
        pixel = pixels[self.position[0], self.position[1]]

        self.mem = (pixel[1], pixel[2])
        self.op = pixel[0]
    def execute(self, pixels):
        match self.op:
            case 1:
                jmp.jump(self.mem, self)
            case 2:
                memory.write(self.mem, pixels, self)
                self.move()
            case 3:
                memory.read(self.mem, pixels, self)
    def affect(self, pixels):
        pixels[self.position[0], self.position[1]] = (self.op, self.mem[0], self.mem[1])
        