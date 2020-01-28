"""Run the same game loop but using prerecorded video

Needed for testing purposes
"""
import cv2

from dino.search import dino_search

def main():
    """Main runner"""
    cap = cv2.VideoCapture('test_assets/dino.mov')

    dino_dummy = cv2.imread('assets/dino_day.png', 0)

    battlefield = None

    while cap.isOpened():
        okay, frame = cap.read()

        if okay:
            if not battlefield:
                battlefield = dino_search(dino_dummy, cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))

            if battlefield:
                top = 2 * battlefield['top']
                height = top + 2 * battlefield['height']
                left = 2 * battlefield['left']
                width = left + 2 * battlefield['width']
                frame = frame[top: height, left: width]

                cv2.imshow('Frame', frame)

                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break

        else:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
