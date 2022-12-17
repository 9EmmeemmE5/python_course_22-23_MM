# import the necessary packages
import cv2 as cv
import matplotlib.pyplot as plt

# Simple mouse click function to store coordinates
def onclick(event):
    global ix, iy
    ix, iy = event.xdata, event.ydata
    x_int=int(ix)
    y_int=int(iy)
    
    # Calling global variable coord in order to use it inside the funct
    global coords
    coords.append((x_int,y_int))
    
    # Disconnect after 2 clicks
    if len(coords) == 2:
        fig.canvas.mpl_disconnect(cid)
        plt.close(1)
    return

image_path=".\\Esercizi_da_consegnare\\Avanzato\\aaa\\DSCF0336.jpg" #definita

image=cv.imread(image_path, cv.IMREAD_GRAYSCALE) #definita
fig,ax=plt.subplots()
plt.subplot(1,1,1)
plt.imshow(image, cmap="gray")

coords = []

# Call click func
cid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.show(block=True)
print(coords) #[(x_top_left,y_top_left),(x_bot_right,y_bot_right)]