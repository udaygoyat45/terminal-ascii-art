from ascii import transform_ascii
from cv2 import cv2

def convert_image():
    # read the photo
    fn = input("input file name: ")
    img = cv2.imread("photos/" + fn)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    w = 100
    r = w / img.shape[1]
    h = int(img.shape[0] * r * 0.45)
    img = cv2.resize(img, (w, h))
    # output the results
    trans_data = transform_ascii(img)
    print(trans_data)

convert_image()
