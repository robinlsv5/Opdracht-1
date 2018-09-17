nums = [3,5]
max = 9999

result = 0
 
for num in nums:
	for i in range(1, 1000):
		if num * i < max:
			result += num * i
print (result)

result = 0

for i in range(0, 1000):
	if i % 3 == 0 or i % 5 == 0:
		result += i
print(result)