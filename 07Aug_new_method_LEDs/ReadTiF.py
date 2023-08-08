import tifffile

# field of view in radian: 0.27752867535596515
# field of view in degrees: 15.901221791753184
# Height of camera in pixels: 2443.1292504994863
# Height of camera in mm: 399.66125478480063
import numpy as np



image = []
def readtif(pathoffiveballs = 'ball13_2_MMStack_Pos0.ome.tif',pathofpositions = 'ball13_2_MMStack_Pos0.ome.tif',Centre =None):

    read_image = tifffile.imread(pathoffiveballs)
    read_positions = tifffile.imread(pathofpositions)
    read_positions = sum(read_positions[0:12])

    for i in range(read_image.shape[0]):
        print(i)
        read = read_image[i,:,:]
        image.append(read)
    if Centre == None:
        return image
    else:
        return read_positions






















if __name__ == '__main__':
    readtif()









