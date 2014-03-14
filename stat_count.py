from collections import Counter
def stat_count(list_length):
	stat_length = []
	cnt = Counter(list_length)
	stat_sorted = sorted(cnt.most_common(), cmp = lambda x,y:cmp(x[0], y[0]))
	return stat_sorted
