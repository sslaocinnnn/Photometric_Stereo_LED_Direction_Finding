import numpy as np
import cv2 as cv
from FindLightDirection.position_of_light.Tifs import ReadTiF

#camera hight 39.5cm position (0,0,1)
#ballr = 2.54cm
scale = 399.66125478480063/25.4
# [[651.  555.  529.8]
# [709.  511.  599.2]
#minimum z for LED is 11.5cm, 30.5/11.5

# field of view in radian: 0.27752867535596515
# field of view in degrees: 15.901221791753184
# Height of camera in pixels: 2443.1292504994863
# Height of camera in mm: 399.66125478480063
def ThreeDCentre():
 image = ReadTiF.readtif(Centre=1)

 print("Image data before Normalize:\n", image.shape)

 normaliz = cv.normalize(image, None, 0, 255, cv.NORM_MINMAX,dtype=cv.CV_8UC1)

 print("Image data after Normalize:\n", normaliz)




 bblr = cv.bilateralFilter(normaliz,4,4,1000)
 mid = cv.medianBlur(bblr,5)


 # egde = cv.Canny(mid,25,100)
 rows = normaliz.shape[0]


 mask = np.zeros(shape= mid.shape,dtype=np.uint8)
 #
 # cv.rectangle(mask,(300,200),(1000,900),(255,255,255),-1)
 #
 # out = cv.bitwise_and(normaliz,normaliz, mask=mask)


 # contours, hierarchy = cv.findContours(egde, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
 # contour = max(contours, key=cv.contourArea)
 # mask = np.ones_like(normaliz)
 # mask1 = cv.drawContours(mask, [contour], -1, (255, 255, 255), -1)

 circles = cv.HoughCircles(mid,cv.HOUGH_GRADIENT,1,rows/8,param1=30,param2=50,minRadius=70,maxRadius=90)
 print(circles)

 circlesfloat = circles
 circlesint = np.uint16(circles)
 # cv.imshow('cc', mid)
 # # cv.imshow('normal',e)
 #
 #
 # cv.waitKey(0)
 # cv.destroyAllWindows()
 unscaledcentre_float = []
 unscaledradius_float = []
 unscaledcircles = circles
 scaledcentre = []
 scaledradius = []
 scaledcentreofballs = []
 centreofballs_float = []
 centreofballs_int=[]
 unscaledcentre_int =[]
 unscaledradius_int=[]


 if circlesint is not None:


     print(circlesint)

     for i in circlesint[0,:]:
        ce1 = (i[0]-696, i[1]-520)
        centreofballs_int.append(ce1)
        ce = (i[0],i[1])
        unscaledcentre_int.append(ce)
        unscaledradius_int.append(i[2])
 #        #Show the circles detected
 #        cv.circle(normaliz, ce, 1, 255, 9)
 #        #        # circle outline
 #        radius = i[2]
 #        cv.circle(normaliz, ce, radius, (255, 0, 255), -1)
 #
 #        #        # #
 #
 #        cv.imshow('cc', normaliz)
 #        #
 #        cv.waitKey(0)
 #        cv.destroyAllWindows()
 # # if circlesfloat is not None:
 #
 #  print(circlesfloat)
 #
 #  for i in circlesfloat[0, :]:
 #   ce1 = (i[0] - 696, i[1] - 520)
 #   centreofballs_float.append(ce1)
 #   ce = (i[0], i[1])
 #   unscaledcentre_float.append(ce)
 #   unscaledradius_float.append(i[2])

 average =sum(unscaledradius_int)/len(unscaledradius_int)
 lengthtopixels = 25.4/(average*2)
 camerasettoone = 1/2443.1292504994863
 print(camerasettoone)
 correctedr = average/camerasettoone
 print("correctedr", correctedr)
 scaledcentre = np.array(centreofballs_int)/camerasettoone
 print("correted cnetre",scaledcentre)
 correctedcentre = centreofballs_int

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


 return unscaledcentre_int,unscaledradius_int,unscaledcircles,correctedcentre,scaledcentre,scaledradius,scaledcentreofballs

if __name__ == '__main__':
 ThreeDCentre()



