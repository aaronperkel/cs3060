import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

length = 1
width = 1
height = 1

x = 0
y = 0
z = height / 2

for i in range(10):
    pyrosim.Send_Cube(name=f"Box{i}", pos=[x,y,z+i] , size=[length,width,height])

pyrosim.End()
