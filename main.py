import matplotlib.pyplot as plt
from convolucion_gauss import I
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

