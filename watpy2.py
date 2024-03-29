import numpy
numpy.set_printoptions(threshold=numpy.nan)
import pprint

def tensor(a,b):
	aShape = numpy.array(a.shape)
	bShape = numpy.array(b.shape)
	new = numpy.zeros(bShape*aShape)
	for i in range(aShape[0]):
		for j in range(aShape[1]):
			new[i*bShape[0]:(i+1)*bShape[0],j*bShape[1]:(j+1)*bShape[1]] = a[i,j]*b
	return new

def tensorNew(a,b):
	aShape = numpy.array(a.shape)
	bShape = numpy.array(b.shape)
	new = numpy.zeros(bShape*aShape)
	for i in range(aShape[0]):
		new[i*bShape[0]:(i+1)*bShape[0]] = a[i]*b
	return new

def formatTensors(arList):
	targ = []
	dic = {
			'z': numpy.array([[1,0],[0,-1]]), 
			'x': numpy.array([[0,1],[1,0]]), 
			'i': numpy.array([[1,0],[0,1]])}
	for i in arList:
		targ += [dic[i]]
	return targ

def doAllTensorThings(targ):
	targ = formatTensors(targ)
	tot = tensor(targ[1],targ[0])
	if len(targ) > 2:
		for i in range(2,len(targ)):
			tot = tensor(tot,targ[i])
	return tot

def makeState(stateList,signs):
	dic = {
			'0': numpy.array([1,0]),
			'1': numpy.array([0,1])}
	cust = []
	for i in stateList:
		tot = tensorNew(dic[i[1]],dic[i[0]])
		for j in range(2,len(i)):
			tot = tensorNew(tot,dic[i[j]])
		cust += [tot]
	t = 0 
	red = signs[t]*tot[t]
	for k in cust:
		
		red += signs[t]*k
		t += 1
	return red

def printNiceArray(ar):
	for i in range(ar.shape[0]):
		row = ''
		for j in range(ar.shape[1]):
			if ar[i,j] < 0:
				row += str(int(ar[i,j]))+' '
			else:
				row += ' '+str(int(ar[i,j]))+' '

		print row

def printNiceList(ar):
	row = ''
	for j in range(ar.shape[0]):
		if ar[j] < 0:
			row += str(int(ar[j]))+' '
		else:
			row += ' '+str(int(ar[j]))+' '

	print row


state1 = ['0000','1100','0011','1111']

signs = [1,1,1,1]

state2 = ['0110','1010','0101','1001']

bingo = [['i','i','x','x'],['x','x','i','i'],['z','z','z','z']]


for d in bingo:
	print "State:"
	printNiceList(makeState(state2,signs))
	print "Operator:"
	printNiceArray(doAllTensorThings(d))
	print "Output:"
	printNiceList(numpy.dot(doAllTensorThings(d),makeState(state2,signs)))
	print "1 * State == Operator * State:"
	print numpy.array_equal(makeState(state2,signs), numpy.dot(doAllTensorThings(d),makeState(state2,signs)))
	print 

for d in bingo:
	print "State:"
	printNiceList(makeState(state1,signs))
	print "Operator:"
	printNiceArray(doAllTensorThings(d))
	print "Output:"
	printNiceList(numpy.dot(doAllTensorThings(d),makeState(state1,signs)))
	print "1 * State == Operator * State:"
	print numpy.array_equal(makeState(state1,signs), numpy.dot(doAllTensorThings(d),makeState(state1,signs)))
	print 
