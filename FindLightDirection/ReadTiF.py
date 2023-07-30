import tifffile




image = []
def readtif(path= '/Users/nicolas/Desktop/MasterProject/TiF/28jul/data/ball_3/ball_3_MMStack_Pos0.ome.tif', Centre =None):

    read_image = tifffile.imread(path)

    for i in range(1,len(read_image)):
        print(i)
        read = read_image[i,:,:]
        image.append(read)
    if Centre == None:
        return image
    else:
        return read_image[0,:,:]






















if __name__ == '__main__':
    readtif()









