from random import random
import math

class Net:


    def __init__(self):
        self.minput = []
        self.weight1=[[]]
        self.weight2=[[]]
        self.xhidden=[]
        self.xoutput=[]

    def read_testdata(self, filename):
        file = open(filename, 'r')
        i=0
        testdata=[]
        for line in file:
            #print(line)
            testdata.append(line.split(";"))
            i+=1


    def train(self, p1, p2, result ):
        minput=[]
        minput.append(p1)
        minput.append(p2)

        # layer 1
        layer1 = self.calculateX(minput,self.weight1)
        layer1_sig = self.addSigmoid(layer1)

        # layer 2
        layer2 = self.calculateX(layer1_sig,self.weight2)
        layer2_sig = self.addSigmoid(layer2)

        print ("output training 1 "+str(layer2_sig))



    def calculateX (self, inputs, weights ):

        # hardcoded
        #x1 = inputs[0] * weights[0][0] + inputs[1] * weights[1][0] + inputs[2] * weights[2][0]
        #x2 = inputs[0] * weights[0][1] + inputs[1] * weights[1][1] + inputs[2] * weights[2][1]
        #x3 = inputs[0] * weights[0][2] + inputs[1] * weights[1][2] + inputs[2] * weights[2][2]
        #print('calc: x1 '+str(round(x1,3)) + ' x2 ' + str(round(x2,3)) + ' x3 ' + str((round(x3,3))))
        #return [x1,x2,x3];

        moutput = []

        for i in range(0,len(inputs)):
            x = 0
            for j in range (0,len(inputs)):
                x = x + inputs[j] * weights[j][i]

            moutput.append(x)

        print ('calc: '+str(moutput))
        return moutput

    def addSigmoid (self, minput):
        moutput=[]
        for i in range(0,len(minput)):
            moutput.append(self.sigmoid(minput[i]))
        return moutput


    def testCalculation(self):
        print("----- do test calcultion -----")

        self.initializeWeights(3)

        self.minput.append(0.9)
        self.minput.append(0.1)
        self.minput.append(0.8)

        self.weight1[0][0] = 0.9
        self.weight1[0][1] = 0.2
        self.weight1[0][2] = 0.1

        self.weight1[1][0] = 0.3
        self.weight1[1][1] = 0.8
        self.weight1[1][2] = 0.5

        self.weight1[2][0] = 0.4
        self.weight1[2][1] = 0.2
        self.weight1[2][2] = 0.6

        print("starting with: ")
        print(" input:   "+str(self.minput))
        print(" weight1: "+str(self.weight1))

        moutput = self.calculateX(self.minput, self.weight1)

        if (round(moutput[0],2)==1.16 and round(moutput[1],2)==0.42 and round(moutput[2],2)==0.62):
            print('TEST OK!')
        else:
            print('TEST FAILED!!  '+str(moutput))


    def initializeWeights(self, numInputs, numNodes, numOutputs):

        for i in range(0,numNodes):
            if (i>0):
              self.weight1.append([])
            for j in range(0,numNodes):
                self.weight1[i].append(random())

        print(self.weight1)

  a
x b
y c




    def sigmoid(self,x):
        return 1 / (1 + math.exp(-x))
