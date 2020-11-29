from painter import *

mat=np.zeros((7,8))
for i in range(7):
    for j in range(8):
        if (i+j)%2==0:
            mat[i,j]=1
        else:
            mat[i,j]=-1

xlabel = ('1 2 3','1','1','1','1','1','1','1')
ylabel = ('1','1','1','1','1','1','1')

paint_map(mat, xlabel, ylabel,"test.jpg")