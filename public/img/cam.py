from flask import Flask, render_template, Response, send_file
import cv2
import pupil_apriltags as apriltag
from pupil_apriltags import Detector
import time
import sys
import numpy as np
import sol 

app = Flask(__name__)

camera = cv2.VideoCapture(0)
detector1 = apriltag.Detector(families='tag36h11')


def gen_frames():
    while True:
        # success, frame = camera.read()
        # if not success:
        #     break
        # else:
        #     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #     count = 0

        #     results1 = detector1.detect(gray)

        #     for tag in results1:
        #         count = count+1

        #     if(count == 9):
        #         for tag in results1:

        #             cv2.circle(frame, tuple(
        #                 tag.corners[0].astype(int)), 4, (255, 255, 255), 2)
        #             cv2.circle(frame, tuple(
        #                 tag.corners[1].astype(int)), 4, (255, 255, 255), 2)
        #             cv2.circle(frame, tuple(
        #                 tag.corners[2].astype(int)), 4, (255, 255, 255), 2)
        #             cv2.circle(frame, tuple(
        #                 tag.corners[3].astype(int)), 4, (255, 255, 255), 2)
        frame = sol.frame
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/flask')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(port=5000, debug=False)
