import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
from FindLightDirection import ReadTiF

#camera hight 30.5cm position (0,0,1)
#ballr = 2.65cm
scale = 30.5/2.65
# [[651.  555.  529.8]
# [709.  511.  599.2]
#minimum z for LED is 11.5cm, 30.5/11.5
def ThreeDCentre():
 image = ReadTiF.readtif(Centre=1)

 print("Image data before Normalize:\n", image.shape)

 normaliz = cv.normalize(image, None, 0, 255, cv.NORM_MINMAX,dtype=cv.CV_8UC1)

 print("Image data after Normalize:\n", normaliz)




 # bblr = cv.bilateralFilter(normaliz,6,6,1000)
 mid = cv.medianBlur(normaliz,21)


 egde = cv.Canny(mid,0,21)
 rows = normaliz.shape[0]


 # mask = np.zeros(shape= egde.shape,dtype=np.uint8)
 #
 # cv.rectangle(mask,(300,200),(1000,900),(255,255,255),-1)
 #
 # out = cv.bitwise_and(normaliz,normaliz, mask=mask)


 # contours, hierarchy = cv.findContours(egde, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
 # contour = max(contours, key=cv.contourArea)
 # mask = np.ones_like(normaliz)
 # mask1 = cv.drawContours(mask, [contour], -1, (255, 255, 255), -1)

 circles = cv.HoughCircles(egde,cv.HOUGH_GRADIENT,1,rows/8,param1=50,param2=30,minRadius=80,maxRadius=150)
 print(circles)




 # cv.imshow('normal',egde)
 # cv.imshow('cc', mid)
 #
 # cv.waitKey(0)
 # cv.destroyAllWindows()
 unscaledcentre = []
 unscaledradius = []
 unscaledcircles = circles
 scaledcentre = []
 scaledradius = []
 scaledcentreofballs = []
 centreofballs = []

 if circles is not None:
     circles = np.uint16(circles)

     print(circles)


     for i in circles[0,:]:
        ce1 = (i[0]-696, i[1]-520)
        centreofballs.append(ce1)
        ce = (i[0],i[1])
        unscaledcentre.append(ce)
        unscaledradius.append(i[2])

        # plt.scatter(ce[0],ce[1])
        # plt.imshow(normaliz)
        # plt.show()
        # print("centre of ball:", centre)
        # print("radius:", radius)

 average =sum(unscaledradius)/len(unscaledradius)
 pixelscale = average/2650
 camera = pixelscale*30500
 correctedr = average/camera
 print("correctedr", correctedr)
 scaledcentre = centreofballs/camera
 print("correted cnetre",scaledcentre)
 correctedcentre = centreofballs

 scaledradius = np.tile(correctedr,(5,1))
 scaledcentreofballs = np.concatenate([scaledcentre,scaledradius],axis=1)
 print('scaledcentreofballs',scaledcentreofballs)
 print('unscaledcircle',unscaledcircles)






 #        # #
 # cv.imshow('normal', egde)
 # cv.imshow('cc', normaliz)
 # #
 # cv.waitKey(0)
 # cv.destroyAllWindows()
 # plt.imshow(egde)
 # plt.show()

 # #
 # arraycentreofballs = np.concatenate([np.array().reshape(5,2),np.array(radius1).reshape(5,1)],axis=1)
 # print(arraycentreofballs)


 return unscaledcentre,unscaledradius,unscaledcircles,correctedcentre,scaledcentre,scaledradius,scaledcentreofballs

if __name__ == '__main__':
 ThreeDCentre()



