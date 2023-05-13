import numpy as np
import imageio
import os
from PIL import Image

img = Image.open('/Users/lijingyi/Desktop/npy_test/imgs/').convert('RGB')

os.chdir('/Users/lijingyi/Desktop/npy_test/imgs/')     #切换python工作路径到你要操作的图片文件夹，mri_2d_test为我的图片文件夹
a=np.ones((446,480,480))    #利用np.ones()函数生成一个三维数组，当然也可用np.zeros，此数组的每个元素a[i]保存一张图片
i=0
for filename in os.listdir("/Users/lijingyi/Desktop/npy_test/imgs/"):  #使用os.listdir()获取该文件夹下每一张图片的名字
	im=imageio.imread(filename)
	a[i]=im
	i=i+1
	if(i==446):   #190为文件夹中的图片数量
		break
np.save('Users/lijingyi/Desktop/npy_test/imgs_npy',a)

