import mcpi.minecraft as minecraft, time as t
mc = minecraft.Minecraft.create()

#move player close to where lights will be
mc.player.setPos(10,0,0)

black=7
red=14
orange=1
green=5

#setup empty lights
def num():
    
for num in (0,1,2,3,4,5,6):
    print(num)
mc.setBlock(0,0,0,35,black)
mc.setBlock(0,1,0,35,black)
mc.setBlock(0,2,0,35,black)
mc.setBlock(0,3,0,35,black)
mc.setBlock(0,4,0,35,black)
mc.setBlock(0,5,0,35,black)

while True:
    mc.setBlock(0,5,0,35,red)
    t.sleep(7)
    mc.setBlock(0,4,0,35,orange)
    mc.setBlock(0,5,0,35,red)
    t.sleep(3)
    mc.setBlock(0,4,0,35,black)
    mc.setBlock(0,5,0,35,black)
    mc.setBlock(0,3,0,35,green)
    t.sleep(7)
    mc.setBlock(0,4,0,35,orange)
    mc.setBlock(0,3,0,35,black)
    t.sleep(4)
    mc.setBlock(0,4,0,35,black)
