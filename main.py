import matplotlib.pyplot as plt
import numpy

from PIL import Image
from scipy import ndimage

from LIB import *

imgIS = Image.open('Warriors.jpg')
I  = imgIS.convert('L')
I  = numpy.asarray(I)
I  = I / 255.0

# Padding
def pad_with(vector, pad_width, iaxis, kwargs):
    pad_value = kwargs.get('padder', 10)
    vector[:pad_width[0]] = pad_value
    vector[-pad_width[1]:] = pad_value

I = numpy.pad(I, 10, pad_with, padder=0)

kernelTS = TopSobel(3) 
kernelGB = GaussBlur(9,9) 
kernelMH = MexicanHat(3,9) 
kernelLA = laplace(9) 
kernelLG = LaplacianGauss(9,9)

imgTS = ndimage.convolve(I, kernelTS, mode='constant', cval=0.0)
imgGB = ndimage.convolve(I, kernelGB, mode='constant', cval=0.0) 
imgMH = ndimage.convolve(I, kernelMH, mode='constant', cval=0.0)
imgLA = ndimage.convolve(I, kernelLA, mode='constant', cval=0.0)
imgLG = ndimage.convolve(I, kernelLG, mode='constant', cval=0.0)


plt.figure(figsize = (15, 15))

plt.subplot(3, 2, 1)
plt.imshow(imgIS)
plt.xlabel('Input Image')

plt.subplot(3, 2, 2)
plt.imshow(imgTS)
plt.xlabel('Image | Top Sobel')

plt.subplot(3, 2, 3)
plt.imshow(imgGB)
plt.xlabel('Image | Gaussian Blur')

plt.subplot(3, 2, 4)
plt.imshow(imgMH)
plt.xlabel('Image | Ricker Wavelet - Mexican Hat')

plt.subplot(3, 2, 5)
plt.imshow(imgLA)
plt.xlabel('Image | Laplacian')

plt.subplot(3, 2, 6)
plt.imshow(imgLG)
plt.xlabel('Image | Laplacian Gauss')

plt.grid(False)
plt.show()

