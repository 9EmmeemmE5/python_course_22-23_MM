import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10,10)
y = x**2

fig = plt.figure(block=True)
ax = fig.add_subplot(111)
ax.plot(x,y)

coords = []
print(coords)
def onclick(event):
    global ix, iy
    ix, iy = event.xdata, event.ydata
    print(f"x0{ix}, y={iy}")

    global coords
    coords.append((ix, iy))

    if len(coords) == 2:
        fig.canvas.mpl_disconnect(cid)

    return coords
cid = fig.canvas.mpl_connect('button_press_event', onclick)