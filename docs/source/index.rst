Manim RubiksCube
============================================


This plugin for `Manim Community <https://www.manim.community/>`_ provides an implementation of the classic Rubik's Cube. This project is open source `(available on GitHub) <https://github.com/WampyCakes/manim-rubikscube>`_.

Installation
============

This plugin is `available on PyPi. <https://pypi.org/project/manim-rubikscube/>`_
Usage of this plugin assumes that Python and Manim are both correctly installed. Manim is listed as a dependency, but no version is specified. This is because the plugin will work with any version of Manim Community that does not have breaking changes to the plugin. Some releases of this plugin have been tested with certain versions of Manim. To see what versions of Manim are confirmed to be compatible with this plugin (to the best of my testing), `see Releases. <https://github.com/WampyCakes/manim-rubikscube/releases>`_ By no means is this exclusive. Most releases of this plugin will work, more or less, on all versions of Manim Community.

To install the RubiksCube plugin run:

.. code-block:: bash

   pip install manim-rubikscube


To see what version of manim-rubikscube you are running:

.. code-block:: bash

    manim-rubikscube

or

.. code-block:: bash

    pip list

Importing
=========

To use the RubiksCube, you can either:


* Add ``from manim_rubikscube import *`` to your script
* Follow the `Manim steps for using plugins <https://docs.manim.community/en/stable/installation/plugins.html#using-plugins-in-projects>`_

Once the RubiksCube is imported, you can use the RubiksCube as any other mobject.

Examples
========


Creating a RubiksCube
---------------------

.. manim:: FadeInExample

    class FadeInExample(ThreeDScene):
        def construct(self):
             # After creating the RubiksCube, it may be necessary to scale it to 
             # comfortably see the cube in the camera's frame
             cube = RubiksCube().scale(0.6) 

             # Setup where the camera looks
             self.set_camera_orientation(phi=50*DEGREES, theta=160*DEGREES)
             self.renderer.camera.frame_center = cube.get_center()

             # At this point, you have created a RubiksCube object.
             # All that's left is to add it to the scene.

             # A RubiksCube acts as any other Mobject. It can be added with 
             # self.add() or any Manim creation animation
             self.play(
                 FadeIn(cube)
             )

             # Rotate the camera around the RubiksCube for 8 seconds
             self.begin_ambient_camera_rotation(rate=0.5)
             self.wait(8)


|

Changing the colors of a RubiksCube
-----------------------------------

.. manim:: ColorExample

   class ColorExample(ThreeDScene):
       def construct(self):
           # Colors are passed in the order [Up, Right, Front, Down, Left, Back]
           # Default is [WHITE, "#B90000", "#009B48", "#FFD500", "#FF5900", "#0045AD"]
           cube = RubiksCube(colors=[WHITE, ORANGE, DARK_BLUE, YELLOW, PINK, "#00FF00"]).scale(0.6)

           self.set_camera_orientation(phi=50*DEGREES, theta=160*DEGREES)
           self.renderer.camera.frame_center = cube.get_center()

           self.play(
               FadeIn(cube)
           )

           self.begin_ambient_camera_rotation(rate=0.5)
           self.wait(8)


|

Setting the state of a RubiksCube
---------------------------------

When you have a RubiksCube in real life and want to replicate it in manim, the ``set_state()`` method enables this functionality. Or, if you know the state of any cube without knowing what movements got it to that point, this method allows you to also replicate that.

.. manim:: StateExample

   class StateExample(ThreeDScene):
       def construct(self):
           cube = RubiksCube().scale(0.6)

           # The set_state method takes in a String that tells the RubiksCube what color each Cubie 
           # should be. Imagine that you have a RubiksCube that is flattened to 2D as below:
           #               |************|
           #               |*U1**U2**U3*|
           #               |************|
           #               |*U4**U5**U6*|
           #               |************|
           #               |*U7**U8**U9*|
           #               |************|
           #  |************|************|************|************|
           #  |*L1**L2**L3*|*F1**F2**F3*|*R1**R2**R3*|*B1**B2**B3*|
           #  |************|************|************|************|
           #  |*L4**L5**L6*|*F4**F5**F6*|*R4**R5**R6*|*B4**B5**B6*|
           #  |************|************|************|************|
           #  |*L7**L8**L9*|*F7**F8**F9*|*R7**R8**R9*|*B7**B8**B9*|
           #  |************|************|************|************|
           #               |************|
           #               |*D1**D2**D3*|
           #               |************|
           #               |*D4**D5**D6*|
           #               |************|
           #               |*D7**D8**D9*|
           #               |************|

           # In order to tell the set_state method what color the U1 cubie should be, you tell it
           # which face's color that is. 

           # For example, if the R face of the Cube is pink and U1 is pink, 
           # the first letter in the string is R. 

           # Similarly, because the center of the U face (U5) does not change color, 
           # it will be the letter U in the state string 
           # (for the U face, that would mean the 5th letter in the string).

           # Starting at the number 1 cubie and working to the number 9 cubie, the order
           # of the state string is the U face, then R face, followed by F, D, L, B,
           # in that order.

           # So, the first 9 letters in the string below tell the RubiksCube what color each
           # Cubie in the U face is. So on and so forth for the other sides.

           # This method works for a cube of any dimensions, as long as a color is provided 
           # for each Cubie face.

           cube.set_state("BBFBUBUDFDDUURDDURLLLDFRBFRLLFFDLUFBDUBBLFFUDLRRRBLURR")

           self.set_camera_orientation(phi=50*DEGREES, theta=160*DEGREES)
           self.renderer.camera.frame_center = cube.get_center()

           self.play(
               FadeIn(cube)
           )

           self.begin_ambient_camera_rotation(rate=0.5)
           self.wait(8)


