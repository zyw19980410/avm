import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, datasets
from sklearn.metrics import roc_curve, auc  ###计算roc和auc

y_label = []
y_score = []
y_label = np.load("data.npz",allow_pickle=True)["arr_1"].tolist()[-1]
y_score = np.load("data.npz",allow_pickle=True)["arr_2"].tolist()[-1]
fpr, tpr, thersholds = roc_curve(y_label, y_score, pos_label=1)
print('----------------------')
print('假阳率\t真阳率\t阈值')
for i, value in enumerate(thersholds):
    print("%f %f %f" % (fpr[i], tpr[i], value))
print('----------------------')

roc_auc = auc(fpr, tpr)

plt.plot(fpr, tpr, 'k--', label='ROC (area = {0:.2f})'.format(roc_auc), lw=2)
plt.xlim([-0.05, 1.05])  
plt.ylim([-0.05, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')  
plt.title('ROC Curve')
plt.legend(loc="lower right")
plt.show()