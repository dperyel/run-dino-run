import pyautogui as pag

from dino.search import find_track_region, run_game_loop
from dino.effect import Effects

if __name__ == '__main__':
    track_region = find_track_region('assets/dino_day.png')
    effects = Effects(pag)
    run_game_loop(track_region, effects)
