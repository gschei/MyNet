from net import Net


n = Net()
n.read_testdata('/home/gilbert/proj/sc2dm/pysc2/testdata.txt')
n.initializeWeights(2)
#n.testCalculation()
n.train(2, 3, 6)
