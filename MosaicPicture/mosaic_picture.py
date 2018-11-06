import etc
import os
from PIL import Image
Image.MAX_IMAGE_PIXELS = 1000000000
data_path = etc.data_path
ims = [Image.open(os.path.join(data_path,fn)) for fn in os.listdir(data_path)]
rw,rh = ims[0].size
rh=0
t = 0
for im in ims:
    if t >0:
        t-=1
        continue
    iw,ih = im.size
    rh+=ih
result = Image.new(ims[0].mode,(rw,rh))
h = 0
t = 0
for im in ims:
    if t >0:
        t-=1
        continue
    result.paste(im,box=(0,h))
    print im
    iw,ih = im.size
    h+=ih
# result.show()
result.save(os.path.join(data_path,'result.png'))