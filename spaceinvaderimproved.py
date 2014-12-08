import mcpi.minecraft as minecraft, time, random #imports minecraft and time
mc  = minecraft.Minecraft.create() #connects to the open minecraft game

pos = mc.player.getPos()
x1 = int(pos.x)
y1 = int(pos.y)
z1 = int(pos.z)
x = random.randint(x1-0,x1+15)
y = random.randint(y1-0,y1+5)
z = random.randint(z1-10,z1+0)
def invader():
    while True:
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
                mc.setBlock(x+4,y+5,z,d,15)
                mc.setBlock(x+8,y+5,z,d,15)
                if d == 35:
                    time.sleep(0.35) #waits 0.3 seconds
                else:
                    time.sleep(0.1)    


invader()
