# PYTHON IMPORT 
import numpy as np
import matplotlib.pyplot as plt
import scipy
import logging as log
from scipy import ndimage
import copy

# PERSONAL IMPORT
import utils

syntheticsDirPath = utils.syntheticsDirPath# r'C:\Users\adrie\Documents\Git\Inpainting\Database'


def test():
	t  = np.array(range(12)).reshape(2,2,3)
	tz = np.zeros(12).reshape(2,2,3)
	tr = np.zeros(4).reshape(2,2)
	tz[0,1,1]=1
	print(tz)
	print('*'*50)
	print(tr)
	print('*'*50)
	# for z in range(3):
	for y in range(2):
		for x in range(2):
			# if any([tz[0,y,x], tz[1,y,x], tz[2,y,x]]):
			if tz[x,y,:].any():
				tr[x,y]=1
	print(tr)
	print(tr[:,:].any())
	exit()

"""[summary]

[description]
"""
def initProcess(params, source, editedSource, difference):
	w, h = source.shape[0], source.shape[1]
	tgtRegion = np.ones(w * h).reshape(w, h)
	srcRegion = np.ones(w * h).reshape(w, h)
	fillFront    = np.ones(w * h).reshape(w, h)
	# Force size_patch to be odd
	assert params['sizePatch'] % 2 == 1, "sizePatch must be odd"
	log.debug('sizePatch:%s'% params['sizePatch'] )
	# Fill targerRegion
	for y in range(h):
		for x in range(w):
			tgtRegion[x,y] = 1 if difference[x,y,:].any() else 0
	nbPoint = np.sum(tgtRegion)
	log.info('nbPoints: %d'%nbPoint)
	# # Initialisation of source_region
	log.debug('tgtRegion.dtype: %s'% tgtRegion.dtype)
	sizeDilate = params['sizeDilate']
	sizeErode = params['sizeErode']
	log.debug('sizeDilate:%s '% sizeDilate)
	structureDilate = np.ones((sizeDilate, sizeDilate))
	structureErode  = np.ones((sizeErode, sizeErode))
	tgtRegionDilated = ndimage.binary_dilation(tgtRegion, structure=structureDilate).astype(tgtRegion.dtype)
	tgtRegionEroded  = ndimage.binary_erosion(tgtRegion , structure=structureErode ).astype(tgtRegion.dtype)
	fillFront = tgtRegionDilated - tgtRegionEroded
	utils.saveOutput(syntheticsDirPath, tgtRegion, 'tgtRegion')
	utils.saveOutput(syntheticsDirPath, tgtRegionDilated, 'tgtRegionDilated')
	utils.saveOutput(syntheticsDirPath, tgtRegionEroded, 'tgtRegionEroded')
	utils.saveOutput(syntheticsDirPath, fillFront, 'fillFront')
	return fillFront, tgtRegion, srcRegion, nbPoint
	# source_region=tmp3.dilate(size_dilate,size_dilate)-tgt_region;

def inpaint(fillFront, tgtRegion, srcRegion, nbPoint):
	log.info('WTF?!')
	while (nbPoint != 0):
		getMaxPatch()
		findExemplarPatch()
		fillPatch()
		updateTgtRegion()
		updateFillFront()
		updateSrcRegion()
		updatePp()

# void Pima::run(const char * outputName)
# {
# 	unsigned int IPS(0),JPS(0),IS(0),JS(0),cpt(0);
# 	double Cprec(0.0);
# 	float cpt2(0.9);
# 	CImg<unsigned char> SRC_prec(srcToFillRGB);
# 	SRC_prec.fill(0);
# 	initialize_Pp();
# 	my_display(cpt);
# 	while(nb_points!=0)
# 	{	
# 		cpt++;
# 		Cprec=get_maxPatch(&IPS,&JPS);
# 		srcToFillCIE=srcToFillRGB.get_RGBtoLab();
# 		//cout << "Debug_srcToFillCIE\n";
# 		find_exemplar_Patch(IPS,JPS,&IS,&JS);
# 		//cout << "Debug_find_exemplar_Patch\n";
# 		SRC_prec=srcToFillRGB;
# 		fill_patch(IPS,JPS,IS,JS);
# 		//cout << "Debug_fill_patch\n";
# 		update_tgtregion(&SRC_prec,&cpt2);
# 		//cout << "Debug_update_tgtregion\n";
# 		update_fillfront();
# 		//cout << "Debug_update_fillfront\n";
# 		update_srcRegion();
# 		//cout << "Debug_update_srcRegion\n";
# 		update_Pp(IPS,JPS,Cprec);

# 		if (cpt%20==0)
# 		{
# 			//my_display(cpt);   //Décommenter pour afficher le résultat toutes les 20 itérations!
# 		}
# 	}
# 	my_display(cpt);
# 	cout << "ouputName : " << outputName << "\n";
# 	srcToFillRGB.save(outputName, -1);
# }




"""[summary]

[description]
"""
def run(params, source=None, editedSource=None):
	# test()
	difference = source - editedSource
	fillFront, tgtRegion, srcRegion, nbPoint = initProcess(params, source, editedSource, difference)
	inpaint(fillFront, tgtRegion, srcRegion, nbPoint)
	# print(np.amin(difference))
	# print(np.amax(difference))
	return difference
