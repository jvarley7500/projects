import picamera,time #imports the camera and time

with picamera.PiCamera() as camera: 
    camera.resolution = 1024,768) #sets the camera resolution
    camera.start_preview()

    time.sleep(2)#waits for two seconds
    camera.capture("picture.jpeg")#takes a picture and calls it picture
