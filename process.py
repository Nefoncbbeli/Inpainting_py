import numpy as np
import matplotlib.pyplot as plt

def run(source=None, editedSource=None):
	difference = source - editedSource
	print(np.amin(difference))
	print(np.amax(difference))
	return difference
