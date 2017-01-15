import os
import matplotlib.pyplot as plt

syntheticsDirPath = r'C:\Users\adrie\Documents\Git\Inpainting\Database'

def saveOutput(outDir, img=None, imgName='image'):
	plt.imsave(os.path.join(outDir, '%s.png'%imgName), img)
