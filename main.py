import pyautogui as pag
import cv2
import numpy as np
import mss
import math
from collections import namedtuple

def find_track_region(dino_path):
    continue_searching = True

    while continue_searching:
        print('start next iteration iteration')
        location = pag.locateOnScreen(dino_path, confidence=0.7, grayscale=True)

        if location:
            continue_searching = False
            d_left, d_top, d_width, d_height = location

            track_region = namedtuple('Box', ['left', 'top', 'width', 'height'])

            return track_region(
                left = math.floor(d_left - 0.5 * d_width), 
                top = d_top - 2 * d_height, 
                width = 10 * d_width, 
                height = 4 * d_height
            )

# def same_on_gui(track_region):
#     in_game = True

#     while in_game:
#         track_screen_shot = pag.locateOnScreen(
#             'assets/cactus_day.png', region=track_region, confidence=0.6, grayscale=True)

#         if track_screen_shot:
#             if track_screen_shot.left - track_screen_shot[0] < 150:
#                 print(track_screen_shot)
#                 pag.press('space')

#         print('screen shot in a memory')

def run_game_loop(track_region):
    cactus = cv2.imread('assets/cactus_day.png', 0)

    while True:
        track_screen_shot = pag.screenshot(region=track_region)
        track = cv2.cvtColor(np.array(track_screen_shot), cv2.COLOR_RGB2GRAY)
        res = cv2.matchTemplate(track, cactus, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = np.where(res >= threshold)

        print(loc);

        for pt in zip(*loc):
            if pt[1] < 500:
                print(pt)
                pag.press('space')

        print('screen shot in a memory')

        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break


if __name__ == '__main__':
    track_region = find_track_region('assets/dino_day.png')
    run_game_loop(track_region)
