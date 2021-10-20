from manim.utils.color import *
from manim.mobject.mobject import Mobject
from manim.mobject.types.vectorized_mobject import VMobject
import numpy as np
from .cubie import Cubie
from kociemba import solver as sv


class RubiksCube(VMobject):
    # If facing the Rubik's Cube, X goes Front to Back, Y goes Right to Left, Z goes Down to Up
    # Each coordinate starts at 0 and goes to (Dimensions - 1)

    # Colors are in the order Up, Right, Front, Down, Left, Back
    def __init__(self, dim=3, colors=None, x_offset=2.1, y_offset=2.1, z_offset=2.1):
        if not (dim >= 2):
            raise Exception("Dimension must be >= 2")

        VMobject.__init__(self)

        if colors is None:
            colors = [WHITE, "#B90000", "#009B48", "#FFD500", "#FF5900", "#0045AD"]

        self.dimensions = dim
        self.colors = colors
        self.x_offset = [[Mobject.shift, [x_offset, 0, 0]]]
        self.y_offset = [[Mobject.shift, [0, y_offset, 0]]]
        self.z_offset = [[Mobject.shift, [0, 0, z_offset]]]

        self.cubies = np.ndarray((dim, dim, dim), dtype=Cubie)
        self.generate_cubies()

    def generate_cubies(self):
        for x in range(self.dimensions):
            for y in range(self.dimensions):
                for z in range(self.dimensions):
                    cubie = Cubie(x, y, z, self.dimensions, self.colors)
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
        #     return

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

    def get_face_slice(self, face):
        """
        Return a NumPy slice object specifying which part of the array corresponds
        to which face. NumPy sli indexing a ndarray,
        e.g. a[:, 2] == a[np.s_[:, 2]]
        """
        face_slices = {
            "F": np.s_[0, :, :],
            "B": np.s_[self.dimensions - 1, :, :],
            "U": np.s_[:, :, self.dimensions - 1],
            "D": np.s_[:, :, 0],
            "L": np.s_[:, self.dimensions - 1, :],
            "R": np.s_[:, 0, :],
        }

        if face in face_slices:
            return face_slices[face]
        else:
            raise ValueError("Invalid face identifier " + face)

    def get_face(self, face, flatten=True):
        face = self.cubies[self.get_face_slice(face)]

        if flatten:
            return face.flatten()
        else:
            return face
