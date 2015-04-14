# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import numpy

# <codecell>

from matplotlib.pyplot import plot, show, legend

# <codecell>

from math import exp

# <codecell>

@numpy.vectorize
def morse(r, r0=0.5, a=1.5, d=2.5):
    e = exp(-a*(r-r0))
    return d*(1-e)**2

# <codecell>

rs = numpy.linspace(0, 10, 100)

# <codecell>

Vs = numpy.array([morse(r) for r in rs])

# <codecell>

%matplotlib inline

# <codecell>

plot(rs, Vs)

# <codecell>

import scipy.optimize

# <codecell>

scipy.optimize.brent(morse)

# <codecell>

scipy.optimize.fmin_cg(morse, [1])

# <codecell>

@numpy.vectorize
def grad_morse(r, r0=0.5, a=1.5, d=2.5):
    e = exp(-a*(r-r0))
    return 2*d*(1-e)*e*a

# <codecell>

scipy.optimize.fmin_cg(morse, [1], fprime=grad_morse)

# <codecell>

def hess_morse(r, r0=0.5, a=1.5, d=2.5):
    e = exp(-a*(r-r0))
    return 2*d*(2*e-1)*e*a*a

# <codecell>

scipy.optimize.fmin_ncg(morse, [1], fprime=grad_morse)

# <codecell>

scipy.optimize.fmin_ncg(morse, [1], fprime=grad_morse, fhess=hess_morse)

# <codecell>

scipy.optimize.fmin_bfgs(morse, [1], fprime=grad_morse)

# <codecell>

scipy.optimize.fmin_l_bfgs_b(morse, [1], fprime=grad_morse)

# <markdowncell>

# **Curve fitting**

# <codecell>

def morse(r, r0=0.5, a=1.5, d=2.5):
    e = numpy.exp(-a*(r-r0))
    return d*(1-e)**2

# <codecell>

rs = numpy.arange(0, 5, .1)
Vs = morse(rs) + 0.01*numpy.random.normal(size=len(rs))

# <codecell>

scipy.optimize.curve_fit(morse, rs, Vs)

# <markdowncell>

# **Least square**

# <codecell>

x = numpy.arange(0, 10, .1)

# <codecell>

k0=3; l0=1

# <codecell>

y = k0*x + l0 + 0.1*numpy.random.random(size=len(x))

# <codecell>

def resid(p, y, x):
    k, l = p
    return y - k*x - l

# <codecell>

p0 = numpy.array([k0, l0])
scipy.optimize.leastsq(resid, p0, args=(y, x))

# <codecell>


