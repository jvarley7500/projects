import time,picamera

name = input("What is your name?")
opinion = "no"

with picamera.PiCamera() as camera:
    camera.resolution = (1024,768)
    while opinion == "n":
        camera.start_preview()
        time.sleep(2)
        camera.capture(name+".jpeg")
        camera.stop_preview()

        opinion = input("Do you like this photo?y/n")
