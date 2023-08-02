import tifffile
import numpy as np
import cv2 as cv



    # for i in range(0,len(read_image)):
    #     print(i)
    #     read = read_image[i,:,:]
    #     image.append(read)
    # if Centre == None:
    #     return image
    # else:
    #     return read_image[0,:,:]

def DomeCentre():
 image = tifffile.imread('/Users/nicolas/Desktop/MasterProject/TiF/18jul/ball/oneball/MMStack_Pos0.ome.tif')[0, :, :]


 print("Image data before Normalize:\n", image.shape)


 normaliz = cv.normalize(image, None, 0, 255, cv.NORM_MINMAX,dtype=cv.CV_8UC1)
 normaliz = -(normaliz-12)


 print("Image data after Normalize:\n", normaliz)




 # bblr = cv.bilateralFilter(normaliz,6,6,1000)
 # mid = cv.medianBlur(normaliz,21)
 #
 #
 # egde = cv.Canny(mid,0,21)
 rows = normaliz.shape[0]


 mask = np.ones(shape= normaliz.shape,dtype=np.uint8)

 cv.rectangle(mask,(400,150),(940,960),(0,0,0),-1)

 out = cv.bitwise_and(normaliz,normaliz, mask=mask)

 bblr = cv.bilateralFilter(out,6,6,1000)
 mid = cv.medianBlur(out,15)


 egde = cv.Canny(mid,0,21)

 # cv.imshow('normal',mid)
 # cv.imshow('cc', egde)
 #
 # cv.waitKey(0)
 # cv.destroyAllWindows()


 # contours, hierarchy = cv.findContours(egde, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
 # contour = max(contours, key=cv.contourArea)
 # mask = np.ones_like(normaliz)
 # mask1 = cv.drawContours(mask, [contour], -1, (255, 255, 255), -1)

 circles = cv.HoughCircles(egde,cv.HOUGH_GRADIENT,2,rows/16)
 print(circles)



 #
 # cv.imshow('normal',out)
 # cv.imshow('cc', out)
 #
 # cv.waitKey(0)
 # cv.destroyAllWindows()

 if circles is not None:
     circles = np.uint16(np.around(circles))
     for i in circles[0, :]:
        center = (i[0], i[1])
        radius = i[2]
 #
        cv.circle(egde, center, 1, 255, 9)
 #        # circle outline
        radius = i[2]
        cv.circle(egde, center, radius, (255, 0, 255), 3)
 #        # #
        cv.imshow('normal', egde)
        cv.imshow('cc', normaliz)
 #
        cv.waitKey(0)
        cv.destroyAllWindows()
 print("centre of ball:",center)
 print("radius:", radius)
 # #
 indexofball = np.append(center, radius)

 return indexofball










if __name__ == '__main__':
    DomeCentre()