|

Properties of a RubiksCube
--------------------------

..

   :strong:`Note:`  It is not necessary to pass any parameters to the RubiksCube. Doing so is entirely for additional functionality and stylistic tweaks.


To this point, we have seen that one property of a RubiksCube is a list of colors for the cube faces. There are currently two other parameters that can be passed.

Dimension
^^^^^^^^^

2-Dimensional RubiksCube
~~~~~~~~~~~~~~~~~~~~~~~~

.. manim:: TwoDimensionalExample

   class TwoDimensionalExample(ThreeDScene):
       def construct(self):
           # The first parameter the RubiksCube takes is dimension.
           # Alternatively, dim=2 can be passed. Default dim is 3
           cube = RubiksCube(2).scale(0.6)

           self.set_camera_orientation(phi=50*DEGREES, theta=160*DEGREES)
           self.renderer.camera.frame_center = cube.get_center()

           self.play(
               FadeIn(cube)
           )

           self.begin_ambient_camera_rotation(rate=0.5)
           self.wait(3)


|

An example of ``set_state()`` on a non-3-dimensional cube:

.. manim:: TwoDimensionalStateExample

   class TwoDimensionalStateExample(ThreeDScene):
       def construct(self):
           cube = RubiksCube(2).scale(0.6)
           # Notice how there are fewer characters in the string compared
           # to the 3-dimensional cube because there are less cubie faces to display
           cube.set_state("RUFBLLBDRDDBRUUDLFFBFRLU")

           self.set_camera_orientation(phi=50*DEGREES, theta=160*DEGREES)
           self.renderer.camera.frame_center = cube.get_center()

           self.play(
               FadeIn(cube)
           )

           self.begin_ambient_camera_rotation(rate=0.5)
           self.wait(3)



10-Dimensional RubiksCube
~~~~~~~~~~~~~~~~~~~~~~~~~

..

   :strong:`WARNING:` While this plugin can create a RubiksCube with large dimensions, it takes a long time to render. In the future, OpenGL rendering will vastly improve this.
   
.. manim:: TenDimensionalExample
    :save_last_frame:

    class TenDimensionalExample(ThreeDScene):
        def construct(self):
            cube = RubiksCube(10).scale(0.2)
            self.set_camera_orientation(phi=50*DEGREES, theta=160*DEGREES)
            self.renderer.camera.frame_center = cube.get_center()

            self.add(cube)



Offset
^^^^^^
A RubiksCube has three different offset values. Offsets can be useful for isolating faces or Cubies for further explanation or analysis.

* The :code:`x_offset` determines how close/far Cubies are from Front to Back
* The :code:`y_offset` determines how close/far Cubies are from Right to Left
* The :code:`z_offset` determines how close/far Cubies are from Top to Bottom

The default value for all three offsets is :code:`2.1`. Adjusting these offsets changes the "gap" between Cubies

|

Offsets of 3
~~~~~~~~~~~~
.. manim:: ThreeOffsetExample

    class ThreeOffsetExample(ThreeDScene):
        def construct(self):
            # Passing in 3 for each offset
            cube = RubiksCube(x_offset=3, y_offset=3, z_offset=3).scale(0.5)

            self.set_camera_orientation(phi=50*DEGREES, theta=160*DEGREES)
            self.renderer.camera.frame_center = cube.get_center()

            self.play(
                FadeIn(cube)
            )

            self.begin_ambient_camera_rotation(rate=0.5)
            self.wait(3)


|

y_offset of 4
~~~~~~~~~~~~~

.. manim:: YOffsetExample

   class YOffsetExample(ThreeDScene):
       def construct(self):
           # Only setting the y_offset
           cube = RubiksCube(y_offset=4).scale(0.6)

           self.set_camera_orientation(phi=50*DEGREES, theta=160*DEGREES)
           self.renderer.camera.frame_center = cube.get_center()

           self.play(
               FadeIn(cube)
           )

           self.begin_ambient_camera_rotation(rate=0.5)
           self.wait(3)


