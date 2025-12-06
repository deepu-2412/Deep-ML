import numpy as np 
from scipy import stats
def descriptive_statistics(data):
	# Your code here
    a = np.array(data)
    mean = np.mean(a)
    median = np.median(sorted(a))    
    mode_res = stats.mode(a)
    mode= np.atleast_1d(mode_res.mode)[0]
    variance = np.var(a)
    std_dev = np.std(a)
    percentiles = []
    for i in range(1,4):
        percentiles.append(np.percentile(a,25*i))
    iqr = stats.iqr(a)
	stats_dict ={
        "mean": mean,
        "median": median,
        "mode": mode,
        "variance": np.round(variance,4),
        "standard_deviation": np.round(std_dev,4),
        "25th_percentile": percentiles[0],
        "50th_percentile": percentiles[1],
        "75th_percentile": percentiles[2],
        "interquartile_range": iqr
    }
	return stats_dict
