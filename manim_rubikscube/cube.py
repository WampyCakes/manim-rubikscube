from manim.utils.color import *
from manim.mobject.mobject import Mobject
from manim.mobject.types.vectorized_mobject import VMobject
import numpy as np
from .cubie import Cubie
from .kociemba import solver as sv

class RubiksCube(VMobject):
    #If facing the Rubik's Cube, X goes Front to Back, Y goes Right to Left, Z goes Down to Up 
    #Each coordinate starts at 0 and goes to (Dimensions - 1)

    cubies = np.ndarray
    indices = {}

    # Colors are in the order Up, Right, Front, Down, Left, Back
    def __init__(self, dim=3, colors=[WHITE, "#B90000", "#009B48", "#FFD500", "#FF5900", "#0045AD"], x_offset=2.1, y_offset=2.1, z_offset=2.1):#, **kwargs):
        if not (dim >= 2):
            raise Exception("Dimension must be >= 2")

        VMobject.__init__(self)
        self.dimensions = dim
        self.colors = colors
        self.x_offset = [[Mobject.shift, [x_offset, 0, 0]]]
        self.y_offset = [[Mobject.shift, [0, y_offset, 0]]]
        self.z_offset = [[Mobject.shift, [0, 0, z_offset]]]

        self.cubies = np.ndarray((dim, dim, dim), dtype=Cubie)
        self.generate_cubies()#**kwargs)
    
    def generate_cubies(self):#, **kwargs):
        for x in range(self.dimensions):
            for y in range(self.dimensions):
                for z in range(self.dimensions):
                    cubie = Cubie(x, y, z, self.dimensions, self.colors)#, **kwargs)
                    self.transform_cubie(x, self.x_offset, cubie)
                    self.transform_cubie(y, self.y_offset, cubie)
                    self.transform_cubie(z, self.z_offset, cubie)
                    self.add(cubie)
                    self.cubies[x, y, z] = cubie

    def set_state(self, positions):
        colors = {
            "U": self.colors[0],
            "R": self.colors[1],
            "F": self.colors[2],
            "D": self.colors[3],
            "L": self.colors[4],
            "B": self.colors[5],
        }
        positions = list(positions)
        # TODO: Try/except in case a color was not given
        # try:
        for cubie in np.rot90(self.get_face("U", False), 2).flatten():
            cubie.get_face("U").set_fill(colors[positions.pop(0)], 1)

        for cubie in np.rot90(np.flip(self.get_face("R", False), (0, 1)), -1).flatten():
            cubie.get_face("R").set_fill(colors[positions.pop(0)], 1)
        
        for cubie in np.rot90(np.flip(self.get_face("F", False), 0)).flatten():
            cubie.get_face("F").set_fill(colors[positions.pop(0)], 1)
        
        for cubie in np.rot90(np.flip(self.get_face("D", False), 0), 2).flatten():
            cubie.get_face("D").set_fill(colors[positions.pop(0)], 1)
        
        for cubie in np.rot90(np.flip(self.get_face("L", False), 0)).flatten():
            cubie.get_face("L").set_fill(colors[positions.pop(0)], 1)
        
        for cubie in np.rot90(np.flip(self.get_face("B", False), (0, 1)), -1).flatten():
            cubie.get_face("B").set_fill(colors[positions.pop(0)], 1)
        # except:
            # return

    def solve_by_kociemba(self, state):
        return sv.solve(state).replace("3", "'").replace("1", "").split()

    def transform_cubie(self, position, offset, tile):
        offsets_nr = len(offset)
        for i in range(offsets_nr):
            for j in range(int(len(offset[i]) / 2)):
                if position < 0:
                    magnitude = len(range(-i, position, -offsets_nr)) * -1
                    offset[-1 - i][0 + j * 2](
                        tile, magnitude * np.array(offset[-1 - i][1 + j * 2])
                    )
                else:
                    magnitude = len(range(i, position, offsets_nr))
                    offset[i][0 + j * 2](
                        tile, magnitude * np.array(offset[i][1 + j * 2])
                    )

    def get_face(self, face, flatten=True):
        if face == "F":
            face = self.cubies[0, :, :]
        elif face == "B":
            face = self.cubies[self.dimensions-1, :, :]
        elif face == "U":
            face = self.cubies[:, :, self.dimensions-1]
        elif face == "D":
            face = self.cubies[:, :, 0]
        elif face == "L":
            face = self.cubies[:, self.dimensions-1, :]
        elif face == "R":
            face = self.cubies[:, 0, :]

        if flatten:
            return face.flatten()
        else:
            return face
    
    def set_indices(self):
        for c in self.cubies.flatten():
            # self.indices[c.get_position()] = c.get_position()
            self.indices[c.get_rounded_center()] = c.position

    def adjust_indices(self, cubies):
        for c in cubies.flatten():
            loc = self.indices[c.get_rounded_center()]
            self.cubies[loc[0], loc[1], loc[2]] = c