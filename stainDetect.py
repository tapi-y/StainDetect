#!/usr/bin/python
# -*- coding: utf-8 -*-
import cv2
import numpy as np
import time
import urllib2
import json


def upload_sensor_data(str):
    data = {'data':{'data':{'washingmachine':{
        'dirt_detect': str
    }}},
    'eventName': 'washingmachine-hack'}

    print data

    url = 'https://fy33dypvtg.execute-api.us-west-1.amazonaws.com/prod/v0/ctrl';
    req = urllib2.Request(url)
    req.add_header('Content-Type', 'application/json')
    
def judge(mask):
    mean = mask.mean()
    if(mean > 25):
        return True
    else:
        return False

def main():
    cap = cv2.VideoCapture(0)
    cap.set(3, 320)
    cap.set(4, 240)
    pre_detect_yellow = False
    pre_detect_red = False

    
    while(cap.isOpened()):

        ret, frame = cap.read()
        #time.sleep(0.5)
        cv2.imshow('Camera',frame)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        y = hsv.shape[0]/2
        x = hsv.shape[1]/2
        #print str(hsv[x,y])
        #print('H='+hsv.data[y*hsv.step + x*hsv.elemSize()+0])
    
        lower_red = np.array([0,130,150])
        upper_red = np.array([10,255,255])
        mask1 = cv2.inRange(hsv,lower_red,upper_red)
        lower_red = np.array([160,130,150])
        upper_red = np.array([179,255,255])
        mask2 = cv2.inRange(hsv,lower_red,upper_red)
        cv2.imshow('Mask_red',mask1+mask2)
        tmp = judge(mask1+mask2)
        if( tmp and pre_detect_red == False):
            upload_sensor_data('red')
            print 'RED'
        pre_detect_red = tmp
    
        lower_yellow = np.array([15,130,140])
        upper_yellow = np.array([35,255,255])
        mask = cv2.inRange(hsv,lower_yellow,upper_yellow)
        tmp = judge(mask)
        if( tmp and pre_detect_yellow == False):
            upload_sensor_data('yellow')
            #upload_sensor_data1(mask)
            print 'YELLOW'
        pre_detect_yellow = tmp
        cv2.imshow('Mask_yellow',mask)
        #print mask[x,y]
        key = cv2.waitKey(1)
        if key & 0x00FF  == ord('q'):
            break
 
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
