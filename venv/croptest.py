import json
import cv2
import sys
import os, io
from PIL import Image
import numpy as np

from google.cloud import vision
import pandas as pd
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'Token.json'

client = vision.ImageAnnotatorClient()


xyz = 'grn.jpeg'


image = cv2.imread(xyz)
x = 710
y = 198

h = 444

w = 900
crop = image[y:y + h, x:x + w]
cv2.imwrite('mycrop.png', crop)
