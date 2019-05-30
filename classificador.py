import cv2
from utilites import getImagesOfFolder, getImageConverted
from matplotlib import pyplot as plt
import numpy as np

colors = {"b": 0, "w": 1}

def getFrenqBranco(image):
    freq_branco = 0
    for color in colors:
        histograma = cv2.calcHist([image], [0], None, [256], [0, 256])

        plt.plot(histograma)
        plt.xlim([0, 256])
        plt.show()

        for i in range(205, 255):
            freq_branco += histograma[i]

        print(freq_branco)

def diagnosticsAll(images):
    for image in images:
        img = getImageConverted(image, cv2.COLOR_RGB2GRAY)

        image_blur = cv2.GaussianBlur(img, (5, 5), 0)

        ret, img_limiarizada = cv2.threshold(image_blur,190, 255,cv2.THRESH_BINARY)

        # cv2.imshow("imagem"+str(image), img_limiarizada)
        # getFrenqBranco(img_limiarizada)

        kernel = np.ones((5, 5), np.uint8)
        image_dilated = cv2.dilate(img_limiarizada, kernel, iterations=1)
        cv2.imshow("Dilatada"+str(image), image_dilated)
        image_eroded = cv2.erode(image_dilated, kernel, iterations=1)
        cv2.imshow("Erodida"+ str(image), image_eroded)


        cv2.imshow("imagem" + str(image), image_eroded)
    cv2.waitKey()

diagnosticsAll(getImagesOfFolder('/'))