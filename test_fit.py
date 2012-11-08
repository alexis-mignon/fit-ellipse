# -*- coding: utf-8 -*-
"""
Sample code for the use of fit_ellipse

:Author: Alexis Mignon
:E-mail: alexis.mignon@gmail.com
"""

import pylab as pl
import numpy as np
from fit_ellipse import create_ellipse, fit_ellipse, get_parameters

# ellipse parameters
r = (1.0, 0.5)
xc = (0.5,1.5)
alpha = np.pi/3

# points to draw the ellipse
X = create_ellipse(r,xc,alpha)
# points from which we guess the parameters
Xn = create_ellipse(r,xc,alpha, angle_range=(-np.pi/2, np.pi/2), n=10)
# additional gaussian noise
Xn += 0.05 * min(r) * np.random.randn(*Xn.shape)

# guess parameters from noised data
a = fit_ellipse(Xn)
rf, xcf, alpha_f = get_parameters(a)

# points to draw the guessed ellipse
Xf = create_ellipse(rf,xcf,alpha_f)

print "real params:"
print "rx, ry:", r[0],",",r[1]
print "xc, yc:", xc[0],",",xc[1]
print "alpha:", alpha
print    

print "found params:"
print "rx, ry:", rf[0],",",rf[1]
print "xc, yc:", xcf[0],",",xcf[1]
print "alpha:", alpha_f

# Plot data
pl.scatter(*Xn.T, label="noisy points")
pl.plot(*X.T, label="source ellipse")
pl.plot(*Xf.T, label="guessed ellipse")
pl.legend(loc="lower right")
pl.show()