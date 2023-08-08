import numpy as np
import centre
import ReadTiF
import math
from numpy import unravel_index
import cv2 as cv
import matplotlib.pyplot as plt

# diameter of the ball 2.65cm ==> 2650 mm, global unit mm
# 3D model of the ball

#camera hight 39.5cm position (0,0,1)
#ballr = 2.54cm





Imgaew = ReadTiF.readtif()

Ball = centre.Findcentre()
twoDcentre = Ball[0]
radius = Ball[1]
threeDcentre = Ball[2]
mask = Ball[3]

size_of_one_pixel = 25.4/(2*radius)
cam_height_in_pixels = 399.66125/size_of_one_pixel
scale = 1/cam_height_in_pixels

R = np.array([0,0,1]).reshape((1,3))


def Reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup

def LightDirec(Sub):
     vectordirections = []
     correctedindex = []
     correcteddirections = []


     Imag = cv.normalize(Imgaew[Sub], None, 0, 255, cv.NORM_MINMAX, dtype=cv.CV_8UC1)
     out = cv.bitwise_and(Imag,Imag, mask = mask)
     # index = unravel_index(out.argmax(), out.shape)
     max = out.max()

     #this for loops need reconsidered
     for i in range(out.shape[0]):
         for j in range(out.shape[1]):
             if out[i, j] == max:
                 index = [j,i]


     print('index',index)

     # index = Reverse(index)
     # print(index)
     #  # cv.circle(out,maxindex, 1, 255, 9)
     #  # cv.imshow('a', out)
     #  # cv.waitKey(0)
     # plt.imshow(out)
     # plt.scatter(index[0],index[1])
     # plt.scatter(twoDcentre[0],twoDcentre[1],c='red')
     # plt.scatter(696,520, c='yellow')
     # plt.gray()
     # plt.show()
     #
     centre_shift = twoDcentre[0],twoDcentre[1]
     index_shift = index[0], index[1]
     index_to_centre = math.sqrt((index_shift[0]-centre_shift[0])**2 + (index_shift[1]-centre_shift[1])**2)
     height_above_centre = math.sqrt(radius**2-index_to_centre**2)
     vector_of_brighest_spot = index_shift[0],index_shift[1],height_above_centre+radius

     print(vector_of_brighest_spot)

     deltax = (vector_of_brighest_spot[0] - threeDcentre[0])/radius
     deltay = (vector_of_brighest_spot[1] - threeDcentre[1])/radius
     deltaz = math.sqrt(1-deltax**2 -deltay**2)


     dirc = np.array([deltax,deltay,deltaz])
     dirc = dirc.reshape(1,3)
     print(dirc)



     L = 2*np.vdot(dirc,R)*dirc-R
     print(L)










     #
     #
     #  dis = math.sqrt((corrtedindex[0]-corretcentre[0]) ** 2 + (corrtedindex[1]-corretcentre[1] ) ** 2)
     #  print("dis", dis)
     #  distance = dis*scale
     #  print(distance)
     #  scalespot = np.array(corrtedindex)*scale
     #
     #  bz = math.sqrt((realraduis ** 2) - (distance ** 2)) + realraduis
     #
     #  spot = scalespot.reshape(1,2)
     #
     #  brtspotcor = np.concatenate([spot,bz.reshape(1,1)],axis=1)
     #  print("Brightest Spot:", brtspotcor)
     #  # plt.scatter(corrtedindex[0], corrtedindex[1])
     #  # plt.scatter(corretcentre[0], corretcentre[1], c='red')
     #  # plt.scatter(0, 0, c='yellow')
     #  # plt.plot([corretcentre[0],corrtedindex[0]],[corretcentre[1],corrtedindex[1]])
     #  # plt.show()
     #

     #
     #  mag = math.sqrt(deltax ** 2 + deltay ** 2 + deltaz ** 2)
     #  # mag = math.sqrt(deltax ** 2 + deltay ** 2)
     #
     #
     #  dirc = np.array([deltax,deltay,deltaz])/mag
     #
     #  direction = np.array(dirc.reshape(1,3))
     #
     #  # plt.imshow(out)
     #  # plt.show()
     #  vectordirections.append(direction)
     #  # plt.scatter(brtspotcor[0, 0],brtspotcor[0, 1])
     #  # plt.scatter(realcentre[0],realcentre[1], c='red')
     #  # plt.scatter(0, 0, c='yellow')
     #  # plt.plot([realcentre[0], dirc[0]*10], [realcentre[1], dirc[1]*10])
     #  # plt.show()
     #
     #
     #
     #
     #
     #
     # # (min, max, minindex, maxindex) = cv.minMaxLoc(out)
     #
     # vectors = np.array(vectordirections).reshape(5,3)
     # print(vectors)
     #
     #
     #
     #
     #
     #
     #
     #
     #
     # # print(directions)
     #
     #
     #
     return L
     #
     #




# def y():
#      x = []
#      for i in range(144):
#       x.append(LightDirec(i))
#      return x



#
# if __name__ == '__felllightdirection__':
#      y()
# else:
#     # y()
#     # LightDirec(5)
if __name__ == '__main__':
    for i in range(12):
        LightDirec(i)










