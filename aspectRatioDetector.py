from scipy import fftpack
import numpy as np
import pylab as py
from PIL import Image
from numpy import array
img = Image.open("rose-wide.png").convert('L')
arr = array(img)

# Take the fourier transform of the image.
F1 = fftpack.fft2(arr)

# Now shift so that low spatial frequencies are in the center.
F2 = fftpack.fftshift( F1 )

# the 2D power spectrum is:
psd2D = np.abs( F2 )**2

# plot the power spectrum
py.figure(1)
py.clf()
py.imshow( psd2D )
py.show()