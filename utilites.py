import os
import cv2

def getImagesOfFolder(folder):
    images = []
    absolutWay = os.path.abspath(folder)
    for currentFolder, subFolders, files  in os.walk(absolutWay):
        images.extend([os.path.join(currentFolder,file) for file in files if file.endswith('.png')])
    return images

def getImageConverted(image, conversor):
    img = cv2.imread(image, 1)
    return cv2.cvtColor(img, conversor)
