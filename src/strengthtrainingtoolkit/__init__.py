from .__version__ import __version__, __author__

import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

from .database import Load, Exercise, Workout
