# Define an output queue
import multiprocessing as mp
import random
import string
import numpy

output = mp.Queue()

# define a example function
def rand_string(pos, output):
    a=pos*3
    output.put((pos, a))

# Setup a list of processes that we want to run
def f(array):
	processes = [mp.Process(target=rand_string, args=(array[x], output)) for x in range(4)]
	return processes
# Run processes

t = numpy.array([1,2,3,4])
proc = f(t)

for p in proc:
    p.start()

# Exit the completed processes
for p in proc:
    p.join()

# Get process results from the output queue
results = [output.get() for p in proc]


print(results)
