from net import Net


n = Net()
#n.testCalculation()

n.read_testdata('/home/gilbert/proj/sc2dm/pysc2/testdata.txt')
n.initializeWeights(2,3,1)
n.query(2, 3)

