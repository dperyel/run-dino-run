import cv2 as cv

class Video():

    def __init__(self, path: str, step=60):
        self.path = path
        self.cap = cv.VideoCapture(path)
        self.frames_step = step
        self.frames_count = int(self.cap.get(cv.CAP_PROP_FRAME_COUNT))
        self.current_frame = 0


    def play(self):
        while self.cap.isOpened():
            print(f'Showing a frame number: {self.current_frame}')
            yield self.cap.read()
            self.current_frame += self.frames_step
            self.current_frame = min(self.current_frame, self.frames_count)
            self.cap.set(cv.CAP_PROP_POS_FRAMES, self.current_frame)

    def __enter__(self):
        return self
    
    def __exit__(self, type, value, tb):
        self.cap.release()
        print('released')
        return True