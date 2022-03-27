# from sympy import true
from tkinter.tix import FileSelectBox
import torch
import numpy as np
import os
# t=[1,2,3,4,5,6,7]
# q=[3,3,3,3,3,3]
# np.savez("data.npz",t,q)
'''
该文件没有意义，用于测试如何使用npz文件
'''

train = np.load("data1.npz",allow_pickle=True)["arr_0"].tolist()
val = np.load("data1.npz",allow_pickle=True)["arr_1"].tolist()
s = set()
for i in val:
    if i in s:
        continue
    else:
        s.add(i)
for i in train:
    if i in s:
        continue
    else:
        s.add(i)
temp = os.listdir("/media/zyw/本地磁盘/nnUNet-master/nnUNet_raw/nnUNet_raw_data/Task001_one/labelsTr")
files=[]
for i in temp:
    files.append(i.split('.')[0])
sum = 0
print(files)
for i in s:
    if i in files:
        files.remove(i)
    else:
        sum += 1
        print("extra file :" + i)
print(sum)