import os
import cv2
from ultralytics import YOLO
from tracker import Tracker
import random

'''
from config  import *
import numpy as np
import pandas as pd
#import convert_all_images_to_videos
import sys
sys.path.insert(0, '/home/adeyemi/Documents/mypythonlibrary')
from myfunctions import images_to_video
import random
import cv2
from tracker import Tracker
from ultralytics import YOLO
'''
blur = 1.0
downsam_factor = 0.33
blur_and_downsample_str = 'blur_'+str(blur)+'_pixels_'+'downsample_factor_'+str(downsam_factor)

video_input_path = '../data/processed/'+ blur_and_downsample_str +'/Highway_' + blur_and_downsample_str+ '.mp4'
#video_input_path = '../data/processed/people.mp4'
video_output_path = os.path.join('.','out.mp4')

cap = cv2.VideoCapture(video_input_path)
ret, frame = cap.read()

cap_out = cv2.VideoWriter(video_output_path, cv2.VideoWriter_fourcc(*'MP4V'), cap.get(cv2.CAP_PROP_FPS),
                                 (frame.shape[1], frame.shape[0]))

model_path = '../../Velpsis_data/models/' + blur_and_downsample_str + '/weights/best.pt'
model = YOLO(model_path)
#model = YOLO('yolov8n.pt')

tracker = Tracker()
colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for j in range(10)]

while ret:

    results = model(frame)
    #print(results)


    for result in results:
        detections = []
        for r in result.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = r

            x1 = int(x1)
            x2 = int(x2)
            y1 = int(y1)
            y2 = int(y2)
            class_id = int(class_id)
            detections.append([x1, y1, x2, y2, score])

        tracker.update(frame, detections)

        for track in tracker.tracks:
            bbox = track.bbox
            x1, y1, x2, y2 = bbox
            track_id = track.track_id

            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (colors[track_id % len(colors)]), 3)

    cap_out.write(frame)
    ret,frame = cap.read()

#    ret, frame = cap.read()

cap.release()
cap_out.release()
#cv2.destroyAllWindows()





#



#if __name__ == "__main__":

#convert_all_images_to_videos



