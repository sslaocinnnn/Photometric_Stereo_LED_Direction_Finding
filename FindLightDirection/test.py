# import LightDirection as light
# def y():
#  x = []
#  for i in range(6):
#     if i != 2:
#         if i!= 4:
#            x.append(light.LightDirec(2,i))
#
# print(x)
#
# if __name__=='__test__':
#     y()
#
#
# import ReadSIF
# import matplotlib.pyplot as plt
#
# ReadSIF.readsif()
# x= ReadSIF.image_data
# print(x)
# for i in range(13):
#     plt.imshow(x[i])
#     plt.gray()
#     plt.show()


import matplotlib.pyplot as plt
from FindLightDirection.dirction_of_lights_oneball import ballcentre, LightDirection as light

ball = ballcentre.ThreeDCentre()
centre = ball[0:2]
radius = ball[2]





fig = plt.figure()

lightdir = light.y()

ax = fig.add_subplot(projection='3d')
# u,v = np.mgrid[0:2*np.pi:100j, 0:np.pi:100j]
# x = radius * np.cos(u) * np.sin(v)
# y = radius * np.sin(u) * np.sin(v)
# z = radius * np.cos(v)
#
# ax.plot_surface(x + centre[0], y + centre[1], z + radius,alpha = 0.6, linewidth = 0)

for i in range(len(lightdir)):
    qq = lightdir[i]
    ax.scatter(qq[0],qq[1],qq[2],c='r', s =20)

plt.show()