"""Game runner module"""

import cv2
import numpy as np
import mss
import pyautogui as pag
import time

from lib.image_processing import find_edges, group_features

def find_dino(time_limit=10):
    dino_template = cv2.imread('./assets/dino_crop.png')
    dino_template = cv2.cvtColor(dino_template, cv2.COLOR_BGR2GRAY)
    dino_bordered_template = find_edges(dino_template)
    dino_h, dino_w = dino_bordered_template.shape

    with mss.mss() as sct:
        timer = time.time()

        while True:
            all_monitors = sct.grab(sct.monitors[1])
            rgb_screen = np.array(all_monitors)
            edges_on_canvas = cv2.cvtColor(rgb_screen, cv2.COLOR_RGB2GRAY)

            screen_edges = find_edges(edges_on_canvas)

            match_res = cv2.matchTemplate(screen_edges, dino_bordered_template, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, max_loc = cv2.minMaxLoc(match_res)

            timer_delta = time.time() - timer

            if (max_val > 0.7):
                return {
                    "left": (max_loc[0] + dino_w) // 2,
                    "top": max_loc[1] // 2,
                    "width": 6 * dino_w,
                    "height": (dino_h - 10) // 2,
                }
            elif (timer_delta > time_limit):
                print(f"no luck to find dino for the last {timer_delta} seconds")
                break

def capture_region(region):
    with mss.mss() as sct:
        monitor_region = {**region, 'monitor': sct.monitors[1]}
        timer = time.time()
        jump_time = 0.6

        prev_state = {
            'speed': 0,
            'time_point': timer,
            'closest_element': None,
        }

        while True:
            working_area = np.array(sct.grab(monitor_region))
            gray_area = cv2.cvtColor(working_area, cv2.COLOR_BGR2GRAY)

            edges_on_canvas = find_edges(gray_area)
            features = group_features(edges_on_canvas)

            current_time = time.time()

            if len(features) > 0:
                # TODO do not count on the features which are too close
                if prev_state['closest_element'] and prev_state['closest_element'][0] > prev_state['closest_element'][1]:
                    d_distance = prev_state['closest_element'][0] - features[0][0]
                    d_time = current_time - prev_state['time_point']
                    prev_state['time_point'] = current_time
                    if d_distance > 0:
                        speed = d_distance // d_time
                        prev_state['speed'] = speed if prev_state['speed'] < speed else prev_state['speed']

                prev_state['closest_element'] = features[0]

                # TODO try polynomial to get a better precision 
                dinamic_distance = 50 + 0.008 * prev_state['speed']
                if features[0][0] < (dinamic_distance + features[0][1]):
                    pag.press('space')

            for left, width in features:
                cv2.rectangle(gray_area, (left, 1), (left + width, 2 * region['height'] - 1), color=(150, 150, 150), thickness=2)
            text = 'Time: %1.2f, Speed: %1.2f' % (time.time() - timer, prev_state['speed'])
            cv2.putText(gray_area, text, (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 255)
            cv2.imshow('frame', gray_area)

            if (cv2.waitKey(16) & 0xFF == ord('q')):
                break

        cv2.destroyAllWindows()
        

def main():
    """Running the main program"""
    region = find_dino()
    capture_region(region)


if __name__ == "__main__":
    main()
