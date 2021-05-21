import random
import numpy

resistorList=[]
order=[]

class Resistor():
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

print(order)

for object in order:
    for component in object:
        print(component.name,end=", ")
        
    print("")