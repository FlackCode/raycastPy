import numpy as np
from matplotlib import pyplot as plt
import keyboard

mapArray = [[1,1,1,1,1],
            [1,0,0,0,1],
            [1,0,0,1,1],
            [1,0,0,0,1],
            [1,1,1,1,1],]

xPos, yPos = (1,1)
xExit, yExit = (3,3)
playerRotation = np.pi/4

while True:
    for i in range(60):
        playerRotation_i = playerRotation + np.deg2rad(i-30)
        x, y = (xPos, yPos)
        sin, cos = (0.02*np.sin(playerRotation_i), 0.02*np.cos(playerRotation_i))
        n = 0
        while True:
            x, y = (x+cos, y+sin)
            n = n+1
            if mapArray[int(x)][int(y)] != 0:
                height = 1 / (0.02 * n)
                break
        plt.vlines(i, -height, height, lw=8)
    plt.axis('off'); plt.tight_layout(); plt.axis([0, 60, -1, 1])
    plt.draw(); plt.pause(0.0001); plt.clf()

    keyPressed = keyboard.read_key()
    x, y = (xPos, yPos)

    if keyPressed == 'up':
        x, y = (x + 0.3*np.cos(playerRotation), y + 0.3*np.sin(playerRotation))
    elif keyPressed == 'down':
        x, y = (x - 0.3*np.cos(playerRotation), y - 0.3*np.sin(playerRotation))
    elif keyPressed == 'left':
        playerRotation = playerRotation - np.pi/8
    elif keyPressed == 'right':
        playerRotation = playerRotation + np.pi/8
    elif keyPressed == 'esc':
        break
    if mapArray[int(x)][int(y)] == 0:
        if int(xPos) == xExit and int(yPos) == yExit:
            break
        xPos, yPos = (x,y)

plt.close()