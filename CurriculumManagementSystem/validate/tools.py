#coding:utf-8
import os
import re
from PIL import  Image
import subprocess

def depoint(img): #input: gray image
    pixdata = img.load()
    w,h = img.size
    lo = 120
    for y in range(2,h-2):
        for x in range(2,w-2):
            count = 0
            if pixdata[x,y-2] > lo:
                count = count + 1
            if pixdata[x,y+2] > lo:
                count = count + 1
            if pixdata[x-2,y] > lo:
                count = count + 1
            if pixdata[x+2,y] > lo:
                count = count + 1
        if count > 2:
            img.putpixel((x,y),255)
            # pixdata[x,y] = 255
    return img



'''
get binarized img
'''
def clean_Image(filepath,newfilepath):
    image = Image.open(filepath)
    pixdata = image.load()
    # print pixdata[3, 3]

    image = image.convert('L')#gray img
    image = image.point(lambda x:0 if x<155 else 255)#binarizing
    # pixdata = image.load()
    # print pixdata[3, 3]
    # binarizing(image,300)
    image.save(newfilepath)

'''
get the binarized image file from gray image file
get the oldImgfiles compile and the newImgfiles suffix'''

def gray_to_binary(comp,suffix):
    for i in os.listdir(os.getcwd()):
        filename ,fileext = os.path.splitext(i)
        # comp = re.compile(r'.{5}d$')
        if comp.findall(filename):
            image = Image.open(i)
            image = image.point(lambda x:0 if x<155 else 255)
            image.save(filename+suffix)

# for i in os.listdir(os.getcwd()):
#     filename,fileext = os.path.splitext(i)
#     if fileext =='.jpeg':
#         clean_Image(i,filename+'t.tif')

# for i in os.listdir(os.getcwd()):
#     filename,fileext = os.path.splitext(i)
#     compile = re.compile(r'.{4}L$')
#     if fileext == '.tif' and compile.findall(filename):
#         #print filename
        # image=  Image.open(i)
        # for i in range(100):
        #     image = depoint(image)
        # image.save(filename+'d.tif')


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

'''
 种子染色法
'''
def get_a_block(recording,image,x,y):
    p = {}
    p[0] = 0
    w,h = image.size
    def dfs(x,y):
        p[0] = p[0] +1
        pixdata = image.road()

        if y+1<h and pixdata[x,y+1] == 0 and recording[x][y+1] == 0:
            recording[x][y+1] = 1
            dfs(x,y+1)
        if x+1<w and pixdata[x+1,y] == 0 and recording[x+1][y] == 0:
            recording[x+1][y] = 1
            dfs(x+1,y)
    return recording,p[0]
if __name__ == '__main__':
    image = Image.open('5rfBLdb.tif')
    w,h = image.size
    recording = [[0] * h for i in range(w)]
    pixdata = image.load()
    dict_block = {}
    num = 0
    for y in range(h):
        for x in range(w):
            if recording[x][y] == 0 and pixdata[x,y] == 0:
                recording,num = get_a_block(recording,image,x,y)
            dict_block[(x,y)] = num
    print dict_block
    print recording