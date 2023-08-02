import numpy as np

import fiveballcentre as ball
import fiveballlightdirection as light
import matplotlib.pyplot as plt

# c1 = ball.ThreeDCentre()[6].reshape(5,3)
# d1 = light.LightDirec(100)

# d2 = np.zeros([5,3])
# d2[:,2] = c1[:,2]
#
# print("222",d2)
centres = ball.ThreeDCentre()[6].reshape(5,3)

# c2 = np.tile([696,520,0],(5,1))
# centre= c1-c2
# directions = d1 -c2-d2
# print(directions)
# centres =c1.flatten()
# directionss =d1.flatten()

scale = 1/2443.1292504994863
# possible1 = [651.,555.,529.8]*scale
# possible2 = [709.,511.,599.2]


def light_geos(dirctions):
    c = centres.flatten()
    d = dirctions
    B = c.T
    A_left = np.tile(np.eye(3),(5,1))
    A_right = np.zeros([15,5])

    for i in range(5):
        A_right[i*3:(i*3)+3,i]= -d[i,:]

    A = np.concatenate((A_left,A_right),axis=1)
    print(A)

    solution = np.linalg.inv(np.dot(A.T,A)).dot(A.T).dot(B)
    #solution = nnls(A,B)
    # solution = np.linalg.lstsq(A,B)
    print(solution)



    # for j in range(5):
    #  ax.plot([centres[j,0],d[j,0]*20],[centres[j,1],d[j,1]*20],[centres[j,2],d[j,2]*20])
    #
    lightpostion = (solution[0],solution[1],solution[2])



    #
    # ax.scatter(solution[0],solution[1],solution[2])
    # ax.scatter(0,0,1)

    return lightpostion









if __name__ == '__main__':
    print(light_geos(light.LightDirec(126)))
    plt.show()
