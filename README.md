# run-dino-run

Make Dino from chrome browser run with a bit of computer vision.
The lib which captures a screen, finds Dino on a screen and then tries to avoid the obstacles.

The idea behind the project was to test the performance of the getting and parsing screenshots by pyautogui. After all the latency between making a screenshot plus matching a template on it and making a decision to press a "jump" was enormously big. To decrease the latency I found a cross platform library which provides awesome result for grabbing a screen - https://pypi.org/project/mss/
It gives me a possibility to get a screen and perform multi matching on the screen around 28-30 times per second.


To run the script, simply install all dependencies and run: 
```
python3 run.py
```

Firs script tries to find a Dino. When Dino is detected the script searches for the obstacles on a screen and if it's too close it triggers a signal to press `space` key.

## Requirements
You need to have the next libraries installed: `numpy, opencv-python, pyautogui, mss`

*Note:* at the moment it works properly only on 13" retina display so far. The boundary is because of template match happens on original Dino screenshot. So to fix it, you need to add a Dino screenshot made from your device.

The repository uses a *git LFS* to store binary files. You need to install it in case you want to get the complete project: https://git-lfs.github.com

## Room for improvements:

 * scale Dino to template match on different displays
 * in case if it's a retina we need to recalculate a region for screenshots


Inspired by article: https://medium.com/datadriveninvestor/automating-your-job-with-python-f1952b6b640d
