from sklearn.neighbors import KNeighborsClassifier
import cv2
import pickle
import numpy as np
import os
import csv
import time
from datetime import datetime
import sys
from whatsapp_sender import send_whatsapp_message
import pandas as pd
import threading

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from win32com.client import Dispatch

tts_engine = Dispatch("SAPI.SpVoice")

def speak(text):
    tts_engine.Speak(text)

video = cv2.VideoCapture(0)
facedetect = cv2.CascadeClassifier('data\\haarcascade_frontalface_default.xml')

with open('data/names.pkl', 'rb') as f:
    LABELS = pickle.load(f)
with open('data/faces_data.pkl', 'rb') as f:
    FACES = pickle.load(f)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(FACES, LABELS)

from collections import defaultdict
attendance_dict = defaultdict(lambda: [None, None]) 

img_bg = cv2.imread("background_img.png") 

while True:
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        crop_img = frame[y:y+h, x:x+w, :]
        resized_img = cv2.resize(crop_img, (50, 50)).flatten().reshape(1, -1)
        output = knn.predict(resized_img)
        ts = time.time()
        date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
        timestamp = datetime.fromtimestamp(ts).strftime("%H:%M:%S")

        if attendance_dict[output[0]][0] is None:  # Entry
            attendance_dict[output[0]][0] = timestamp  
            attendance = [output[0], timestamp, "Entry"]
            speak(f"Welcome {output[0]}, attendance taken.")
        else:  # Exit
            attendance_dict[output[0]][1] = timestamp 
            attendance = [output[0], attendance_dict[output[0]][0], timestamp, "Exit"]
            speak(f"Goodbye {output[0]}, exit recorded.")

        exist = os.path.isfile("Attendance/Attendance_" + date + ".csv")
        if exist:
            with open("Attendance/Attendance_" + date + ".csv", "+a") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(attendance)
        else:
            with open("Attendance/Attendance_" + date + ".csv", "+a") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['NAME', 'ENTRY TIME', 'EXIT TIME/ENTRY TIME', 'STATUS'])
                writer.writerow(attendance)

    frame_resized = cv2.resize(frame, (1366, 636))
    img_bg[131:131 + 636, 0:0 + 1366] = frame_resized

    cv2.imshow("Frame", img_bg)

    k = cv2.waitKey(1)
    if k == ord('o'):
        pass 
    if k == ord('q'):
        break 

video.release()
cv2.destroyAllWindows()

attendance_message = f" Attendance Marked\nName: {output[0]}\nTime: {timestamp}\nStatus: {attendance[2]}"
send_whatsapp_message("+918078445837", attendance_message)
