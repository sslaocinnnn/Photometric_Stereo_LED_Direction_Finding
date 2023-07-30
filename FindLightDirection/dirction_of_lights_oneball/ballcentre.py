import numpy as np
import cv2 as cv
from FindLightDirection.dirction_of_lights_oneball import ReadTiFone

# #These lines for reading SIF files
# from FindLightDirection import ReadSIF
# ReadSIF.readsif()
def ThreeDCentre():
 image = ReadTiFone.readtif(Centre=1)

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

 if circles is not None:
     circles = np.uint16(np.around(circles))
     for i in circles[0, :]:
        center = (i[0], i[1])
        radius = i[2]
 #
 #        cv.circle(egde, center, 1, 255, 9)
 # #        # circle outline
 #        radius = i[2]
 #        cv.circle(egde, center, radius, (255, 0, 255), 3)
 # #        # #
 #        cv.imshow('normal', egde)
 #        cv.imshow('cc', normaliz)
 # #
 #        cv.waitKey(0)
 #        cv.destroyAllWindows()
 print("centre of ball:",center)
 print("radius:", radius)
 # #
 indexofball = np.append(center, radius)

 return indexofball

if __name__ == '__main__':
 ThreeDCentre()



