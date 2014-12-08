import mcpi.minecraft as minecraft, time
mc = minecraft.Minecraft.create()

while True:
    pos = mc.player.getPos()
    x = pos. x
    y = pos. y
    z = pos. z
    block = 41
    mc.setBlock(x, y, z, block)
    time.sleep(0.2)
