import numpy as np
import cv2
from numpy import linalg as la
import statistics
import matplotlib.pyplot as plt

A = np.zeros([10304, 320]) 
cale = r'm0Poze'

for i in range(1, 41): 
    caleFolderPers = cale + '\s' + str(i) + '\\'
    for j in range(1, 9):
        calePozaAntrenare = caleFolderPers + str(j) + '.pgm'
        print(calePozaAntrenare) 

        pozaAnt = np.array(cv2.imread(calePozaAntrenare, 0))
        pozaAnt = np.array(pozaAnt)
        print(pozaAnt)

        pozaVectorizata = pozaAnt.reshape(-1, 1)
        A[:, j] = pozaVectorizata[:, 0]

        A[:, 8 * (i - 1) + j - 1] = pozaVectorizata[:, 0]

print(A[:, 2])
img = A[:, 2]
poza = np.reshape(img, (112, 92))
print(np.reshape(img, (112, 92)))

dictNorma = {'1': 1, '2': 2, 'inf': np.inf, 'cos': np.cos(180)}

def  KNN(A, poza, norma):
    poza = poza.reshape(-1, )
    col = len(A[:, 2])
    z = np.zeros((len(A[0]),), dtype=float)
    print(type(z), np.shape(z))
    print(len(A[0]))

    for i in range(0, len(A[0])):

        if norma == '1':
            diferenta = poza - A[:, i]
            z[i] = la.norm(diferenta, 1)
            print("z[i] norma 1 :", z[i], i)
        elif norma in dictNorma.keys() and norma == '2':
            diferenta = poza - A[:, i]
            z[i] = la.norm(diferenta, 2)
            print("z[i] norma 2:", z[i])
        elif norma in dictNorma.keys() and norma == 'inf':
            diferenta = poza - A[:, i]
            z[i] = la.norm(diferenta, np.inf)
            print("z[i] norma inf:", z[i])
        elif norma in dictNorma.keys() and norma == 'cos':
            num1 = np.dot(poza, A[:, i])
            num2 = la.norm(poza) * la.norm(A[:, i])
            z[i] = 1 - num1 / num2
            print("z[i] norma cos:", z[i])
        else:
            print("E obligatoriu să completezi o norma : ")
            norma = input
    print(z)

    poz = np.argsort(z)
    poz =poz[:3]
    vecini=np.zeros(len(poz))
    for i in range (0,len(poz)):
        if poz[i]%8==1:
            vecini[i]=poz[i]//8+1
        else:
            vecini [i]=poz[i]/8
    print (poz)
    vecin=int(statistics.mode(vecini))
    print(vecini)
    print(vecin)
    poz=8*(vecin)
    print(poz)


    pozaG = A[:, poz]
    pozaG = pozaG.reshape(112, 92)
    plt.imshow(pozaG)
    plt.show()




path = r'm0Poze\s7\2.pgm'
pozaS = cv2.imread(path, 0)
plt.imshow(pozaS)
plt.show()

if __name__ == "__main__":
    input = input("Pentru a apela funcția NN, completeaza o norma : ")

    KNN(A, pozaS, input)#chemarea funcției alg. K-NN