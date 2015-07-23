from math import pi
import pyglet.gl as gl
from core.entities import Effect
from core.matrix import push, pop


class Translate(Effect):
    def wrap(self, fs,
             x, y=0.0, z=0.0):
        push()
        gl.glTranslatef(x, y, z)
        for f in fs:
            f()
        pop()


class Scale(Effect):
    def wrap(self, fs,
             *args):

        if len(args) == 3:
            x, y, z = args
        elif len(args) == 2:
            x, y, z = args + [1]
        elif len(args) == 1:
            x, y, z = args * 3
        else:
            raise TypeError  # TODO better explaination

        push()
        gl.glScalef(x, y, z)
        for f in fs:
            f()
        pop()


class Rotate(Effect):
    def wrap(self, fs,
             angle,
             x=0.0, y=0.0, z=1.0):
        push()
        gl.glRotatef(angle * 180 / pi,
                     x, y, z)
        for f in fs:
            f()
        pop()


class Turnaround(Effect):
    def wrap(self, fs, n):
        for i in range(n):
            push()
            angle = 2.0 * pi * i / n
            gl.glRotatef(angle * 180 / pi,
                         0, 0, 1)
            for f in fs:
                f()
            pop()
