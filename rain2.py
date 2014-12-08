import mcpi.minecraft as minecraft, random, time as t
mc = minecraft.Minecraft.create()

while True: #loops infintely   
    x1 = random.randint(int(pos.x)-10),int((pos.x)+10) #makes the x coordinates a random coordinate less than 10 away from the players position
    z1 = random.randint(int(pos.z)-10,int((pos.z)+10)#makes the z coordinates a random coordinate less than 10 away from players position
    mc.setBlock(x1,y+50,z1,13) #sets gravel at the coordinates x1,y1,z1
    t.sleep(0.2) #pauses for 0.2 seconds
