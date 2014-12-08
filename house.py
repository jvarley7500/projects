import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

pos = mc.player.getPos()
x = int(pos.x)
y = int(pos.y)
z = int(pos.z)

mc.setBlocks(-128,128,-128,128,0,128,0)

def build_house(x,y,z):
    mc.setBlocks(x+1,y,z+1,x+6,y+6,z+6,45)
    mc.setBlocks(x+2,y+1,z+2,x+5,y+4,z+5,0)
    mc.setBlocks(x+1,y+1,z+2,x+1,y+3,z+2,0)

build_house(x,y,z)
build_house(10,20,5)
build_house(70,20,5)
build_house(80,20,5)
build_house(90,20,5)
