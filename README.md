# run-dino-run

Make chrome dino run with a bit of computer vision.
The lib which capture a screen, finds dino and then tries to avoid the obstacles.

The idea behind the project was to test the performance of the getting and parsing screenshots by pyautogui. After all the latency between the makeing a screenshot plus matching a template on it and making a decision to press a "jump" was too big. To decrease the latency I found a cross platform library which provides awesome result for grabbing a screen - https://pypi.org/project/mss/
It gives me a possibility to get a screen and perform multi matching on the screen around 28-30 times per second.


*Note:* it works correctly only with retina display so far. And screenshot is taken on 1st monitor (in case you use several of them)
To run the script:
```
python3 run.py
```
You also need some additional libraries installed: `numpy, opencv-python, pyautogui, mss`

Firs script tries to find a Dino. When Dino is detected the script searches for the cactuses on a screen and if it's too close a press event on `space` key is emitted.

## Room for improvements:


### Detect a monitor type
In case if it's a retina we need to recalculate a region for screenshots


Inspired by article: https://medium.com/datadriveninvestor/automating-your-job-with-python-f1952b6b640d
