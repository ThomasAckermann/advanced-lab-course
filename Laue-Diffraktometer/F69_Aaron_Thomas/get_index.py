import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


coord_list = []

def clicked()
	global ix, iy
	ix, iy =  event.xdata, event.ydata
	entry = [ix, iy]
	print("x_data: {}, y_data: {}")
	coord_list.append(entry)
	return entry

path = "C:\PSLViewer-4.3-win32-SECURED\F69_Aaron_Thomas\Exercise_2\quartz_0.png"
img = mpimg.imread(path)
plt.imshow(img)
plt.show()

cid = fig.canvas.mpl_connect("button_press_event", clicked)

print(coord_list)
np.save('data.npy', coord_list)
