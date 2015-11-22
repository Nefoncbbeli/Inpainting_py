import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import process

# Global parameters
syntheticsDirPath = r'F:\GitHub\Database\Synthetics'

def getInputs(plot=False):
	sourcePath        = os.path.join(syntheticsDirPath, 'c.ppm')
	editedSourcePath  = os.path.join(syntheticsDirPath, 'd.ppm')
	sourceArray       = np.array(plt.imread(sourcePath      ))
	editedSourceArray = np.array(plt.imread(editedSourcePath))
	if plot:
		plt.imshow(sourceArray)
		plt.axis('off')
		plt.show()
	return sourceArray, editedSourceArray

def saveOutputs(diff=None):
	if not diff==None:
		plt.imsave(os.path.join(syntheticsDirPath, 'diff.png'), diff)
	return 0

if __name__ == '__main__':
	source, editedSource = getInputs()
	difference = process.run(source, editedSource)
	saveOutputs(difference)
	print('ok')

##Heart of C code.
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
# 		update_targetregion(&SRC_prec,&cpt2);
# 		//cout << "Debug_update_targetregion\n";
# 		update_fillfront();
# 		//cout << "Debug_update_fillfront\n";
# 		update_sourceregion();
# 		//cout << "Debug_update_sourceregion\n";
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