import sif_parser
import numpy as np
from numpy import unravel_index
import matplotlib.pyplot as plt
import pandas as pd
import xarray
import xarray as xr
import cv2 as cv
import os
from natsort import natsorted

image_data = []
def readsif(path='/Users/nicolas/Desktop/MasterProject/17jul/oneball'):
    for filename in natsorted(os.listdir(path)):
        print(filename)
        data = xr.DataArray(sif_parser.xr_open(path + '/' + filename))
        twodims = data.isel(Time = 0)
        TwoD = twodims.values

        # plt.imshow(TwoD)
        # plt.title(filename)
        # plt.show()
        image_data.append(TwoD)






#
# if __name__ == 'ReadSIF':
# readsif('/Users/nicolas/Desktop/MasterProject/SIFData/balls')
#

if __name__ == '__main__':
    readsif()







#
# da1 = da/da.max()
# #
# # c = np.argmax(da1)
# # # print(c)
# d = unravel_index(da1.argmax(),da1.shape)
# print(d)
# print(da1[d])






#
# plt.imshow(da1)
#
# plt.show()






# cv.imshow('da',da)
# cv.waitKey(0)
#
# # closing all open windows
# cv.destroyAllWindows()