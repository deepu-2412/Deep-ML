import numpy as np
def cosine_similarity(v1, v2):
	d = np.dot(v1, v2)
    return round(d/(np.linalg.norm(v1)*np.linalg.norm(v2)),3)
	pass
