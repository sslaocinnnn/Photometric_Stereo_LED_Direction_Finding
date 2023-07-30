import numpy as np


import numpy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from FindLightDirection.dirction_of_lights_oneball import ballcentre as ball
from FindLightDirection.dirction_of_lights_oneball import LightDirection as light


def function():
 light_pos = []
 # fig = plt.figure()
 # ax = fig.add_subplot(projection='3d')
 for n in range(2, 152):
    direction = light.LightDirec(n)
    light_pos.append(direction)

 light_positions = np.array(light_pos)
 print('Positions are:/',light_positions.shape)

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
 ax.scatter(0,0,1,c='red')
 ax.scatter(X,Y,Z,c='yellow')
 ax.view_init(0, 0)
 plt.title('3D Map of LEDs/Red Dot is the Camera')

 plt.show()

 return light_positions

if __name__ == '__main__':
    np.save('/Users/nicolas/PycharmProjects/Photonicssetero/CaluculateNomral/oneballlight',function())




# print("light posistions",light_positions)
# print('shape',light_positions.shape)
# plt.show()

