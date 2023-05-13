import os
from PIL import Image

dirname_read="/Users/lijingyi/Desktop/npy_test/imgs/"
dirname_write="/Users/lijingyi/Desktop/npy_test/imgs/imgs_jpg/"
names=os.listdir(dirname_read)
count=0
for name in names:
    img = Image.open(dirname_read+name)
    name=name.split(".")
    if name[-1] == "png":
        name[-1] == "jpg"
        name = str.join(".",name)
        to_save_path = dirname_write +name
        img = img.convert('RGB')
        img.save(to_save_path)
        count+=1
        print(to_save_path,"---count:",count)
    else:
        continue