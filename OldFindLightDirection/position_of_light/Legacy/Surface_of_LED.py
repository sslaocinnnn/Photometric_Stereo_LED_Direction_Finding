import numpy as np

import matplotlib.pyplot as plt
from OldFindLightDirection import fiveballlightdirection as light


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

