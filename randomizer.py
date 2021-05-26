#may 21 2021
import random
import numpy

resistorList=[]
order=[]

masterList=numpy.array()

class Component():
    def location(self,x1,y1,x2,y2):
        self.location1=tuple(x1,y1)
        self.location2=tuple(x2,y2)

class VoltageSource(Component):
    def __init__(self, name, voltage):
        self.name=name
        self.voltage=voltage

class Resistor(Component):
    def __init__(self, name, resistance):
        self.name=name
        self.resistance=resistance

def generateResistor(number):
    for x in range(number):
        name="R"+str(x)
        resistorList.append(Resistor(name, random.randint(100,500)))

generateResistor(10)

random.shuffle(resistorList)

while len(resistorList)>0:
    temp=[]
    for x in range(random.randint(1,len(resistorList))):
        temp.append(resistorList.pop())
    
    order.append(temp)

# print(order)

for object in order:
    for component in object:
        print(component.name,end=", ")
        
    print("")