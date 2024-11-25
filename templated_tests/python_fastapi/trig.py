import math

def degrees_to_radians(degrees):
    """Convert degrees to radians."""
    return degrees * math.pi / 180

def radians_to_degrees(radians):
    """Convert radians to degrees."""
    return radians * 180 / math.pi

def sin(degrees):
    """Calculate sine of an angle in degrees."""
    return math.sin(degrees_to_radians(degrees))

def cos(degrees):
    """Calculate cosine of an angle in degrees."""
    return math.cos(degrees_to_radians(degrees))

def tan(degrees):
    """Calculate tangent of an angle in degrees."""
    if abs(cos(degrees)) < 1e-10:  # Prevent division by very small numbers
        raise ValueError("Tangent undefined at 90 or 270 degrees")
    return math.tan(degrees_to_radians(degrees))

def sec(degrees):
    """Calculate secant of an angle in degrees."""
    cosine = cos(degrees)
    if abs(cosine) < 1e-10:
        raise ValueError("Secant undefined at 90 or 270 degrees")
    return 1 / cosine

def csc(degrees):
    """Calculate cosecant of an angle in degrees."""
    sine = sin(degrees)
    if abs(sine) < 1e-10:
        raise ValueError("Cosecant undefined at 0 or 180 degrees")
    return 1 / sine

def cot(degrees):
    """Calculate cotangent of an angle in degrees."""
    sine = sin(degrees)
    if abs(sine) < 1e-10:
        raise ValueError("Cotangent undefined at 0 or 180 degrees")
    return cos(degrees) / sine