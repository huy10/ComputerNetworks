def stat_sort(records):
	dic_records = {}
	for item in records:
		if dic_records.has_key(item[0]):
			dic_records[item[0]][0] += item[1]
			dic_records[item[0]][1] += [item[1]]
		else:
			dic_records[item[0]] = [item[1], [item[1]]]
	sorted_records = sorted(dic_records.items(), cmp = lambda x, y: cmp(x[1][0], y[1][0]), reverse = True)
	return sorted_records
