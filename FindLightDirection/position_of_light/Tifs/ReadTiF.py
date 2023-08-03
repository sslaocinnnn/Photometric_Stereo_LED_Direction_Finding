import tifffile

# field of view in radian: 0.27752867535596515
# field of view in degrees: 15.901221791753184
# Height of camera in pixels: 2443.1292504994863
# Height of camera in mm: 399.66125478480063



image = []
def readtif(pathoffiveballs = '/Users/nicolas/Desktop/MasterProject/TiF/01aug 2/_1/_1_MMStack_Pos0.ome.tif',pathofpositions = '/Users/nicolas/Desktop/MasterProject/TiF/01aug 2/ballposition/MMStack_Pos0.ome.tif',Centre =None):

    read_image = tifffile.imread(pathoffiveballs)
    read_positions = tifffile.imread(pathofpositions)

    for i in range(0,len(read_image)):
        print(i)
        read = read_image[i,:,:]
        image.append(read)
    if Centre == None:
        return image
    else:
        return read_positions






















if __name__ == '__main__':
    readtif()









