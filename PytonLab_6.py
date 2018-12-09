def readFile():
	#nameOfFile = input("Enter name of file: ")
	file = open('text.txt', 'r')
	data = file.read()
	file.close()
	return data
	
def putDataInList(data):
	for ch in ['.',',','!','?',';',':']:
		if ch in data:
			data=data.replace(ch, '')
	lst = data.split()
	return lst
	
def calculateNumberOfWords(lst):
	d = {}
	for i in range(len(lst)):
		if d.get(lst[i]) is None:
			d[lst[i]] = 1
		else:
			d[lst[i]] += 1
	return d
	
def printTheMostRareWord(d):
	key = ''
	value = 0
	for i in d.keys():
		if(value == 0):
			key = i
			value = d.get(i) 
		if d.get(i) < value:
			key = i
			value = d.get(i) 
	print(key, value)		
	
	
printTheMostRareWord(calculateNumberOfWords(putDataInList(readFile())))