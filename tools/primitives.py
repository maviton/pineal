import pyglet.gl as gl
import pyglet.image
from pyglet.image.codecs.png import PNGImageDecoder

from core.entities import Entity
from core.shapes import solid_polygon, wired_polygon


class Psolid(Entity):
    memo = {}

    def draw(self, n, color):
        if n not in self.memo:
            self.memo[n] = solid_polygon(n)

        vlist = self.memo[n]
        vlist.colors = color * (n * 3)
        vlist.draw(gl.GL_TRIANGLES)


class Pwired(Entity):
    memo = {}

    def draw(self, n, color):
        if n not in self.memo:
            self.memo[n] = wired_polygon(n)

        vlist = self.memo[n]
        vlist.colors = color * n
        vlist.draw(gl.GL_LINE_LOOP)


class Image(Entity):
    memo = {}

    def draw(self, name):
        if name not in self.memo:
            self.memo[name] = pyglet.image.load("images/%s.png" % name,
                                                decoder=PNGImageDecoder())

        self.memo[name].blit(-1.0, 1.0, 0.0,
                             2.0, 2.0)