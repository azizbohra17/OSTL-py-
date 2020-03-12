f = open("xyz.txt","r")
w = c = l = 0
for line in f:
	l = l+1
	words = line.split()
	w = w+len(words)
	c = c+len(line)
print('Number of lines: ',l,'\nNumber of words:',w,'\nNumber of character:',c)
