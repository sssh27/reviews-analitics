data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if  count % 1000 == 0 :
			print(len(data))
print('總共有', len(data), '筆資料')



sum = 0
for d in data:
 	sum _len = sum_len + len(d)
print('留言平均長度為', sum/len(data))	

new = []
for d in data:
if len(d) < 100:
	new.append(d)
	print('有', len(new), '筆資料長度小於100')

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('有', len(good), ' 筆資料提到good')


#文字計數
wc = {}
for d in data :
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1
for word in wc:
	if wc[word] > 1000:
		print(word, wc[word])
print(len(wc))
print(wc['Shawn'])

while True:
	word = input('想查什麼字?')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現', wc[word], '次')
	else:
		print('這個字沒有出現過')