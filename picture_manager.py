from picamera import PiCamera
from time import sleep


class PictureManager(object):

    def __init__(self):
        self.camera = PiCamera()
        
    def set_max_resolution(self):
        self.set_resolution()
        self.set_framerate()
        
    def set_resolution(self, length=2592, height=1944):
        self.camera.resolution = (length, height)
    
    def get_resolution(self):
        return self.camera.resolution
        
    def set_framerate(self, framerate=15):
        self.camera.framerate = framerate
    
    def get_framerate(self):
        return self.camera.framerate
    
    def take_picture(self, path, sleeptime=5):
        self.camera.start_preview()
        sleep(sleeptime)
        self.camera.capture(path)
        self.camera.stop_preview()
    
    def record_video(self, time, path):
        self.camera.start_preview()
        self.camera.start_recording(path)
        sleep(time)
        self.camera.stop_recording()
        self.camera.stop_preview()
