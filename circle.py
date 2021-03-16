import sys
import cv2 as cv
import numpy as np


param_1 = 80
param_2 = 25
#full path to image required
if sys.argv[1] == "-help":
    print("""
    It is circle finder. 
    Required parameter is full path to image
    Additional parameters:
    -param_1 – Upper threshold for the internal Canny edge detector. Default = 80
    -param_2 – Threshold for center detection. Default = 25
    
    When image with circles is displayed, you can press "s" button to save image
    """)

else:
    file_name = sys.argv[1]
    if len(sys.argv) > 2:
        i = 2
        while i < len(sys.argv):
            if sys.argv[i] == "-param_1":
                param_1 = int(sys.argv[i+1])
                i += 2
            elif sys.argv[i] == "-param_2":
                param_2 = int(sys.argv[i + 1])
                i += 2
            else:
                print("Incorrect argument")
                i += 2


    img = cv.imread(file_name, cv.IMREAD_COLOR) # Image load

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # conversion to black and white
    gray = cv.medianBlur(gray, 5) # Blur in order to reduce noise
    
    rows = gray.shape[0] # we need it to define distance between centers of circles

    # it is the key function in searching circles
    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, rows / 16, param1=param_1, param2=param_2, minRadius=0, maxRadius=300) #parameters was adapted to selected image

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            # circle center
            cv.circle(img, center, 1, (0, 100, 100), 3)
            # circle outline
            radius = i[2]
            cv.circle(img, center, radius, (255, 0, 0), 3)
    else:
        print('No circles')
    
    
    cv.imshow("detected circles", img)
    k = cv.waitKey(0) # if "s" press, the image will be saved

    if k == ord("s"):
        cv.imwrite("image_with_circles.png", img)
