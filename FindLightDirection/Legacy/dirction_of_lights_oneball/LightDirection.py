import numpy as np
# from FindLightDirection import ReadSIF
from FindLightDirection import ballcentre
import math
from numpy import unravel_index
from FindLightDirection import ReadTiFone
import cv2 as cv

scale = 1/(105.6/2650*30500)
print(scale)



# diameter of the ball 2.65cm ==> 2650 mm, global unit mm
# 3D model of the ball

# realDia = 2650
# realRedius = realDia/2

#
# fig = plt.figure()
#use cartesian coordinates
# ReadSIF.readsif()
# Imgaew = ReadSIF.image_data
# print(Imgaew)
Imgaew = ReadTiFone.readtif()
ball = ballcentre.ThreeDCentre()

def Reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup
def LightDirec(Sub):
     vectordirections = []
     print("3D Coordinate of Ball Centre:", ball)

     Imag = cv.normalize(Imgaew[Sub], None, 0, 255, cv.NORM_MINMAX, dtype=cv.CV_8UC1)
     mask = np.zeros_like(Imag)
     mask = cv.circle(mask,(ball[0],ball[1]),ball[2],(255,255,255),-1)
     out = cv.bitwise_and(Imag,Imag, mask = mask)

     # (min, max, minindex, maxindex) = cv.minMaxLoc(out)
     index = unravel_index(out.argmax(),out.shape)

     maxindex = Reverse(index)

     # cv.circle(out,maxindex, 1, 255, 9)
     # cv.imshow('a', out)
     # cv.waitKey(0)
     # cv.destroyAllWindows()

     Spot = maxindex
     corrtedindex = Spot[0] - 696, Spot[1] - 520
     corretcentre = ball[0] - 696, ball[1] - 520
     # print(maxindex)
     realraduis = ball[2]*scale
     realcentre = np.array(corretcentre)*scale




     dis = math.sqrt((corrtedindex[0]-corretcentre[0]) ** 2 + (corrtedindex[1]-corretcentre[1] ) ** 2)
     print("dis",dis)
     distance = dis * scale
     scalespot = np.array(corrtedindex) * scale
     bz = math.sqrt((realraduis ** 2) - (distance ** 2)) + realraduis

     spot = scalespot.reshape(1, 2)

     brtspotcor = np.concatenate([spot, bz.reshape(1, 1)], axis=1)
     print("Brightest Spot:", brtspotcor)

     deltax = brtspotcor[0, 0] - realcentre[0]
     deltay = brtspotcor[0, 1] - realcentre[1]
     deltaz = brtspotcor[0, 2] - realraduis

     mag = math.sqrt(deltax ** 2 + deltay ** 2 + deltaz ** 2)

     dirc = np.array([deltax,deltay,deltaz])/mag
     direction = np.array(dirc.reshape(3,))
     print(direction)



     return direction







if __name__ == '__main__':
 LightDirec(5)










