numbers=list(map(int, input().split()))
key= int(input())
if key in numbers:
	print(numbers.index(key))
else:
	print("Not found")
