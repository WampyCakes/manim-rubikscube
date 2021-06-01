from .cube import *
from .cube_animations import *

try:
    import importlib.metadata as importlib_metadata
except ModuleNotFoundError:
    import importlib_metadata

__version__ = "latest"#importlib_metadata.version(__name__)
