"""Search module contains all needed to detect elements on a screen"""
import math

import cv2
import numpy as np
import mss

def dino_search(dino_dummy, full_screen):
    """Gets a screen shot in cv2 gray format together with dino template

    Region is found when when dino is matched with more then 99% probability
    """

    res = cv2.matchTemplate(full_screen, dino_dummy, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(res)

    if max_val > 0.99:
        d_left, d_top = max_loc
        d_height, d_width = (72, 83)

        # NOTE that all attributes are divided by 2 it's needed to avoid
        # twice bigger capture region on retina display
        # Consider to fix it by analizing the monitor settings
        return {
            "top": math.floor((d_top - 2 * d_height) / 2),
            "left": math.floor((d_left + d_width)/2),
            "width": 5 * d_width,
            "height": 2 * d_height,
        }


def find_track_region(dino_path, dino_search_callback):
    """Find dino on a screen and register a region where to find obstacles"""

    with mss.mss() as sct:
        dino_dummy = cv2.imread(dino_path, 0)

        while True:
            sct_img = np.array(sct.grab(sct.monitors[1]))
            full_screen = cv2.cvtColor(sct_img, cv2.COLOR_RGB2GRAY)
            coords = dino_search_callback(dino_dummy, full_screen)
            if coords:
                return coords

def group_coords(coords, threshold=20):
    """Grouping coordinates to the clusters with a giving threshold

    Expects list of tuples: [(x, y)]
    """

    if len(coords) == 0:
        return []

    sorted_coords = sorted(coords, key=lambda tup: tup[0])
    diameter = 2 * threshold
    clusters = [[sorted_coords[0]]]

    pivot = sorted_coords[0]
    index = 0

    for coord in sorted_coords[1:]:
        if coord[0] - pivot[0] > diameter:
            index += 1
            pivot = coord
            clusters.append([coord])
        else:
            clusters[index].append(coord)

    means = map(_mean_coord, clusters)

    return list(means)

def _mean_coord(cluster):
    length = len(cluster)
    mean_x = sum(map(lambda coord: coord[0], cluster)) / length
    mean_y = sum(map(lambda coord: coord[1], cluster)) / length

    return (math.floor(mean_x), math.floor(mean_y))

def run_game_loop(track_region, effects):
    """Mane game loop

    Frequency of the loop depend on how fast does the function makes screenshots
    and how fast will the obstacle found
    """
    cactus = cv2.imread('assets/cactus_day.png', 0)

    with mss.mss() as sct:
        while True:
            track_screen_shot = np.array(sct.grab(track_region))
            track = cv2.cvtColor(track_screen_shot, cv2.COLOR_RGB2GRAY)
            res = cv2.matchTemplate(track, cactus, cv2.TM_CCOEFF_NORMED)
            threshold = 0.7
            loc = np.where(res >= threshold)
            loc = list(zip(*loc[::-1]))
            loc = group_coords(loc, 10)

            for point in loc:
                cv2.rectangle(track, point, (point[0] + 50, point[1] + 50), (0, 0, 255), 1)

            cv2.imshow('OpenCV/Numpy grayscale', track)

            for point in loc:
                if point[0] < 280:
                    effects.press_key('space')
                    break

            if cv2.waitKey(25) & 0xFF == ord("q"):
                cv2.destroyAllWindows()
                break

            # time.sleep(0.01)
