import mcpi.minecraft as minecraft #imports minecraft
mc = minecraft.Minecraft.create() #opens connection to current minecraft game

while True: #loops infinitely
    pos = mc.player.getPos()#gets players position
    x = pos.x - 1
    y = pos.y - 1
    z = pos.z - 1
    x1 = pos.x + 1
    y1 = pos.y + 1
    z1 = pos.z + 1

air = 0
while True:
    mc.setBlocks(x1, y1, z1, x, y, z,0)
