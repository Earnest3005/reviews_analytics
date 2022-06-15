data = []
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '比留言字數小於100')
print(new[0])
