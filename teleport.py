import time,random,mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

x = random.randint(0,100)
y = random.randint(0,100)
z = random.randint(0,100)

#counting down until teleportation by posting a message to chat
while True:
    time.sleep(3)
    mc.postToChat("Teleporting in 3")
    time.sleep(1)
    mc.postToChat("Teleporting in 2")
    time.sleep(1)
    mc.postToChat("Teleporting in 1")
    time.sleep(1)

    #changes position of the player

    mc.player.setPos(x,y,z)
    time.sleep(2)
    mc.player.setPos(x,y,z)
    time.sleep(2)
    mc.player.setPos(x,y,z)
    time.sleep(1)
    mc.postToChat("Teleportation complete")
    time.sleep(4)
