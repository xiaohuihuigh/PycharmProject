import PIL

from PIL import Image,ImageFilter,ImageOps
'''
clean the image used the method (if the point.value <143 value = 0 else value = 255)

update the image 
'''
def cleanImage(imagePath):
    image = Image.open(imagePath)
    image = image.point(lambda x: 0 if x<143 else 255)
    borderImage = ImageOps.expand(image,border=20,fill='white')
    borderImage.save(imagePath)
# cleanImage('validatecode.png')
# kitten = Image.open('validatecode.png')
# blurryKitten = kitten.filter(ImageFilter.GaussianBlur)
# blurryKitten.save('kitten_blurred.jpg')
# blurryKitten.show()

from generic_variables import *
import requests
import os
import time
valiurl = LoginUrl+ValidateCodeUrl

'''
get 100 validatecode pneg
'''
# for i in range(100):
#     with open(os.path.join('ValidateCodeDir',str(i)+'.jpeg'),'wb')as f:
#         f.write(requests.get(valiurl).content)
    # cleanImage(os.path.join('ValidateCodeDir',str(i)+'.jpeg'))
        # time.sleep(3)
# for i in range(1000):
#     os.remove(os.path.join('ValidateCodeDir',str(i)+'.png'))
'''
input the validatecode value
'''
# for i in range(100):
#     with open (os.path.join('ValidateCodeDir',str(i)+'.txt'),'wb')as f:
#         print i,'input the validate'
#         f.write(str(raw_input()))

# for i in range(100):
#     image = Image.open(os.path.join('ValidateCodeDir',str(i)+'.jpeg'),'r')
#     image.save(os.path.join('ValidateCodeDir',str(i)+'.tif'))
