def opcode(l,offset=0):
	if l[0+offset]==99:
		return l
	if l[0+offset]==1:
		l[l[3+offset]]=l[l[1+offset]]+l[l[2+offset]]
	if l[0+offset]==2:
		l[l[3+offset]]=l[l[1+offset]]*l[l[2+offset]]
	#print(l)
	return opcode(l,offset+4)

from copy import deepcopy

def main():
	input=[1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,9,1,19,1,19,5,23,1,23,6,27,2,9,27,31,1,5,31,35,1,35,10,39,1,39,10,43,2,43,9,47,1,6,47,51,2,51,6,55,1,5,55,59,2,59,10,63,1,9,63,67,1,9,67,71,2,71,6,75,1,5,75,79,1,5,79,83,1,9,83,87,2,87,10,91,2,10,91,95,1,95,9,99,2,99,9,103,2,10,103,107,2,9,107,111,1,111,5,115,1,115,2,119,1,119,6,0,99,2,0,14,0]
	for x in range(0,100):
		for y in range(0,100):
			ti=deepcopy(input)
			ti[1]=x
			ti[2]=y
#			print('trying',x,y,ti[:5])
			try:
				output=opcode(ti)
#				print('output',output[0])
			except Exception as e:
				print(e)
				pass
			if output[0]==19690720:
				print(x,y,100*x+y)
				break

