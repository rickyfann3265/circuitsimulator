import random,numpy

resistorList=[]

class Component():
    def location(self,x1,y1,x2,y2):
        self.location1=(x1,y1)
        self.location2=(x2,y2)

class VoltageSource(Component):
    def __init__(self, name, voltage):
        self.name=name
        self.voltage=voltage

class Resistor(Component):
    def __init__(self, name, resistance):
        self.name=name
        self.resistance=resistance

#creates a function that generates N number of resistors with variable resistance of 100-500 ohms and numbers them incrementally
def generateResistor(number):
    for x in range(number):
        name="R"+str(x)
        resistorList.append(Resistor(name, random.randint(100,500)))

#generate desired number of resistors
numResistors=int(input())
numElements=numResistors #add the other elements when we cross that bridge
generateResistor(numResistors)

#determines the number of nodes which is dependent on the number of elements
numNodes=0
if numElements<2:
    numNodes==1

else:
    numNodes=random.randint(2,numElements)

#overall array containing all connections between nodes, without components
nodeArray=[]
for i in range(numNodes):
    for j in range(numNodes):
        if i>=j:
            nodeArray.append(None)
        else:
            nodeArray.append([])

#converts the list into an array of the appropriate randomnly generated size
nodeArray=numpy.array(nodeArray,dtype=object).reshape((numNodes,numNodes))
print(nodeArray)

#shuffles the resistors for randomization and begins to assign them appropriately
#begins with the initial required connections
random.shuffle(resistorList)
for x in range(numNodes):
    if x<numNodes-1:
        print(x)
        nodeArray[x][x+1].append(resistorList.pop())
    else:
        nodeArray[0][numNodes-1].append(resistorList.pop())

print(nodeArray)

#begins randomnly assigning the remaining resistors to valid positions in the circuit
while len(resistorList)>0:
    iRandom=random.randint(1, numNodes-1)

    jRandom=random.randint(iRandom+1, numNodes-1)
    # jRandom needs to go from iRandom+1 to numNodes-1 but runs into an issue when the array is too small, otherwise it works
