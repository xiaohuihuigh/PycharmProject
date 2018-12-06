import io

import os
import re
def listdir(path):
    list_name = []
    for file in os.listdir(path):
        file_path = os.path.join(path,file)
        if not os.path.isdir(file_path):
            list_name.append(file_path)
    return list_name
path = '/home/zyh/PycharmProjects/biquge'

def txt_file_list(list_name):
    pat = re.compile('\*\*')
    file_list = []
    for i in list_name:
        # print(i)
        if pat.findall(i):
            path,file_name = os.path.split(i)
            a,b = file_name.split('**')
            file_list.append((int(a),file_name))
    file_list.sort()
    print(file_list)
    for ti in file_list:
        a,file_name = ti
        print(file_name)
        with open(file_name,'r')as f:
            text = f.read()
        with open('all.txt','a+')as f:
            f.write('\n'+file_name+'\n')
            f.write(text)

list_name = listdir(path)
txt_file_list(list_name)