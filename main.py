import pyautogui as pag
import cv2
import numpy as np
import mss
import math
import time

def find_track_region(dino_path):
    continue_searching = True
    dino_dummy = cv2.imread(dino_path, 0)

    with mss.mss() as sct:

        while continue_searching:
            sct_img = np.array(sct.grab(sct.monitors[1]))
            full_screen = cv2.cvtColor(sct_img, cv2.COLOR_RGB2GRAY)
            res = cv2.matchTemplate(full_screen, dino_dummy, cv2.TM_CCOEFF_NORMED)
            threshold = 0.9
            loc = np.where(res >= threshold)

            if len(loc[1]) > 0:
                continue_searching = False
                d_top = loc[0][0] 
                d_left = loc[1][0]
                d_height = 72
                d_width = 83

                print(math.floor((d_left - 0.5 * d_width)/2))
                # TODO move the correction for retina display to a helper
                return {
                    "top": math.floor((d_top - 2 * d_height) / 2),
                    "left": math.floor((d_left - 0.5 * d_width)/2),
                    "width": 5 * d_width,
                    "height": 2 * d_height,
                }

def run_game_loop(track_region):
    cactus = cv2.imread('assets/cactus_day.png', 0)

    with mss.mss() as sct:
        while True:
            track_screen_shot = np.array(sct.grab(track_region))
            track = cv2.cvtColor(track_screen_shot, cv2.COLOR_RGB2GRAY)
            res = cv2.matchTemplate(track, cactus, cv2.TM_CCOEFF_NORMED)
            threshold = 0.7
            loc = np.where(res >= threshold)

            for pt in zip(*loc[::-1]):
                cv2.rectangle(track, pt, (pt[0] + 50, pt[1] + 50), (0,0,255), 1)

            cv2.imshow('OpenCV/Numpy grayscale', track)

            for pt in zip(*loc[::-1]):
                print("Jump?")
                print(pt)
                if pt[0] < 360:
                    print(loc)
                    print(pt)
                    print('---------')
                    pag.press('space')
                    break

            if cv2.waitKey(25) & 0xFF == ord("q"):
                cv2.destroyAllWindows()
                break

            time.sleep(0.01)



if __name__ == '__main__':
    track_region = find_track_region('assets/dino_day.png')
    run_game_loop(track_region)
