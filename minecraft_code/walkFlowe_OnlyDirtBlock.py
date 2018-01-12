from mcpi import minecraft
from time  import sleep

mc = minecraft.Minecraft.create()

dirt = 2
flower = 38

while True :
    x,y,z = mc.player.getPos()
    block_beneath = mc.getBlock(x, y-1, z)
    if block_beneath == dirt:
        mc.setBlock(x,y,z,flower)
        sleep(0.1)
    else:
        mc.setBlock(x,y-1,z,dirt)

    #mc.setBlock(x,y,z,flower)
    #sleep(0.1)
    
