import cv2
import numpy as np

def show_image():

    while True:
        # carregando as imagens
        img = cv2.imread("imagens/roi.png", -1)
        img_not_glaucoma = cv2.imread("imagens/not_glaucoma.png", -1)

        # transformando as imagens carregadas para a escala de cinza
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_not_glaucoma_gray = cv2.cvtColor(img_not_glaucoma, cv2.COLOR_BGR2GRAY)

        # limiarizando a imagem
        ret, thresh1 = cv2.threshold(img_gray, 205, 255
                                     , cv2.ADAPTIVE_THRESH_MEAN_C)
        ret, thresh2 = cv2.threshold(img_not_glaucoma_gray, 205, 255
                                     , cv2.ADAPTIVE_THRESH_MEAN_C)
        # exibindo a imagens do paciente com glaucoma
        cv2.imshow('Com Glaucoma (Segmentado)', thresh1)
        cv2.imshow('Com Glaucoma', img)

        # exibindo a imagens do paciente sem glaucoma
        cv2.imshow('Sem Glaucoma (Segmentado)', thresh2)
        cv2.imshow('Sem Glaucoma', img_not_glaucoma)

        cv2.waitKey(1)

show_image()




def getImage(url, format):
    image = cv2.imread(url)
    return cv2.cvtColor(image, format)
    