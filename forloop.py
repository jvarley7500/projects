#demonstration of for loops in python
import mcpi.minecraft as minecraft, time, random
mc = minecraft.Minecraft.create()

mc.setBlocks(-30,-5,-30,30,30,30,0) #makes a hole in the world that is 60 wide and 60 deep


for base in range(5):
    mc.setBlock(0,0,0,5-base,base,5-base,35,4)
    
