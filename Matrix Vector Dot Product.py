def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
    d = []
    if len(a[0])!=len(b):
        return -1
    else:
        for i in range(len(a)):
            s = 0
            for x in range(len(a[i])):
                s += a[i][x]*b[x]
            d.append(s)
    return d
	pass
