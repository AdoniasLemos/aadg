import cv2
from utils import Util

def init ():
  images = Util.getImagenOfFolder(".")
  print(images)

init()