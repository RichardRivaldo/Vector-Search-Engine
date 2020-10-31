# Basic Vector Operations

# Libraries
import math

# Vector Dot Product
# If v = [2, 4] and w = [3, 1], then zip(v, w) = [(2, 3), (4, 1)]
def dot(v,w):
    return sum(v_i * w_i for (v_i, w_i) in zip(v,w))

# Vector Sum of Squares
def sumofsq(v):
    return dot(v,v)

# Vector Magnitude
def magnitude(v):
    return math.sqrt(sumofsq(v))

# Cosine Similarity
def cosine_similarity(v, w):
    vdotw = dot(v, w)
    normv = magnitude(v)
    normw = magnitude(w)
    return (vdotw / (normv * normw))

# Other Vector Operations

# Vector Addition
def add(v,w):
    return [(a+b) for a,b in zip(v,w)]

# Vector Substraction
def substract(v,w):
    return [(a-b) for a,b in zip(v,w)]

# Vector Scalar Product
def scalar(c,v):
    return [c * v_i for v_i in v]

# Vector Distance
def distance(v,w):
    return magnitude(substract(v,w))


"""
import numpy as np

A = np.array([1, 2, 3])
B = np.array([3, 2, 5])
print(cosine_similarity(A, B))
"""