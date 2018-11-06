import os
# for i in range(100):
#     os.remove(str(i)+'.txt')
    # with open(str(i)+'.txt','r')as f:
    #     name = f.read()
    # print name
    # os.rename(str(i)+'.jpeg',name+'.jpeg')
    # os.rename(str(i)+'.tif',name+'.tif')
for i in os.listdir(os.getcwd()):
    # print os.path.splitext(i)
    if os.path.splitext(i)[1] == '.tif':
        if i =='merge.tif':
            continue
        os.system('tesseract '+i+' output -l fontyp -psm 7')
        with open ('ans.txt','a+')as f:
            with open('output.txt','r')as fr:
                reads = fr.readline()
                print str(os.path.splitext(i)[0])+"   "+str(reads)
                f.write(str(os.path.splitext(i)[0])+str(reads))
                f.write("\n")