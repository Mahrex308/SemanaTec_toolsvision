import matplotlib.pyplot as plt
import numpy

from PIL import Image
from scipy import ndimage

from LIB import *

Is = Image.open('Warior.jpeg')
I  = Is.convert('L')
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

imgTS = ndimage.convelve(I, kernelTS, mode='constant', cval=0.0)
imgGB = ndimage.convelve(I, kernelGB, mode='constant', cval=0.0) 
imgMH = ndimage.convelve(I, kernelMH, mode='constant', cval=0.0)
imgLP = ndimage.convelve(I, kernelLA, mode='constant', cval=0.0)
imgLG = ndimage.convelve(I, kernelLG, mode='constant', cval=0.0)

