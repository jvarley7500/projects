import mcpi.minecraft as minecraft, time, random #imports minecraft, time, and random
mc  = minecraft.Minecraft.create() #connects to the open minecraft game

pos = mc.player.getPos()#gets players position
x1 = int(pos.x)#makes x1 equal to position x of the player but as a whole number
y1 = int(pos.y)#makes y1 equal to position y of the player but as a whole number
z1 = int(pos.z)#makes z1 equal to position z of a player but as a whole number
x = random.randint(x1-0,x1+15)#sets x to a random coordinate between 0 and 15
y = random.randint(y1-0,y1+5)#sets y to a random coordinate between 0 and 5
z = random.randint(z1-10,z1+0)#sets z to a random coordinate between 0 and 10
def invader():
    while True:#loops the indented code below
        x1 = int(pos.x)
        y1 = int(pos.y)
        z1 = int(pos.z)
        x = random.randint(x1-6,x1+15)
        y = random.randint(y1-0,y1+5)
        z = random.randint(z1-5,z1+15)
        for d in(35,0):
            for c in(14,1,4,5,3,10): #sets c to numbers in brackets
                mc.setBlocks(x+1,y+2,z,x+1,y+4,z,d,c) #sets wool blocks with the colour c to the coordinates 
                mc.setBlocks(x+2,y+4,z,x+2,y+5,z,d,c)
                mc.setBlocks(x+3,y+3,z,x+9,y+6,z,d,c)
                mc.setBlocks(x+10,y+4,z,x+10,y+5,z,d,c)
                mc.setBlocks(x+11,y+2,z,x+11,y+4,z,d,c)
                mc.setBlock(x+3,y+2,z,d,c) #sets a singular wool block with the colour c to the coordinates 
                mc.setBlock(x+9,y+2,z,d,c)
                mc.setBlocks(x+4,y+1,z,x+5,y+1,z,d,c)
                mc.setBlocks(x+7,y+1,z,x+8,y+1,z,d,c)
                mc.setBlock(x+8,y+7,z,d,c)
                mc.setBlock(x+9,y+8,z,d,c)
                mc.setBlock(x+4,y+7,z,d,c)
                mc.setBlock(x+3,y+8,z,d,c)
                mc.setBlock(x+4,y+5,z,d,15)#sets the colour to 15
                mc.setBlock(x+8,y+5,z,d,15)
                if d == 35:
                    time.sleep(0.35) #waits 0.3 seconds
                else:
                    time.sleep(0.1)  #waits 0.1 seconds  


invader()#makes the invader function go
