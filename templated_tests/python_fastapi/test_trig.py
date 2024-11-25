import pytest
import math
from trig import *

# Define some common test angles in degrees
SPECIAL_ANGLES = [0, 30, 45, 60, 90, 180, 270, 360]
TOLERANCE = 1e-10  # Tolerance for floating point comparisons

def test_degrees_to_radians_common_angles():
    """Test conversion from degrees to radians for common angles"""
    test_cases = [
        (0, 0),
        (30, math.pi/6),
        (45, math.pi/4),
        (60, math.pi/3),
        (90, math.pi/2),
        (180, math.pi),
        (360, 2*math.pi)
    ]
    
    for degrees, expected_radians in test_cases:
        assert abs(degrees_to_radians(degrees) - expected_radians) < TOLERANCE