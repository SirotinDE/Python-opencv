import cv2
import numpy as np

windowName = 'Drawing Demo'

orig = np.zeros((512, 512, 3), np.uint8)
img = orig.copy()

cv2.namedWindow(windowName)

# true if mouse is pressed
drawing = False
# true if mouse moved after pressed
moved = False

(ix, iy) = (-1, -1)

# mouse callback function
def draw_shape(event, x, y, flags, param):
    global ix, iy, drawing, mode, img, moved

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        (ix, iy) = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            moved = True                    
            img = orig.copy()
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if moved == True:
            moved = False
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 1)

cv2.setMouseCallback(windowName, draw_shape)

def main():
    global mode
    
    while(True):
        cv2.imshow(windowName, img)
        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()