|

Accessing Faces and Cubies
--------------------------

Accessing a Cubie
^^^^^^^^^^^^^^^^^

A cubie is each individual cube in a RubiksCube. For a 3x3x3 RubiksCube, there are 27 cubies. The cube's cubies are stored in a numpy array called ``cubies``.

For a 3-dimensional RubiksCube, the cubies array is structured as follows:

.. code-block::

   Shape: (dim, dim, dim)
   [
       [
           [Cubie, Cubie, Cubie],
           [Cubie, Cubie, Cubie],
           [Cubie, Cubie, Cubie]
       ],
       [
           [Cubie, Cubie, Cubie],
           [Cubie, Cubie, Cubie],
           [Cubie, Cubie, Cubie]
       ],
       [
           [Cubie, Cubie, Cubie],
           [Cubie, Cubie, Cubie],
           [Cubie, Cubie, Cubie]
       ]
   ]

Each "level" in the array represents a coordinate. Each of the first three arrays represents a different X value (0, 1, or 2). In each of those arrays, there are three more arrays, each representing a different Y value (0, 1, or 2). Finally, there are three Cubie objects. Each represents a different Z value. The size of this array directly corresponds to the dimension of the RubiksCube. This structure, along with numpy, allows for easy, convenient, and cheap accessing of cubies and faces.

..

   :strong:`For Reference:` If facing the Rubik's Cube, X goes Front to Back, Y goes Right to Left, Z goes Down to Up. Each coordinate starts at 0 and goes to (Dimension - 1)


So, to access the Cubie at coordinates X=0, Y=0, Z=0, ``cube.cubies[0, 0, 0]`` will return it. This holds true no matter the dimension of the RubiksCube.

.. manim:: IndicateCubieExample

   class IndicateCubieExample(ThreeDScene):
       def construct(self):
           cube = RubiksCube().scale(0.6)

           self.set_camera_orientation(phi=50*DEGREES, theta=160*DEGREES)
           self.renderer.camera.frame_center = cube.get_center()

           self.play(
               FadeIn(cube)
           )
           self.wait()

           # Retrieve the cubie at 0, 0, 0 and play the Indicate animation on it
           self.play(
               Indicate(cube.cubies[0, 0, 0])
           )

           self.wait()



Accessing a Face
^^^^^^^^^^^^^^^^

The RubiksCube has a method called ``get_face()`` that will return an array of Cubies. At its core, this just accesses Cubies like we did above.

Because the front face of the RubiksCube has an X value of 0 (regardless of the dimension of the cube), returning all Cubies with an X value of 0 will give you the front face. When ``cube.get_face("F")`` is called, it is effectively returning ``cube.cubies[0, :, :]``. This is possible for all 6 faces of the RubiksCube, and it can also be used manually to return more than just one "slice" of a RubiksCube at a time. This is achievable with `numpy indexing <https://numpy.org/doc/stable/reference/arrays.indexing.html>`_.

.. manim:: IndicateFaceExample

   class IndicateFaceExample(ThreeDScene):
       def construct(self):
           cube = RubiksCube().scale(0.6)

           self.set_camera_orientation(phi=50*DEGREES, theta=160*DEGREES)
           self.renderer.camera.frame_center = cube.get_center()

           self.play(
               FadeIn(cube)
           )
           self.wait()

           # Because get_face() returns an array of Cubie objects, they must
           # be added to a VGroup before an animation can be called on all 
           # of them simultaneously
           self.play(
               Indicate(VGroup(*cube.get_face("F")))
           )

           self.wait()


|

Accessing a Cubie Face
^^^^^^^^^^^^^^^^^^^^^^

Just as the cube's ``get_face()`` method works, once you have accessed a Cubie object, you can call ``get_face(face)``. For example, calling ``cube.cubies[0, 0, 0].get_face("F")`` will return the front face of that cubie as a ``Square()`` mobject. If the ``get_face()`` method returns a different square than you expected, it is likely a result of the RubiksCube's or the camera's orientation changing your perspective of direction in the scene.

|

Face Rotations
--------------

The recommended way to rotate a face of the RubiksCube is to use the ``CubeMove()`` animation. I highly discourage trying to rotate the cube without using this pre-made animation. While possible, it's not worth it.

CubeMove animation
^^^^^^^^^^^^^^^^^^

