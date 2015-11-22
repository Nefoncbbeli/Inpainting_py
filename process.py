import numpy as np
import matplotlib.pyplot as plt
import copy
from params import params

def initProcess(source, editedSource, difference):
	tmp = np.ones((source.shape[0], source.shape[1], 1)) #One channel
	sourceRegion = copy.copy(tmp)
	targetRegion = copy.copy(tmp)
	fillFront    = copy.copy(tmp)
	# Force size_patch to be odd
	assert params['sizePatch'] % 2 == 1, "sizePatch must be odd"
	print('difference:', difference.shape)
	print(len(difference[::][::]))
	targetRegion = 1 if any(difference[::0]!=0, difference[::1]!=0, difference[::2]!=0) else 0

def run(source=None, editedSource=None):
	difference = source - editedSource
	initProcess(source, editedSource, difference)
	# print(np.amin(difference))
	# print(np.amax(difference))
	return difference
