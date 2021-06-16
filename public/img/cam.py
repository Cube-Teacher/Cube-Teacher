from flask import Flask, render_template, Response, send_file
import cv2
import pupil_apriltags as apriltag
from pupil_apriltags import Detector
import time
import sys
import numpy as np

app = Flask(__name__)

# camera = cv2.VideoCapture(0)
detector1 = apriltag.Detector(families='tag36h11')

def gen_frames():
    while True:
        frame = cv2.imread("a.jpg")
        if frame is None:
            continue
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/flask')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(port=5000, debug=False)
