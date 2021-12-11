import os
import subprocess as sp

import numpy as np
import cv2 as cv


paths = {
    'notepad': "gnome-text-editor",
    'discord': "C:\\Users\\ashut\\AppData\\Local\\Discord\\app-1.0.9003\\Discord.exe",
    'calculator': "gnome-calculator"
}


def open_camera():
    # sp.run('start microsoft.windows.camera:', shell=True)
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        # Our operations on the frame come here
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # Display the resulting frame
        cv.imshow('frame', gray)
        if cv.waitKey(1) == ord('q'):
            break
    # When everything done, release the capture
    cap.release()
    cv.destroyAllWindows()


def open_notepad():
    os.startfile(paths['notepad'])


def open_discord():
    os.startfile(paths['discord'])


def open_cmd():
    os.system('start cmd')


def open_calculator():
    sp.Popen(paths['calculator'])