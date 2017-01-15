import os
import matplotlib.pyplot as plt

opj = os.path.join
opd = os.path.dirname
opb = os.path.basename

databaseDir = opj(opd(opd(__file__)), 'Database')
outputDir   = opj(opd(opd(__file__)),'_outputDir')
debugDir    = opj(outputDir, 'debug')

def createOutputDir(outputDir):
	if not os.path.exists(outputDir):
		os.makedirs(outputDir)

def saveOutput(outputDir, img=None, imgName='image'):
	createOutputDir(outputDir)
	plt.imsave(opj(outputDir, '%s.png'%imgName), img)