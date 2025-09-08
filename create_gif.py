import imageio.v3 as iio

filenames = ['imgs/team-pic1.png', 'imgs/team-pic2.png']
images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('imgs/team-pic.gif', images, duration=500, loop=0)