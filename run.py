"""Game runner module"""

# import cv2
# import numpy as np
import mss
import mss.tools

def main():
    """Running the main program"""

    with mss.mss() as sct:

        monitor1 = {
            "top": 0,
            "left": 0,
            "width": sct.monitors[0]['width'],
            "height": sct.monitors[0]['height'],
            "mon": 1
        }

        monitor2 = {
            "top": 0,
            "left": 0,
            "width": sct.monitors[1]['width'],
            "height": sct.monitors[1]['height'],
            "mon": 2
        }


        imgM1 = sct.grab(monitor1)
        imgM2 = sct.grab(monitor2)

        mss.tools.to_png(imgM1.rgb, imgM1.size, output="test_monitor1.png")
        mss.tools.to_png(imgM2.rgb, imgM2.size, output="test_monitor2.png")





if __name__ == "__main__":
    main()
