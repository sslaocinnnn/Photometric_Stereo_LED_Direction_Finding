import numpy as np
# from FindLightDirection import ReadSIF
import fiveballcentre
from FindLightDirection.position_of_light.Tifs import ReadTiF
import math
from numpy import unravel_index
import cv2 as cv

# diameter of the ball 2.65cm ==> 2650 mm, global unit mm
# 3D model of the ball

# realDia = 2650
# realRedius = realDia/2
scale = 1/2443.1292504994863
print(scale)

R = np.array([0,0,1]).reshape((1,3))

Imgaew = ReadTiF.readtif()
ball = fiveballcentre.ThreeDCentre()

def Reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup

def LightDirec(Sub):
     vectordirections = []
     correctedindex = []
     correcteddirections = []

     print("3D Coordinate of Ball Centre:", ball)
     ballcentre =  ball[0]
     ballraduis = ball[1]
     correctballcentre = ball[3]
     realballcentre = ball[4]
     realballraduis = ball[5]
     print(realballraduis)

     Imag = cv.normalize(Imgaew[Sub], None, 0, 255, cv.NORM_MINMAX, dtype=cv.CV_8UC1)


     for i in range(5):
      centretonp = ballcentre[i]
      realraduis = realballraduis[i][0]
      corretcentre = correctballcentre[i]
      realcentre = realballcentre[i]
      mask = np.zeros_like(Imag)
      mask = cv.circle(mask,centretonp,ballraduis[i],(255,255,255),-1)
      out = cv.bitwise_and(Imag,Imag, mask = mask)
      index = unravel_index(out.argmax(), out.shape)
      print('index',realraduis)

      maxindex = Reverse(index)
      print(maxindex)
      # cv.circle(out,maxindex, 1, 255, 9)
      # cv.imshow('a', out)
      # cv.waitKey(0)
      # cv.destroyAllWindows()
      # plt.imshow(out,origin='lower')
      # plt.scatter(maxindex[0],maxindex[1])
      # plt.scatter(centretonp[0],centretonp[1],c='red')
      # plt.scatter(696,520, c='yellow')
      # plt.show()

      Spot = maxindex
      corrtedindex = Spot[0]-696,Spot[1]-520
      print(corrtedindex)
      print(corretcentre)


      dis = math.sqrt((corrtedindex[0]-corretcentre[0]) ** 2 + (corrtedindex[1]-corretcentre[1] ) ** 2)
      print("dis", dis)
      distance = dis*scale
      print(distance)
      scalespot = np.array(corrtedindex)*scale

      bz = math.sqrt((realraduis ** 2) - (distance ** 2)) + realraduis

      spot = scalespot.reshape(1,2)

      brtspotcor = np.concatenate([spot,bz.reshape(1,1)],axis=1)
      print("Brightest Spot:", brtspotcor)
      # plt.scatter(corrtedindex[0], corrtedindex[1])
      # plt.scatter(corretcentre[0], corretcentre[1], c='red')
      # plt.scatter(0, 0, c='yellow')
      # plt.plot([corretcentre[0],corrtedindex[0]],[corretcentre[1],corrtedindex[1]])
      # plt.show()

      deltax = brtspotcor[0, 0] - realcentre[0]
      deltay = brtspotcor[0, 1] - realcentre[1]
      deltaz = brtspotcor[0, 2] - realraduis

      mag = math.sqrt(deltax ** 2 + deltay ** 2 + deltaz ** 2)
      # mag = math.sqrt(deltax ** 2 + deltay ** 2)


      dirc = np.array([deltax,deltay,deltaz])/mag

      direction = np.array(dirc.reshape(1,3))

      # plt.imshow(out)
      # plt.show()
      vectordirections.append(direction)
      # plt.scatter(brtspotcor[0, 0],brtspotcor[0, 1])
      # plt.scatter(realcentre[0],realcentre[1], c='red')
      # plt.scatter(0, 0, c='yellow')
      # plt.plot([realcentre[0], dirc[0]*10], [realcentre[1], dirc[1]*10])
      # plt.show()






     # (min, max, minindex, maxindex) = cv.minMaxLoc(out)

     vectors = np.array(vectordirections).reshape(5,3)
     print(vectors)









     # print(directions)



     return vectors






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
    print(LightDirec(126))










