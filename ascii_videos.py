from ascii import transform_ascii
from cv2 import cv2

def convert_image(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    w = 200
    r = w / img.shape[1]
    h = int(img.shape[0] * r * 0.45)
    img = cv2.resize(img, (w, h))
    trans_data = transform_ascii(img)
    print(trans_data)

fin = input("input the video name: ")
cap = cv2.VideoCapture(f'videos/{fin}')

while(cap.isOpened()):
    ret, frame = cap.read()
    convert_image(frame)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
