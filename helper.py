import matplotlib.pyplot as plt
from sklearn.utils.multiclass import unique_labels
from sklearn.metrics import confusion_matrix
import numpy as np

def get_labels():
    return [
        '1',
        '2',
        '67',
        '79',
        '12',
        '143',
        '38',
        '125',
        '151',
        '191',
    ]

def convert_label_cat1(x):
    convert = {
        '1' : 0,
        '2' : 1,
        '67' : 2,
        '79' : 3,
        '12' : 4,
        '143' : 5,
        '38' : 6,
        '125' : 7,
        '151' : 8,
        '191' : 9
    }
    return convert[str(x)]

def unconvert_label_cat1(x):
    unconvert = [
        '1',
        '2',
        '67',
        '79',
        '12',
        '143',
        '38',
        '125',
        '151',
        '191',
    ]
    return unconvert[int(x)]


def plot_confusion_matrix(y_true, y_pred, classes,
                          normalize=False,
                          title=None,
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if not title:
        if normalize:
            title = 'Normalized confusion matrix'
        else:
            title = 'Confusion matrix, without normalization'

    # Compute confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    # Only use the labels that appear in the data
    temp = list(map(int,unique_labels(y_true, y_pred)))
    classes = list(map(int,unique_labels(y_true, y_pred)))
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

#     print(cm)

    fig, ax = plt.subplots()
    im = ax.imshow(cm, interpolation='nearest', cmap=cmap)
    ax.figure.colorbar(im, ax=ax)
    # We want to show all ticks...
    ax.set(xticks=np.arange(cm.shape[1]),
           yticks=np.arange(cm.shape[0]),
           # ... and label them with the respective list entries
           xticklabels=classes, yticklabels=classes,
           title=title,
           ylabel='True label',
           xlabel='Predicted label')

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], fmt),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")
    fig.tight_layout()
    return ax



labels_cat2 = [
 209,
 4,
 68,
 213,
 37,
 47,
 13,
 69,
 5,
 137,
 124,
 136,
 14,
 221,
 131,
 3,
 24,
 30,
 138,
 73,
 19,
 217,
 186,
 173,
 51,
 142,
 45,
 18,
 46,
 81,
 140,
 135,
 50,
 48,
 150,
 189,
 133,
 134,
 233,
 196,
 153,
 132,
 152,
 202,
 39,
 165,
 141,
 192,
 200,
 197,
 199,
 232,
 194,
 195,
 139,
 70,
 193,
 198,
 201]


def convert_label_cat2(x):
    return labels_cat2.index(int(x))


def unconvert_label_cat2(x):
    return labels_cat2[int(x)]
