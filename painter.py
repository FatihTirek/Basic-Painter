import cv2 as cv
import numpy as np

isDragging = False
isFilled = False # press 'f' to draw filled
radius = 15 # press '+' to increase radius '-' to decrease
thickness = 2 # press 'w' to increase thickness 's' to decrease
color = (0, 0, 255) # press c to get random color
img = np.zeros((500, 500, 3), dtype='uint8')
mode = False # press m to change shape

def squarePoints(x, y):
    pt1 = (x - radius // 2, y + radius // 2)
    pt2 = (x + radius // 2, y - radius // 2)

    return (pt1, pt2)

def drawCircle(event, x, y, flags, param):
    global isDragging

    if event == cv.EVENT_LBUTTONDOWN:
        isDragging = True
    if event == cv.EVENT_LBUTTONUP:
        isDragging = False
    if isDragging:
        if mode:
            cv.circle(param, (x, y), radius, color, -1 if isFilled else thickness)
        else:
            points = squarePoints(x, y)
            cv.rectangle(param, points[0], points[1], color, thickness)

cv.namedWindow('Painter')
cv.setMouseCallback('Painter', drawCircle, img)

while True:
    cv.imshow('Painter', img)
    key = cv.waitKey(10) & 0xFF

    if key == 27:
        break
    elif key == ord('f'):
        isFilled = not isFilled
    elif key == ord('c'):
        color = tuple([int(x) for x in np.random.randint(0, 256, 3)])
    elif key == ord('+'):
        radius += 1
    elif key == ord('w'):
        thickness += 1
    elif key == ord('-'):
        if radius >= 1:
            radius -= 1
    elif key == ord('s'):
        if thickness >= 1:
            thickness -= 1
    elif key == ord('m'):
        mode = not mode

cv.destroyAllWindows()