import mcpi.minecraft as minecraft, time
mc = minecraft.Minecraft.create()

for block in (3,8):
    mc.setBlock(0,40,block,22)
    mc.postToChat(block)
    time.sleep(1)

