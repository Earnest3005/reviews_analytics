data = []
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆 留言字數小於100')

good = []
for d in data:
	if 'good' in d or 'Good' in d:
		good.append(d)
print('一共有', len(good), '筆留言提到good')