.. manim:: CubeMoveExample

   class CubeMoveExample(ThreeDScene):
       def construct(self):
           cube = RubiksCube().scale(0.6)

           self.set_camera_orientation(phi=50*DEGREES, theta=160*DEGREES)
           self.renderer.camera.frame_center = cube.get_center()

           self.play(
               FadeIn(cube)
           )
           self.wait()

           # CubeMove() is the recommended way to animate a move. It functions very similiarly to 
           # Rotating(). It takes a RubiksCube object and the face to rotate. The possible faces
           # are F, B, U, D, L, and R. To do an inverse move, it is proceeded by a single quote (').
           # To do a double move, put a "2" after the face to move. All three variations are shown:
           self.play(CubeMove(cube, "F"))
           # If you think a move is too fast or too slow, run_time can be provided (in seconds).
           self.play(CubeMove(cube, "U2"), run_time=2)
           self.play(CubeMove(cube, "R'"))

           self.wait()


|

Solving the Cube
----------------

This implementation of a RubiksCube also includes `Kociemba's algorithm <https://github.com/hkociemba/RubiksCube-TwophaseSolver>`_\ , a brilliantly fast solving algorithm made by Herbert Kociemba. The RubiksCube object includes the method ``solve_by_kociemba()``. Given a state, it will return a list of moves to perform. Solving is only possible for 3-dimensional cubes. Solving any other size RubiksCube will require hardcoding of the moves to perform. Currently, ``solve_by_kociemba()`` requires a state string to solve (like the one used in ``set_state()``\ ). In the future, this will be replaced with using the state of the cube without having to manually input the state of the cube.

.. code-block:: python

   from manim import *
   from manim_rubikscube import *

   class SolveExample(ThreeDScene):
       def construct(self):
           cube = RubiksCube()
           print(cube.solve_by_kociemba("BBFBUBUDFDDUURDDURLLLDFRBFRLLFFDLUFBDUBBLFFUDLRRRBLURR"))

Given the state of the Cube, it returned the necessary moves to execute to solve it. All moves returned by the method are able to be read by ``CubeMove()``.

.. code-block::

   solve_by_kociemba() returned:
   ['F2', 'B2', "R'", "B'", 'R2', "L'", 'D', "F'", 'U', 'B', 'U2', 'L', 'U2', "R'", 'D2', 'R', 'L', 'D2', 'F2', 'B2']

Putting it All Together
-----------------------

.. manim:: AllTogetherExample

   class AllTogetherExample(ThreeDScene):
       def construct(self):
           # Change the cube from default colors
           cube = RubiksCube(colors=[WHITE, ORANGE, DARK_BLUE, YELLOW, PINK, "#00FF00"]).scale(0.6)

           self.set_camera_orientation(phi=50*DEGREES, theta=160*DEGREES)
           self.renderer.camera.frame_center = cube.get_center()

           # Set the state of the cube
           state = "BBFBUBUDFDDUURDDURLLLDFRBFRLLFFDLUFBDUBBLFFUDLRRRBLURR"
           cube.set_state(state)

           self.play(FadeIn(cube))
           self.wait()

           # Loop through results of the kociemba algorithm
           for m in cube.solve_by_kociemba(state):
               # Execute the move
               self.play(CubeMove(cube, m), run_time=1.5)

           # Show the final product
           self.play(
               Rotating(cube, radians=2*PI, run_time=2)
           )


|

To do
=====


* ``Transform()`` between RubiksCubes of different dimensions
* Rotate multiple slices (like rotating the two front faces of a 4x4x4)
* Check solvability of cube
* Execute string of cube moves
* ``solve_by_kociemba()`` on current state of cube
* Allow for parameters to be passed from ``RubiksCube`` to ``Cubie`` for use by the ``Square()`` faces
* Switch from using center-tracking to index-tracking for ``adjust_indices()``
* Allow for coloring of inner faces of Cubies
* Focus on cubies and faces
* Clean the code
* and much more!

.. Release Notes
.. =============


.. * 0.1.0

..   * Initial release

Acknowledgments
===============


* `XorUnison's <https://github.com/XorUnison>`_ Honeycomb mobject is an upcoming feature in `Manim Community <https://github.com/ManimCommunity/manim>`__. This RubiksCube plugin takes advantage of Honeycomb's ``transform_tile()`` method and offset implementation. Until it is added to Manim Community, the best way to see Honeycomb is `through his videos on Tiling <https://www.youtube.com/user/XorUnison/videos>`_\ , the 2D version of Honeycomb. 
* `Herbert Kociemba's Two Phase Rubik's Cube Solving Algorithm <https://github.com/hkociemba/RubiksCube-TwophaseSolver>`_

License
=======

This plugin is licensed under the MIT license (\ `see LICENSE file <https://github.com/WampyCakes/manim-rubikscube/blob/main/LICENSE>`_\ ).


.. .. toctree::
..    :maxdepth: 2
..    :caption: Contents:



.. Indices and tables
.. ==================

.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`
