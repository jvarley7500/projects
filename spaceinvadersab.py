import mcpi.minecraft as minecraft, time #imports minecraft and time
mc  = minecraft.Minecraft.create() #connects to the open minecraft game

pos = mc.player.getPos()#gets the position of the player
x = pos.x
y = pos.y
z = pos.z

while True: #infintely loops the indented code below
    for c in(14,1,4,5,3,10): #sets c to numbers in brackets
        mc.setBlocks(x+1,y+2,z,x+1,y+4,z,35,c) #sets wool blocks with the colour c to the coordinates 
        mc.setBlocks(x+2,y+4,z,x+2,y+5,z,35,c)
        mc.setBlocks(x+3,y+3,z,x+9,y+6,z,35,c)
        mc.setBlocks(x+10,y+4,z,x+10,y+5,z,35,c)
        mc.setBlocks(x+11,y+2,z,x+11,y+4,z,35,c)
        mc.setBlock(x+3,y+2,z,35,c) #sets a singular wool block with the colour c to the coordinates 
        mc.setBlock(x+9,y+2,z,35,c)
        mc.setBlocks(x+4,y+1,z,x+5,y+1,z,35,c)
        mc.setBlocks(x+7,y+1,z,x+8,y+1,z,35,c)
        mc.setBlock(x+8,y+7,z,35,c)
        mc.setBlock(x+9,y+8,z,35,c)
        mc.setBlock(x+4,y+7,z,35,c)
        mc.setBlock(x+3,y+8,z,35,c)
        mc.setBlock(x+4,y+5,z,35,15)
        mc.setBlock(x+8,y+5,z,35,15)
        time.sleep(0.3) #waits 0.3 seconds
