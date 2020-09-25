import cv2
import numpy as np

def main():
    img = cv2.imread('counterScaner.jpeg')
    showCrosshair = False
    fromCenter = False
    r = cv2.selectROI("Image",img,fromCenter, showCrosshair)
    imCrop = img[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
    cv2.imshow("Crop", imCrop)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()