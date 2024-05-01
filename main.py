import numpy as np
from matplotlib import pyplot as plt
import keyboard

mapArray = [[1,1,1,1,1],
            [1,0,0,0,1],
            [1,0,0,1,1],
            [1,0,0,0,1],
            [1,1,1,1,1],]

for i in range(len(mapArray[0])):
    for j in range(len(mapArray[1])):
        if mapArray[i][j] == 1:
            mapArray[i][j] = list(np.random.uniform(0, 1 ,3))

xPos, yPos = (1,1)
xExit, yExit = (3,3)
playerRotation = np.pi/4

while True:
    plt.hlines(-0.6, 0, 60, colors='gray', lw=165, alpha=0.5)
    plt.hlines(0.6, 0, 60, colors='lightblue', lw=165, alpha=0.5)
    xTile, yTile, ceilTile = ([], [], [])

    for i in range(60):
        playerRotation_i = playerRotation + np.deg2rad(i-30)
        x, y = (xPos, yPos)
        sin, cos = (0.02*np.sin(playerRotation_i), 0.02*np.cos(playerRotation_i))
        n = 0
        while True:
            xx, yy = (x, y)
            x, y = (x+cos, y+sin)
            n = n+1
            if abs(int(3*xx)-int(3*x)) > 0 or abs(int(3*yy)-int(3*y)) > 0:
                xTile.append(i)
                yTile.append(-1 / (0.02 * n))
                if int(x) == xExit and int(y) == yExit:
                    ceilTile.append('b')
                else:
                    ceilTile.append('k')
            if mapArray[int(x)][int(y)] != 0:
                height = np.clip(1 / (0.02 * n), 0, 1)
                color = np.asarray(mapArray[int(x)][int(y)])*(0.3 + 0.7 * height**2)
                break
        plt.vlines(i, -height, height, lw=8, colors=color)
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