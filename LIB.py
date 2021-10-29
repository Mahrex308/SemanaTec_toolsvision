import matplotlib.pyplot as plt
import numpy
from PIL import Image
from scipy import ndimage

# GaussBLur lo hizo Luis Fernando Gomez Benitez

def GaussBlur(sigma, K):
    A=numpy.zeros((K,K))
    for x in range(0,K):
        for y in range(0,K):
            A[x][y] = 1/(2*numpy.pi*sigma**2)*numpy.exp(-(x**2+y**2)/(2*sigma**2))

    return A

# MexicanHat lo hizo Raul Romero Martinez

def MexicanHat(sigma, K):
    A=numpy.zeros((K,K))
    for x in range(0,K):
        for y in range(0,K):
            A[x][y] = 1/(numpy.pi*sigma**4) * (1-(1/2)*((x**2+y**2)/(sigma**2))) * numpy.exp(-(x**2+y**2)/(2*sigma**2))
    return A

# LaplacianGauss lo hizo Brandon Hernandez Monroy

def LaplacianGauss(sigma, K):
    A=numpy.zeros((K,K))
    for x in range(0,K):
        for y in range(0,K):
            A[x][y] = -(1/(numpy.pi*sigma**4)) * (1-((x**2+y**2)/(2*sigma**2)))* numpy.exp(-(x**2+y**2)/(2*sigma**2))
    return A

# Laplace lo hizo Marino Olvera Camacho

def laplace(K):
    A=numpy.zeros((K,K))
    A[K//2][K//2] = 4
    A[K//2 + 1][K//2] = -1
    A[K//2 - 1][K//2] = -1
    A[K//2][K//2 + 1] = -1
    A[K//2][K//2 - 1] = -1
    return A

# TopSobel ya estaba hecho 

def TopSobel(K):
    A = numpy.zeros((K,K))
    A[K//2][K//2] = 0
    A[K//2 + 1][K//2] = -2
    A[K//2 - 1][K//2] = 2
    A[K//2][K//2 + 1] = 0
    A[K//2][K//2 - 1] = 0
    A[K//2 + 1][K//2 + 1] = -1
    A[K//2 + 1][K//2 - 1] = -1
    A[K//2 - 1][K//2 + 1] = 1
    A[K//2 - 1][K//2 - 1] = 1
    return A


