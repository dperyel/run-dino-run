import cv2 as cv 
import numpy as np 
from lib.video import Video

def main():

    main_window_name = 'main_window_name'
    selecting = False
    initial_x = -1
    initial_y = -1

    def crop_cb(event, x, y, flag, params):
        global initial_x, initial_y, selecting

        if event == cv.EVENT_LBUTTONDOWN:
            selecting = True
            initial_x, initial_y = x, y

        elif (event == cv.EVENT_MOUSEMOVE and selecting == True):
            print((initial_x, initial_y, x, y))
        
        elif event == cv.EVENT_LBUTTONUP:
            selecting = False
            print((initial_x, initial_y, x, y))

    cv.namedWindow(main_window_name)
    cv.setMouseCallback(main_window_name, crop_cb)

    with Video(path='./test_assets/long_run.mov', step=1000) as video:
        for _, frame in video.play():
            cv.imshow(main_window_name, frame)
            key = cv.waitKey(10000)

            elif key == ord('q'):
                break

    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
