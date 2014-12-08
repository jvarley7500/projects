import picamera,time #imports the camera and time

for picture in range(5):
    name = input("What is your name?")
    with picamera.PiCamera() as camera: 
        camera.resolution = (1024,768) #sets the camera resolution
        camera.start_preview()
        time.sleep(2)#waits for two seconds
        camera.capture(name+".jpeg")#takes a picture and calls it picture
