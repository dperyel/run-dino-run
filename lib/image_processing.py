import cv2

def find_borders(img):
    return cv2.Canny(img, threshold1=0, threshold2=255)
