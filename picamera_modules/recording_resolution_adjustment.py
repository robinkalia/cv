#!/usr/bin/env

# Robin Kalia
# robinkalia@berkeley.edu
# recording_resolution_adjustment.py: Contains the code for adjusting the resolution 
#									  of camera for recording while recording video

import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.start_preview()
    camera.start_recording('foo.h264')
    camera.wait_recording(60)
    camera.stop_recording()
    camera.stop_preview()