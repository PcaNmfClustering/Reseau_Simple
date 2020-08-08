from math import exp,tanh

def sigmoide(val):
    return 1 / (1 + exp(-1 * val))

def tangente(val):
    return 1.7159 * tanh((2/3)*val)
