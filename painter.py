import numpy as np
import matplotlib
from matplotlib import pyplot as plt 
color1=(1,1,1)
color2=(0,0,0)

def paint_map(mat, xlabel, ylabel, figname):

    xsize = mat.shape[0]
    ysize = mat.shape[1]

    plt.figure(figsize=(10, 10))
    my_cmap=matplotlib.colors.LinearSegmentedColormap.from_list('my_camp',[color1,color2],2)
    cs=plt.imshow(mat,cmap=my_cmap)
    
    plt.xticks(np.linspace(0,ysize,ysize,endpoint=False),xlabel,fontsize=20,rotation=300)
    plt.yticks(np.linspace(0,xsize,xsize,endpoint=False),ylabel,fontsize=20)
    plt.tick_params(bottom=False,left=False,labeltop=False,labelright=False,labelleft=True,labelbottom=True)
    plt.savefig(figname)