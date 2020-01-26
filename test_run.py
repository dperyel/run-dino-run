"""Run the same game loop but using prerecorded video

Needed for testing purposes
"""
import cv2

def main():
    """Main runner"""
    cap = cv2.VideoCapture('test_assets/dino.mov')

    while cap.isOpened():
        okay, frame = cap.read()

        if okay:
            cv2.imshow('Frame', frame)

            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        else:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
