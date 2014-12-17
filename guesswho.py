import picamera, time, json

def getPicture(name): #takes a photo and gives it a name
    try:
        with picamera.PiCamera() as camera:
            camera.resolution = (1024,768)
            check = False
            while check == False:
                camera.start_preview()
                time.sleep(2)
                filename=name+".jpeg"
                camera.capture(filename)
                camera.stop_preview()
                if input("Is this picture okay?y/n") == "y": #asks if the picture is okay. If it isn't then it will take another picture
                    check = True
                    
    except picamera.exc.PiCameraValueError: #if there is this error it will tell the person instead of just crashing
        print("There is a problem with the camera, please check it is connected.")
        filename=""

    except picamera.exc.PiCameraMMALError:
        print("There is a problem with the camera, please try again.")
        filename = ""
              
    return filename

def getCharProfile(): #sets up a character profile
    name = ""
    while name == "":
        name = input("What is your name?")
        if input("Is this  your name: " +name) == "y": #asks if the name is correct and if it isn't will ask for their name again
            getPicture(name)
        else:
            name = ""
            
    hairColour = ""
    while hairColour == "":
        hairColour = input("What is your hair colour?")
        
    hatWear = ""
    while hatWear == "":
        hatWear = input("Are you wearing a hat?")

    eyeColour = ""
    while eyeColour == "":
        eyeColour = input("What colour are your eyes?")

    gender = ""
    while gender == "":
        gender = input("Are you male or female?")

    glasses = ""
    while glasses == "":
        glasses = input("Are you wearing glasses?")

    global profileList
    profileList = [name,hairColour,hatWear,eyeColour,gender,glasses]
    return profileList

def saveCharProfile(profiles): #saves the character profile
    profile = getCharProfile()
    profiles.append(profile)
    with open("profiles.txt",mode = "w") as my_file:
        json.dump(profiles,my_file)
    return profiles

def loadProfile():
    try:
        with open("profiles.txt",mode = "r") as my_file:
            profiles = json.load(my_file)
            print(profiles)

    except IOError:
        print("Error")
        profiles = []
    return profiles


profiles = loadProfile()
while len(profiles)<24:
    profiles = saveCharProfile(profiles)

