def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    import numpy as np
    if len(a[0])==len(b):
        a = np.array(a)
        b = np.array(b)
        return a @ b
    else:
        return -1
	
