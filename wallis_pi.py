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

import math # get a high precision value of pi for reference

my_pi = 1
precision = 1e-03 # the target precision.

product = 1
i = 1

while abs(math.pi - my_pi) > precision:
    product *= (4*i**2) / ((4*i**2)-1)
    my_pi = product * 2
    i += 1

print(precision, 'target precision')
print(i,'iterations run to achieve target precision')
print(my_pi,'my_pi')
