"""
Questo modulo implementa la funzione di creazione della lista di coordinate di 2 punti per
generare una regione di interesse all'interno di un grafico contenente un immagine
"""
# import the necessary packages
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def on_press(event):
    global coords
    coords.append((x_int,y_int))
    
    global x_coord,y_coord
    x_coord=event.xdata
    y_coord=event.ydata
    
    x_int=int(x_coord)
    y_int=int(y_coord)
    print('you pressed', event.button, x_coord, y_coord)
    
    if len(coords)==2:
        fig.canvas.mpl_disconnect(cid)
    return coords

coords=[]
fig, ax = plt.subplots()
ax.plot(np.random.rand(10))
cid = fig.canvas.mpl_connect('button_press_event', on_press)
plt.show(block=True)
