# PYTHON IMPORT 
import os
import numpy as np
import matplotlib.pyplot as plt
import json
import logging
logging.basicConfig(format='%(levelname)s: %(message)s',level=logging.DEBUG)

# PERSONAL IMPORT 
import process
import utils
with open('params.json') as params_file:
	params = json.load(params_file)

def getInputs(plot=False):
	sourcePath        = os.path.join(utils.databaseDir, 'c.ppm')
	editedSourcePath  = os.path.join(utils.databaseDir, 'd.ppm')
	sourceArray       = np.array(plt.imread(sourcePath      ))
	editedSource = np.array(plt.imread(editedSourcePath))
	if plot:
		plt.imshow(sourceArray)
		plt.title('Source')
		plt.axis('off')
		plt.show()
		plt.imshow(editedSource)
		plt.title('SourceEdited')
		plt.show()
	return sourceArray, editedSource

"""Main fonction

This is the main
"""
if __name__ == '__main__':
	logging.info('Start main')
	source, editedSource = getInputs(plot=False)
	process.run(params, source, editedSource)
	logging.info('End main')