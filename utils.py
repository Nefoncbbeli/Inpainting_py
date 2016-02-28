import os
import matplotlib.pyplot as plt

def saveOutput(outDir, img=None, imgName='image'):
	plt.imsave(os.path.join(outDir, '%s.png'%imgName), img)
