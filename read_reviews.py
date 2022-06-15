data = []
count = 0
with open('reviews.txt', 'r') as reviews:
	for review in reviews:
		data.append(review)
		count = count + 1 
		if count % 1000 == 0:
			print(len(data))
print(len(data))
print(data[0])