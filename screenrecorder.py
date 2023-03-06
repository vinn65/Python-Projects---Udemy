import cv2
from PIL import ImageGrab
import numpy as np


def ScreenRec():
    forcc  = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter("output.avi", forcc, 5.0, (1366, 768))

    while True:
        img = ImageGrab.grab()
        img_empty = np.array(img)
        frame = cv2.cvtColor(img_empty, cv2.COLOR_GRAY2BGR)
        cv2.imshow("Screen Recorder", frame)

        out.write(frame)

        if cv2.waitKey(1) == 27:
            break

    out.release()    
    cv2.destroyAllWindows()

ScreenRec()
