import mcpi.minecraft as minecraft, random, time as t
mc = minecraft.Minecraft.create()

while True:
    pos = mc.player.getPos()
    x = int(pos.x)
    y = pos.y
    z = int(pos.z)
    x1 = random.randint(x-10,x+10)
    y1 = y+50
    z1 = random.randint(z-10,z+10)
    mc.setBlock(x1,y1,z1,13)
    t.sleep(0.2)
