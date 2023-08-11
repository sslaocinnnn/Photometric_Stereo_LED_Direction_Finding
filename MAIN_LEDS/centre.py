import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
import ReadTiF

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

image = ReadTiF.readtif(Centre=1)

# ll = sum(image[0:13])

# print("Image data before Normalize:\n", image.shape)

normaliz = cv.normalize(image, None, 0, 6000, cv.NORM_MINMAX,dtype=cv.CV_8UC1)

print("Image data after Normalize:\n", normaliz)

# plt.imshow(normaliz)
# plt.gray()
# plt.show()




def Findcentre():
 mid = cv.medianBlur(normaliz,35)
 edge = cv.Canny(mid,0,200)

 contours, hierarchy = cv.findContours(edge, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
 mask = np.zeros_like(normaliz)
 mask1 = cv.drawContours(mask, contours, 2, (255, 255, 255), -1)
 ##Select hierarchy for the central ball

 # plt.imshow(mask1)
 # plt.show()

 y = normaliz.shape[0]
 x = normaliz.shape[1]
 mask = cv.bitwise_and(normaliz,normaliz,mask = mask1)
 xl = np.zeros([y,1])
 yl = np.zeros([x,1])
 for i in range(y):
  for j in range(x):
   if mask[i,j] != 0:
    xl[i]  = xl[i]+1



 for ii in range(x):
  for jj in range(y):
   if mask[jj,ii] != 0:
    yl[ii]  = yl[ii]+1

 # print(xl.argmax())
 # print(xl.max())
 # print(yl.argmax())
 # print(yl.max())
 avey = []
 avex = []
 for xx in range(len(xl)):
   if xl[xx] == xl.max():
    avex.append(xx)


 for yy in range(len(yl)):
  if yl[yy] == yl.max():
   avey.append(yy)

 y = np.array(avex).mean()
 x = np.array(avey).mean()

 print('y',y)
 print('x',x)



 # plt.imshow(mask,origin='upper')
 # plt.scatter(x,y)
 # plt.show()

 twoDcentre  = [x,y]
 radius = (xl.max()+yl.max())/4

 threeDcentre = [x,y,radius]
 return twoDcentre,radius,threeDcentre,mask1













#
if __name__ == '__main__':
  Findcentre()



