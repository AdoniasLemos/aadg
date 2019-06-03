import cv2
import numpy as np

colors = {"b": 0, "w": 1}


def diagnostic(path_image):

    image = cv2.imread(path_image)

    image_converted = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    image_blur = cv2.GaussianBlur(image_converted, (5, 5), 0)

    ret, th = cv2.threshold(image_blur, 205, 255, cv2.THRESH_BINARY)

    kernel = np.ones((5, 5), np.uint8)

    image_dilated = cv2.dilate(th, kernel, iterations=1)
    image_eroded = cv2.erode(image_dilated, kernel, iterations=1)
    cv2.imshow("Image", image_eroded)
    cv2.waitKey()
    media =  calc_media(image_eroded)


def calc_media(image):

    freq = 0
    divisor = 0

    hist = cv2.calcHist([image], [0], None, [256], [0, 256])

    for i in range(255):
        divisor= divisor+ 1
        freq += hist[i]
        print(hist[i])
    return freq / divisor


diagnostic('imagens/roi.png')