import sys
sys.path.append(r'C:\Users\ayush\Documents\GitHub\Stack-Queue')

#the 'r' converts normal string to raw string
#otherwise you will get the error "(unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape"

from stackqueue import *

class graph:
	def __init__(self):
		self.store=[]

	def addVertex(self,n):
		for i in range(0,n,1):
			self.store+=[[]]
		return len(self.store)

	def addEdge(self,fromPos,toPos,unidirectional,weight):
		self.store[fromPos]+=[[toPos,weight]]
		if (unidirectional==False):
			self.store[toPos-1]=[[fromPos-1,weight]]
			return True

#Traversal Function of the entire graph. If TypeBreadth is True = Breadth-first traversal; use queue data-structure. 
#Otherwise TypeBreadth is False = Depth-first traversal; use stack data-structure.
	def traversal(self,TypeBreadth):
		Discovered=[]
		Processed=[]
		rval=[]
		if(TypeBreadth==True):
			C=queue()
		else:
			C=stack()
		for i in range(0,len(self.store)):
			Discovered+=[False]
			Processed+=[False]
		for v in self.store:
			if (Discovered[v[0]]==False):
				C.push(v[1])
				
				Discovered[v[0]]=True
			while (C.isEmpty()==False):
				w=C.pop()
				if(Processed[w]==False):
					rval+=[w]
					Processed[w]=True #and process data as required (i.e. print/read/etc.)
					print (w)
				for x in w:
					if (Discovered[x]==False):
						C.push(x)
						Discovered[x]==True
		return 0

	def printGraph(self):
		print (self.store)

g=graph()
g.addVertex(1)
g.addEdge(0,1,True,0)
g.addEdge(0,2,True,0)
g.traversal(True)










