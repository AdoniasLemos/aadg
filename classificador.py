import cv2
from utilites import getImagesOfFolder, getImageConverted
from matplotlib import pyplot as plt

colors = {"b": 0, "w": 1}

def getFrenqBranco(image):
    freq_branco = 0
    for color in colors:
        histograma = cv2.calcHist([image], [colors[color]], None, [256], [0, 256])

        for i in range(205, 255):
            freq_branco += histograma[i]

            print(freq_branco)

def diagnosticsAll(images):
    for image in images:
        img = getImageConverted(image, cv2.COLOR_RGB2GRAY)

        ret, img_limiarizada = cv2.threshold(img,190, 255,cv2.THRESH_BINARY)
        cv2.imwrite("imageresult.png", img_limiarizada)


diagnosticsAll(getImagesOfFolder('./'))