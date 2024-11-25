import pytest
import math
from trig import sin, cos, tan, sec, csc, cot

# Define some common test angles in degrees
SPECIAL_ANGLES = [0, 30, 45, 60, 90, 180, 270, 360]
TOLERANCE = 1e-10  # Tolerance for floating point comparisons