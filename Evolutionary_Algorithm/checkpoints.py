import numpy as np

pop = dict(DNA=(np.random.rand(1, 3)*5).repeat(2, axis=0),   # initialize the pop DNA values
           mut_strength=np.random.rand(2, 3))

print(pop)