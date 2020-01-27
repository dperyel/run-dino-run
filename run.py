"""Game runner module"""
import pyautogui as pag

from dino.search import find_track_region, run_game_loop, dino_search
from dino.effect import Effects

def main():
    """Starts the game loop"""
    track_region = find_track_region('assets/dino_day.png', dino_search)
    effects = Effects(pag)
    run_game_loop(track_region, effects)

if __name__ == '__main__':
    main()
