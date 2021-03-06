# https://www.pyimagesearch.com/2015/12/21/increasing-webcam-fps-with-python-and-opencv/
# import the necessary packages
from threading import Thread
import cv2 as cv

# webcam video stream thread parent
class WebcamVideoStream:
    def __init__(self, width, height, src=0, backend=cv.CAP_DSHOW):
        # initialize the video camera stream and read the first frame
        # from the stream
        self.stream = cv.VideoCapture(src, backend)
        self.stream.set(cv.CAP_PROP_FRAME_WIDTH, width)
        self.stream.set(cv.CAP_PROP_FRAME_HEIGHT, height)
        (self.grabbed, self.frame) = self.stream.read()

        # initialize the variable used to indicate if the thread should
        # be stopped
        self.stopped = False

    def start(self):
        # start the thread to read frames from the video stream
        Thread(target=self.update, args=()).start()
        return self

    def update(self):
        # keep looping infinitely until the thread is stopped
        while True:
            # if the thread indicator variable is set, stop the thread
            if self.stopped:
                return

            # otherwise, read the next frame from the stream
            (self.grabbed, self.frame) = self.stream.read()

    def read(self):
        # return the frame most recently read
        return self.frame

    def stop(self):
        # indicate that the thread should be stopped
        self.stopped = True

# webcam video stream thread windows os specific child
# (defines necessary backend)
class WinVideoStream(WebcamVideoStream):
    def __init__(self, width, height, src=0, backend=cv.CAP_DSHOW):
        # initialize the video camera stream and read the first frame
        # from the stream
        self.stream = cv.VideoCapture(src, backend)
        self.stream.set(cv.CAP_PROP_FRAME_WIDTH, width)
        self.stream.set(cv.CAP_PROP_FRAME_HEIGHT, height)
        (self.grabbed, self.frame) = self.stream.read()

        # initialize the variable used to indicate if the thread should
        # be stopped
        self.stopped = False

# webcam video stream thread mac os specific child
# (excludes backend)
class MacVideoStream(WebcamVideoStream):
    def __init__(self, width, height, src=0):
        # initialize the video camera stream and read the first frame
        # from the stream
        self.stream = cv.VideoCapture(src)
        self.stream.set(cv.CAP_PROP_FRAME_WIDTH, width)
        self.stream.set(cv.CAP_PROP_FRAME_HEIGHT, height)
        (self.grabbed, self.frame) = self.stream.read()

        # initialize the variable used to indicate if the thread should
        # be stopped
        self.stopped = False