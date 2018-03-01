
import itertools
import numpy as np
import matplotlib.pyplot as plt


def _cor(cor):
    cores = {
        'vermelho': '\033[31m',
        'verde': '\033[32m',
        'azul': '\033[34m',
        'ciano': '\033[36m',
        'magenta': '\033[35m',
        'amarelo': '\033[33m',
        'preto': '\033[30m',
        'branco': '\033[37m',
        'original': '\033[0;0m',
        'reverso': '0\33[2m',
        '': '\033[0;0m',
    }
    return cores[cor]

def porcentagem(_indice, n):
    por = (_indice*100)/n
    log = '\033[32m'+'(%i:%i) \033[0;0m<>\033[34m [ %.2f%s ] ''\033[0;0m' %(_indice,n,por,'%')
    #print(log)
    return log


def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    print('vendo classes')
    print(type(classes))
    print(classes)
    print('end-----end')

    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

"""
# Compute confusion matrix
cnf_matrix = confusion_matrix(y_test, y_pred)
np.set_printoptions(precision=2)

# Plot non-normalized confusion matrix
plt.figure()
plot_confusion_matrix(cnf_matrix, classes=class_names,
                      title='Confusion matrix, without normalization')

# Plot normalized confusion matrix
plt.figure()
plot_confusion_matrix(cnf_matrix, classes=class_names, normalize=True,
                      title='Normalized confusion matrix')

plt.show()
"""