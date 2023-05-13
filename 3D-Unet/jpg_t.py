import PIL.Image
import os
i=0
path = "/Users/lijingyi/Desktop/npy_test/imgs/"
savepath = "/Users/lijingyi/Desktop/npy_test/imgs/jpg/"
filelist = os.listdir(path)
for file in filelist:
    im = PIL.Image.open(path+filelist[i])
    filename = os.path.splitext(file)[0]
    im.save(savepath+filename+'.jpg') # or 'test.tif'
    i=i+1

