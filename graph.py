import sys
sys.path.append(r'C:\Users\ayush\Documents\GitHub\Stack')
sys.path.append(r'C:\Users\ayush\Documents\GitHub\Queue')

#the 'r' converts normal string to raw string
#otherwise you will get the error "(unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape"

from stack import stack
from queue import *


a=queue.queue()
a.enQ(3)
a.enQ(4)
print(a)