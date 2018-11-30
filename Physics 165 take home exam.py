# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 12:13:40 2018

@author: Matthew
"""

#plot for the aperture

import numpy as np
import matplotlib.pyplot as plt

N = 100                    #higher N means higher resolution but will result in a weird diffraction pattern
A = np.zeros((N,N))

x = np.linspace(-2,2,N)
y = x

xx , yy = np.meshgrid(x, y)

#student number is 43009 therefore the transmittance of the outer ring is 40% while the inner ring is 30%

r1 = 0.4                  #radius of the bigger circle
r2 = 0.1               #radius of the smaller circle
                          #the width of the larger circle should be 20 percent of the aperture plane

c1 = np.where(xx**2 + yy**2 <= r1)
c2 = np.where(xx**2 + yy**2 <=r2  )

A[c1] = 0.4
A[c2] = 0.3

print("\nAperture plot:")

plt.imshow(A, cmap='gray', vmin=0, vmax=2)
plt.colorbar()
plt.axis('off')

plt.show()

#computing for the diffraction pattern using fast fourier transform for 2d

from numpy.fft import fft2, fftshift

FA = np.abs(fftshift(fft2(A)))

print("\nDiffraction pattern: ")

plt.imshow(FA,cmap='afmhot', vmin=0, vmax=300)
plt.colorbar()
plt.axis('off')
plt.show()


