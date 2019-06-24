import cv2
import math
import numpy as np

def supress(x):
    for f in fs:
        distx = f.pt[0] - x.pt[0]
        disty = f.pt[1] - x.pt[1]
        dist = math.sqrt(distx*distx + disty*disty)
        if (f.size > x.size) and (dist<f.size/2):
            return True

detector = cv2.MSER_create()
image = cv2.imread("./image/xdr.jpg")
height, width = image.shape[:2]
detect_area = image[0:270,150:850,:]
result_image = image.copy()
gray_image = cv2.cvtColor(detect_area, cv2.COLOR_BGR2GRAY)

fs = detector.detect(gray_image)
fs.sort(key = lambda x: -x.size)
sfs = [x for x in fs if not supress(x)]
print("There are "+str(len(sfs)*2)+" holes on Pro Display XDR.")

for f in sfs:
        cv2.circle(result_image, (int(f.pt[0])+150, int(f.pt[1])), int(f.size/2), (0,0,255), 2, -1)
        cv2.circle(result_image, (int(f.pt[0])+150, int(f.pt[1])+257), int(f.size/2), (0,0,255), 2, -1)

cv2.imwrite("./image/xdr_result.jpg", result_image)