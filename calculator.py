import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

dhTable = ([])

class calculator:
    def dh_kine(dhTable, count):
        stack = 0
        if count == 1:
            stack = np.array([[np.cos(dhTable[0]), -np.sin(dhTable[0]) * np.cos(dhTable[1]), np.sin(dhTable[0]) * np.sin(dhTable[1]), dhTable[2] * np.cos(dhTable[0])],
                              [np.sin(dhTable[0]), np.cos(dhTable[0]) * np.cos(dhTable[1]), -np.cos(dhTable[0]) * np.sin(dhTable[1]), dhTable[2] * np.sin(dhTable[0])],
                              [0, np.sin(dhTable[1]), np.cos(dhTable[1]), dhTable[3]],
                              [0, 0, 0, 1]])
        else:
            for i in range(count):
                T = np.array([[np.cos(dhTable[i, 0]), -np.sin(dhTable[i, 0]) * np.cos(dhTable[i, 1]), np.sin(dhTable[i, 0]) * np.sin(dhTable[i, 1]), dhTable[i, 2] * np.cos(dhTable[i, 0])],
                             [np.sin(dhTable[i, 0]), np.cos(dhTable[i, 0]) * np.cos(dhTable[i, 1]), -np.cos(dhTable[i, 0]) * np.sin(dhTable[i, 1]), dhTable[i, 2] * np.sin(dhTable[i, 0])],
                             [0, np.sin(dhTable[i, 1]), np.cos(dhTable[i, 1]), dhTable[i, 3]],
                             [0, 0, 0, 1]])
                print(i)
                if i == 0:
                    Matrix = T
                    stack = T
                else:
                    finMatrix = Matrix @ T
                    stack = np.hstack((stack, finMatrix))
                    Matrix = finMatrix
        return stack

    def xyzpos(stack, count):
        X = np.array([0])
        Y = np.array([0])
        Z = np.array([0])

        for i in range(3, count*4, 4):
            if i == 3:
                X = np.concatenate((X[:], [stack[0, i], stack[0, i]]))
                Y = np.concatenate((Y[:], [stack[1, i], stack[1, i]]))
                Z = np.concatenate((Z[:], [stack[2, i], stack[2, i]]))
            else:
                X = np.concatenate((X[:], [stack[0, i]]))
                Y = np.concatenate((Y[:], [stack[1, i]]))
                Z = np.concatenate((Z[:], [stack[2, i]]))
        return np.vstack((X, Y, Z))

    def pos2base(Q):
        X,Y,Z=Q[0,:],Q[1,:],Q[2,:]
        pos = []
        for i in range(Q):
            pos = np.array([X[i]], Y[i]. Z[i])
        return pos