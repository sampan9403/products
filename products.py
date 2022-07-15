products = []

while True:
	name = input('enter product name: ')
	if name == 'q': # quit
		break
	price = input('enter product price: ')
	# p = []
	# p.append(name)
	# p.append(price)
	p = [name, price] # equal to line 8 to 10
	products.append(p) # or products.append([name],[price])
print(products)

products[0][0]