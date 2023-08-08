import numpy as np

import matplotlib.pyplot as plt
import BrightSpots as L
from sklearn.preprocessing import normalize

def function():
 light_pos = []
 # fig = plt.figure()
 # ax = fig.add_subplot(projection='3d')
 for n in range(12):
    direction = L.LightDirec(n)


    light_pos.append(direction)

 light_positions = np.array(light_pos).reshape(12,3)
 # print('Positions are:/')


 # X = X.reshape(1,X.shape[0])
 # Y = Y.reshape(1,Y.shape[0] )
 # Z = Z.reshape(1,Z.shape[0])
 #
 # print(X.shape)
 # print(Y.shape)
 # print(Z.shape)

 # for i in range(len(Bs)):


 # light_positionsnorm = normalize(light_positions,axis=1)


 X = np.array(light_positions[:,0])
 Y = np.array(light_positions[:,1])
 Z = np.array(light_positions[:,2])

 # Xn = np.array(light_positionsnorm[:, 0])
 # Yn = np.array(light_positionsnorm[:, 1])
 # Zn = np.array(light_positionsnorm[:, 2])
 #
 #
 # print(Z.argmin())
 # print("light posistions", light_positions)
 # print('shape', light_positions.shape)

 # light_positions = np.delete(light_positions,(125),axis=0)

 # X = np.array(light_positions[:, 0])
 # Y = np.array(light_positions[:, 1])
 # Z = np.array(abs(light_positions[:, 2]))
 #
 # print(Z.argmin())
 # print("light posistions", light_positions)
 # print('shape', light_positions.shape)
 #
 fig = plt.figure()
 ax = fig.add_subplot(projection='3d')

 ax.scatter(X, Y, Z)
 ax.view_init(0, 0)
 # ax.set_zlim(0,1)
 plt.title('Unit Vectors of LEDs')
 plt.savefig('Unit Vectors of LEDs')
 plt.show()
 #
 # fig = plt.figure()
 # ax = fig.add_subplot(projection='3d')
 # ax.scatter(X,Y,Z,c='yellow')
 # ax.view_init(0, 0)
 # # ax.set_zlim(0,1)
 # ax.plot_trisurf(X,Y,Z)
 # plt.title('Unit Vectors of LEDs with surface')
 # plt.savefig('Unit Vectors of LEDs with surface')
 # plt.show()


 # fig = plt.figure()
 # ax = fig.add_subplot(projection='3d')
 #
 # ax.scatter(Xn,Yn,Zn)
 # ax.view_init(0, 0)
 # # ax.set_zlim(0,1)
 # plt.title('Normalized Unit Vectors of LEDs')
 # plt.savefig('Normalized Unit Vectors of LEDs')
 # plt.show()
 #
 # fig = plt.figure()
 # ax = fig.add_subplot(projection='3d')
 #
 # ax.scatter(Xn,Yn,Zn)
 # ax.view_init(0, 0)
 # # ax.set_zlim(0,1)
 # ax.plot_trisurf(Xn,Yn,Zn)
 # plt.title('Normalized Unit Vectors of LEDs with surface')
 # plt.savefig('Normalized Unit Vectors of LEDs with surface')
 # plt.show()

 np.save('/Users/nicolas/Desktop/MasterProject/TiF/aug08.npy',light_positions)
 return light_positions

if __name__ == '__main__':
  function()






