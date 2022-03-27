import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
'''
dice变化图，以及roc图
'''
f = np.load("data.npz", allow_pickle=True)
x_label = list(range(0, len(f["arr_0"])))
mass_dice = [i[0] for i in f["arr_0"]]
vein_dice = [i[1] for i in f["arr_0"]]
fig, axes = plt.subplots(1, 2)
axes[0].set(title="val_mass_dice", ylim=[0, 1])
axes[1].set(title="val_vein_dice", ylim=[0, 1])
axes[0].plot(x_label, mass_dice)
axes[1].plot(x_label, vein_dice)
plt.show()
fig, axes = plt.subplots(2, 2)
axes[0][0].set(title="valTN")
axes[0][1].set(title="valFP")
axes[1][0].set(title="valFN")
axes[1][1].set(title="valTP")

tp = []
fn = []
fp = []
tn = []
total_val_pre = f["arr_1"]
total_val_lab = f["arr_2"]
for i in range(0, len(total_val_pre)):
    temptn, tempfp, tempfn, temptp = confusion_matrix(total_val_pre[i], total_val_lab[i]).ravel()

    tp.append(temptp)
    tn.append(temptn)
    fn.append(tempfn)
    fp.append(tempfp)
    sum = 0
    for j in total_val_pre[i]:
        sum += j
    print("val set len is :" + str(len(total_val_pre[i])) + "    true label count is :" + str(sum) + "fp + tn is :" + str(
        tempfp + temptn))
axes[0][0].plot(x_label, tn)
axes[0][1].plot(x_label, fp)
axes[1][0].plot(x_label, fn)
axes[1][1].plot(x_label, tp)
plt.show()


fig, axes = plt.subplots(2, 2)
axes[0][0].set(title="trainTN")
axes[0][1].set(title="trainFP")
axes[1][0].set(title="trainFN")
axes[1][1].set(title="trainTP")
tp = []
fn = []
fp = []
tn = []
total_val_pre = f["arr_3"]
total_val_lab = f["arr_4"]
for i in range(0, len(total_val_pre)):
    temptn, tempfp, tempfn, temptp = confusion_matrix(total_val_pre[i], total_val_lab[i]).ravel()

    tp.append(temptp)
    tn.append(temptn)
    fn.append(tempfn)
    fp.append(tempfp)
    sum = 0
    for j in total_val_pre[i]:
        sum += j
    print("train set len is :" + str(len(total_val_pre[i])) + "     true label count is :" + str(sum) + "fp + tn is :" + str(
        tempfp + temptn))
axes[0][0].plot(x_label, tn)
axes[0][1].plot(x_label, fp)
axes[1][0].plot(x_label, fn)
axes[1][1].plot(x_label, tp)
plt.show()