import numpy as np
def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
    
    b = len(a[0])*len(a)
    y = new_shape[0]*new_shape[1]
    if b!=y:
        return [] 
    else:
        return np.reshape(a,new_shape).tolist()
	
