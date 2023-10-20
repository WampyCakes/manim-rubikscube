import numpy as np
from manim.animation.animation import Animation
from manim.constants import PI
from manim.mobject.types.vectorized_mobject import VGroup

from .cube import RubiksCube

class CubeMove(Animation):
    def __init__(self, mobject: RubiksCube, face, **kwargs):
        # This only makes sense when called on a RubiksCube
        assert isinstance(mobject, RubiksCube)

        # Compute the axis of rotation by taking the vector from the cube's center
        # to the middle cubie of the rotated face
        # TODO: this might accumulate numerical errors, but it seems ok for tens of moves
        self.axis = (
            mobject.get_face(face[0], flatten=False)[1, 1].get_center()
            - mobject.get_center()
        )
        self.face = face

        self.n_turns = 1 if "2" not in face else 2
        self.n_turns = -self.n_turns if "'" in face else self.n_turns

        super().__init__(mobject, **kwargs)

    def create_starting_mobject(self):
        starting_mobject = self.mobject.copy()
        return starting_mobject

    def interpolate_mobject(self, alpha):
        self.mobject.become(self.starting_mobject)
        
        VGroup(*self.mobject.get_face(self.face[0])).rotate(
            -self.rate_func(alpha) * (PI / 2) * self.n_turns,
            self.axis,
        )

    def finish(self):
        super().finish()
        cubies = self.mobject.cubies[self.mobject.get_face_slice(self.face[0])]

        # We need to make sure that moves that are supposed to be clockwise really are
        n_turns = self.n_turns if (self.face[0] in {"L", "F", "D"}) else -self.n_turns

        # Get to a non-negative value
        n_turns = (n_turns + 4) % 4
        
        cubies = np.rot90(cubies, k=n_turns)

        self.mobject.cubies[self.mobject.get_face_slice(self.face[0])] = cubies
