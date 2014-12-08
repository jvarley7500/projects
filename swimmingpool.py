import mcpi.minecraft as minecraft #imports minecraft and renames it to shorten it
mc = minecraft.Minecraft.create() #opens connection to the current minecraft game

#making a swimming pool
mc.setBlocks(0,0,0,10,10,25,20) #makes a glass cuboid
mc.setBlocks(1,1,1,8,10,23,9) #fills the glass cuboid with water
mc.player.setPos(20,20,20) #teleports player to near the pool
