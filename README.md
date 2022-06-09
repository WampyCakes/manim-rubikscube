# Manim RubiksCube

This is a fork of the plugin for the [Manim Community](https://www.manim.community/) that provides an implementation of the classic Rubik\'s Cube.

# NOTE

This fork aims to fix the installation error cause by a breaking change in the latest version of Manim (v0.15.2). Use this fork if you're having trouble installing it (or just edit single line of code in `cubie.py` as shown in the pull request) or wait until the original one is merged.

# Installation

This plugin is [available on PyPi.](https://pypi.org/project/manim-rubikscube/) Usage of this plugin assumes that Python and Manim are both correctly installed. Manim is listed as a dependency, but no version is specified. This is because the plugin will work with any version of Manim Community that does not have breaking changes to the plugin. Some releases of this plugin ave been tested with certain versions of Manim. To see what versions of Manim are confirmed to be compatible with this plugin (to the best of my testing), [see Releases.](https://github.com/WampyCakes/manim-rubikscube/releases) By no means is this exclusive. Most releases of this plugin will work, more or less, on all versions of Manim Community. To install the RubiksCube plugin run:

``` {.bash}
pip install manim-rubikscube
```

To see what version of manim-rubikscube you are running:

``` {.bash}
manim-rubikscube
```

or

``` {.bash}
pip list
```

# Importing

To use the RubiksCube, you can either:

-   Add `from manim_rubikscube import *` to your script
-   Follow the [Manim steps for using
    plugins](https://docs.manim.community/en/stable/installation/plugins.html#using-plugins-in-projects)

Once the RubiksCube is imported, you can use the RubiksCube as any other mobject.

# Documentation and Examples

Documentation and examples are [available here.](https://manim-rubikscube.readthedocs.io/en/stable/)

# License

This plugin is licensed under the MIT license. See the `LICENSE` file for more information.
