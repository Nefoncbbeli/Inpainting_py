import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

image_file = os.path.join(os.path.dirname(__file__),'c.ppm')
image = plt.imread(image_file)
imageNP=np.array(image)
print(imageNP.shape)

# plt.imshow(image)
# plt.axis('off')  # clear x- and y-axes
# plt.show()
print("Hello World")



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