data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
sum = 0
for d in data:
	sum = sum + len(d)
print(sum/len(data))