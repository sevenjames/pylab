# =============================================================================
# 2020-01-21
# programming challenge from SciPy Lecture Notes
# section 1.2.3 Getting Started > The Python Language > Control Flow
# https://scipy-lectures.org/intro/language/control_flow.html
# compute pi using the Wallis formula
# 
# precision  iterations
# 1e-03      786
# 1e-04      7855
# 1e-05      78541
# 1e-06      785399
# 1e-07      7851419
# 
# =============================================================================

# get a high precision value of pi for reference
from math import pi as math_pi

def wallacepi(precision=1e-03):
    """compute pi using the Wallis formula"""
    my_pi = 1
    product = 1
    i = 1

    while abs(math_pi - my_pi) > precision:
        product *= (4*i**2) / ((4*i**2)-1)
        my_pi = product * 2
        i += 1
        
    return [my_pi,precision,i]

print('Wallace Pi calculation using default precision')
print(wallacepi())
print()

print('Wallace Pi calculation for several specified degrees of precision')
print('[pi, precision, iterations]')
for p in [1e-03,1e-04,1e-05,1e-06]:
    print(wallacepi(p))
