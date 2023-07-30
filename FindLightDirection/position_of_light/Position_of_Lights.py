import numpy as np


import numpy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from FindLightDirection.position_of_light import fiveballcentre as ball
from FindLightDirection.position_of_light import fiveballlightdirection as light
from FindLightDirection.position_of_light import light_geo as geo

def function():
 light_pos = []
 # fig = plt.figure()
 # ax = fig.add_subplot(projection='3d')
 for n in range(3, 153):
    direction = light.LightDirec(n)
    lightpo = geo.light_geos(direction)
    light_pos.append(lightpo)

 light_positions = np.array(light_pos)
 print('Positions are:/')
 X = np.array(light_positions[:, 0])
 Y = np.array(light_positions[:, 1])
 Z = np.array(light_positions[:, 2])

 # X = X.reshape(1,X.shape[0])
 # Y = Y.reshape(1,Y.shape[0] )
 # Z = Z.reshape(1,Z.shape[0])
 #
 # print(X.shape)
 # print(Y.shape)
 # print(Z.shape)

 # for i in range(len(Bs)):

 fig = plt.figure()
 ax = fig.add_subplot(projection='3d')

 ax.plot_trisurf(X, Y, Z)
 ax.view_init(0, 0)
 plt.show()

 return light_positions

if __name__ == '__main__':
    np.savetxt('/Users/nicolas/PycharmProjects/Photonicssetero/CaluculateNomral/datas',function())





# print("light posistions",light_positions)
# print('shape',light_positions.shape)
# plt.show()

