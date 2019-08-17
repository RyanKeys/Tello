from djitellopy import Tello
import cv2
import pygame
from pygame.locals import *
import numpy as np
import time


class missions(object):

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Tello Feed")
        self.screen = pygame.display.set_mode([960, 720])
        self.tello = Tello()

    def run(self):

        if not self.tello.connect():
            print("Tello not connected")
            return

        if not self.tello.streamon():
            print("Could not start video stream")
            return

        frame_read = self.tello.get_frame_read()
        eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
        face_cascade = cv2.CascadeClassifier(
            'haarcascade_frontalface_default.xml')

        while True:
            self.screen.fill([0, 0, 0])
            frame = cv2.cvtColor(frame_read.frame, cv2.COLOR_BGR2RGB)
            gray = cv2.cvtColor(frame_read.frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y),
                              (x+w, y+h), (255, 0, 0), 2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y + h, x:x + w]
                eyes = eye_cascade.detectMultiScale(roi_gray)
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey),
                                  (ex+ew, ey+eh), (0, 255, 0), 2)
            frame = np.rot90(frame)
            frame = np.flipud(frame)
            frame = pygame.surfarray.make_surface(frame)
            self.screen.blit(frame, (0, 0))
            pygame.display.update()
            time.sleep(1 / 60)
        self.tello.end()


def main():
    frontend = missions()
    frontend.run()


if __name__ == "__main__":
    main()
    pass
