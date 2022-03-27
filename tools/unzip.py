import zipfile
import shutil
import zipfile
import os
'''
将当前文件夹下mrb文件解压，提取出nrrd文件
'''
temp = os.listdir('./')
mrblist = []
for mrb in temp:
    print(mrb)
    if 'mrb' in mrb:
        mrblist.append(mrb)
print(mrblist)
for file in mrblist:
    zip_file = zipfile.ZipFile(file)
    zip_list = zip_file.namelist()  # 得到压缩包里所有文件
    sum = 0
    for f in zip_list:
        if 'nrrd' in f:
            sum += 1
    if sum > 2:
        continue
    for f in zip_list:
        if 'nrrd' in f:

            print(f)
            if 'segmentation.' in f or 'Segmentation.' in f or 'Seg.' in f or 'seg.' in f:
                if not os.path.exists('%s_segment.nrrd' % f.split('/')[0][0:3]):
                    zip_file.extract(f, './')
                    shutil.move(f, './')
                    os.rename(f.split('/')[-1], '%s_segment.nrrd' % f.split('/')[0][0:3])
            else:
                if not os.path.exists('%s_train.nrrd' % f.split('/')[0][0:3]):
                    zip_file.extract(f, './')
                    shutil.move(f, './')
                    os.rename(f.split('/')[-1], '%s_train.nrrd' % f.split('/')[0][0:3])

    zip_file.close()  # 关闭文件，必须有，释放内存
# temp=os.listdir('./')
# nrrdlist=[]
# for nrrd in temp:
#     if 'nrrd' in nrrd:
#         nrrdlist.append(nrrd)
# for file in nrrdlist:

#     print(file)
#     convert(file,file.replace('nrrd','nii'))
