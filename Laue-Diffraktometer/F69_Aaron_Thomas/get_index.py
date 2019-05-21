import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

coord_list = []

def clicked(event):
	global ix, iy
	ix, iy =  event.xdata, event.ydata
	entry = [ix, iy]
	print("x_data: {}, y_data: {}".format(ix, iy))
	coord_list.append(entry)
	return entry 

path = "Exercise_2/quartz_20.png"
img = mpimg.imread(path)
ax = plt.gca()
fig = plt.gcf()
implot = ax.imshow(img)

cid = fig.canvas.mpl_connect("button_press_event", clicked)

plt.show()

print(coord_list)

np.save('data_quartz_20.npy', coord_list)
np.savetxt('data_quartz_20.txt', coord_list)

