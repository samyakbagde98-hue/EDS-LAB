# write the code..
numbers = []
while True:
	#print("Menu:")
	print("1. Add")
	print("2. Remove")
	print("3. Display")
	print("4. Quit")
	choice = input("Enter choice: ")
	if choice == '1':
		try:
			num_input = int(input("Integer: "))
			numbers.append(num_input)
			print("List after adding:",numbers)
		except ValueError:
			print("Invalid input")
	elif choice == '2':
		if not numbers:
			print("List is empty")
		else:
			try:
				num_remove = int(input("Integer: "))
				if num_remove in numbers:
					numbers.remove(num_remove)
					print("List after removing:",numbers)
				else:
					print("Element not found")
			except ValueError:
				print("Invalid input")
	elif choice == '3':
		if not numbers:
			print("List is empty")
		else:
			print(numbers)
	elif choice == '4':
		break
	else:
		print("Invalid choice")
