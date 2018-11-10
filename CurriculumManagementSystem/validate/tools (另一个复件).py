import os
from PIL import  Image
import subprocess
def binarizing(img,threshold):#input: gray image
    pixdata = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            print pixdata[x,y]
            if pixdata[x, y] < threshold:
                pixdata[x, y] = 0
            else:
                pixdata[x, y] = 255*3
    return img



def clean_Image(filepath,newfilepath):
    image = Image.open(filepath)
    pixdata = image.load()
    # print pixdata[3, 3]
    image = image.convert('L')
    image = image.point(lambda x:0 if x<164 else 255)

    # pixdata = image.load()
    # print pixdata[3, 3]
    # binarizing(image,300)
    image.save(newfilepath)
for i in os.listdir(os.getcwd()):
    filename,fileext = os.path.splitext(i)
    if fileext =='.jpeg':
        clean_Image(i,filename+'t.tif')
# for i in os.listdir(os.getcwd()):
#     # print os.path.splitext(i)
#     if os.path.splitext(i)[1] == '.tif':
#         if i =='merge.tif':
#             continue
#         os.system('tesseract '+i+' output -l fontyp -psm 7')
#         with open ('ans.txt','a+')as f:
#             with open('output.txt','r')as fr:
#                 reads = fr.readline()
#                 print str(os.path.splitext(i)[0])+"   "+str(reads)
#                 f.write(str(os.path.splitext(i)[0])+str(reads))
#                 f.write("\n")