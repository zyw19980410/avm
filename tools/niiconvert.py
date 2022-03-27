import os

import nibabel as nib
import nrrd
import numpy as np
'''
将当前文件夹下的nrrd文件转换成nii
'''
def convert(data_path, save_path):
    data, options = nrrd.read(data_path)  # 读取 nrrd 文件
    img = nib.Nifti1Image(data, np.eye(4))  # 将 nrrd 文件转换为 .nii 文件
    nib.save(img, save_path)  # 保存 nii 文件


temp = os.listdir('./')
nrrdlist = []
for nrrd in temp:
    if 'nrrd' in nrrd:
        nrrdlist.append(nrrd)
for file in nrrdlist:
    print(file)
    convert(file, file.replace('nrrd', 'nii'))
