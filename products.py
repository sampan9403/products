import os # operating system

# 讀取檔案
products = [] 
if os.path.isfile('products.csv'): # 檢查檔案是否存在
	print('Yes')
	with open('products.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue # 繼續
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)
else:
	print('No')

# 讓使用者輸入
while True:
	name = input('enter product name: ')
	if name == 'q': # quit
		break
	price = input('enter product price: ')
	# p = []
	# p.append(name)
	# p.append(price)
	# p = [name, price] # equal to line 8 to 10
	products.append([name, price]) # or products.append(p)
print(products)

# 印出所有購買記錄
for p in products:
	print('the price of', p[0], 'is', p[1])

# 寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')