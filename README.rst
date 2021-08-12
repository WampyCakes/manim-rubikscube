Manim RubiksCube
============================================


This plugin for `Manim Community <https://www.manim.community/>`_ provides an implementation of the classic Rubik's Cube.

NOTE
====
Wonder how Manim RubiksCube looks so much better in `this video <https://www.youtube.com/watch?v=xMY0mPPY25k>`_ than my docs and examples show? I have made a lot of technical upgrades and aesthetic updates to the plugin locally that are not yet ready for GitHub or a new release. Stay patient for the update! Until then, you can locally edit manim-rubikscube yourself to replicate the aesthetics I have in this video, if you so desire. 

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

Documentation and Examples
==========================
Documentation and examples are `available here. <https://manim-rubikscube.readthedocs.io/en/stable/>`_

License
=======
This plugin is licensed under the MIT license. See the ``LICENSE`` file for more information.
