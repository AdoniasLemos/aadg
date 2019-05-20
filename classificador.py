import cv2
import numpy as np
# import matplotlib.pyplot as plt

colors = {"b": 0, "w": 1}


def get_frenq_branco(image):
    freq_branco = 0
    for color in colors:
        histograma = cv2.calcHist([image], [colors[color]], None, [256], [0, 256])

        for i in range(205, 255):
            freq_branco += histograma[i]

            print(freq_branco)
"""for hist in histograma:
dom = (np.max(histograma))
histograma[255]"""