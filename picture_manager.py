from picamera import PiCamera
from time import sleep


class PictureManager(object):

    def __init__(self):
        self.camera = PiCamera()
        
    def set_max_resolution(self):
        '''
        method setting camera to max resolution for pictures
        '''
        self.set_resolution()
        self.set_framerate()
        
    def set_resolution(self, length=2592, height=1944):
        '''
        method setting camera resolution
        :param length: length in pixel of the picture
        :param height: height in pixel of the picture
        '''
        self.camera.resolution = (length, height)
    
    def get_resolution(self):
        '''
        method returning camera resolution
        '''
        return [self.camera.resolution(0), self.camera.resolution(1)]
        
    def set_framerate(self, framerate=15):
        '''
        method setting camera framerate
        :param framerate: framerate of the camera
        '''
        self.camera.framerate = framerate
    
    def get_framerate(self):
        '''
        method returning camera framerate
        '''
        return self.camera.framerate
    
    def take_picture(self, path, sleeptime=5):
        '''
        method taking a picture and saving it to given path
        :param path: full path of the picture, need to include name of the
                     picture and extension (.jpg)
        :param sleeptime: pausing time before taking a picture, advised to 
                          leave at least 2 second for the camera to get used 
                          to the light
        '''
        self.camera.start_preview()
        sleep(sleeptime)
        self.camera.capture(path)
        self.camera.stop_preview()
    
    def record_video(self, path, time):
        '''
        method taking a video of given time and saving it to given path
        :param path: full path of the picture, need to include name of the
                     picture and extension (.h264)
        :param time: time of the video in seconds
        '''
        self.camera.start_preview()
        self.camera.start_recording(path)
        sleep(time)
        self.camera.stop_recording()
        self.camera.stop_preview()
