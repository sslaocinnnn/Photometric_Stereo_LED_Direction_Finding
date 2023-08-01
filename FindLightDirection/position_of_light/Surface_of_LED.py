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
 for n in range(1, 154):
    direction = light.LightDirec(n)


 fig = plt.figure()
 ax = fig.add_subplot(projection='3d')

 ax.plot_surface(X, Y, Z)
 ax.view_init(0, 0)
 plt.show()

 return light_positions

if __name__ == '__main__':
    np.savetxt(function())





# print("light posistions",light_positions)
# print('shape',light_positions.shape)
# plt.show()

