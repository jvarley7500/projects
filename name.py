import mcpi.minecraft as minecraft, time
mc = minecraft.Minecraft.create()

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

def j(x,y,z,colour):
    mc.setBlock(x+2,y+1,z,35,colour)
    mc.setBlocks(x+3,y,z,x+4,y,z,35,colour)
    mc.setBlocks(x+5,y+1,z,x+5,y+6,z,35,colour)
    mc.setBlocks(x+4,y+6,z,x+6,y+6,z,35,colour)

def v(x,y,z,colour):
    mc.setBlocks(x+8,y+3,z,x+8,y+6,z,35,colour)
    mc.setBlocks(x+9,y+1,z,x+9,y+2,z,35,colour)
    mc.setBlock(x+10,y,z,35,colour)
    mc.setBlocks(x+11,y+1,z,x+11,y+2,z,35,colour)
    mc.setBlocks(x+12,y+3,z,x+12,y+6,z,35,colour)

def m(x,y,z,colour):
    mc.setBlocks(x+1,y,z,x+1,y+7,z,35,colour)
    mc.setBlock(x+2,y+6,z,35,colour)
    mc.setBlocks(x+3,y+4,z,x+3,y+5,z,35,colour)
    mc.setBlock(x+4,y+6,z,35,colour)
    mc.setBlocks(x+5,y,z,x+5,y+7,z,35,colour)

m(0,20,0,10)
