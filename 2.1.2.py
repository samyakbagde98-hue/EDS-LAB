# Initial dictionary with 10 predefined records
student = {
    1: "Amit",
    2: "Riya",
    3: "Kiran",
    4: "Neha",
    5: "Arjun",
    6: "Pooja",
    7: "Rahul",
    8: "Sneha",
    9: "Vikram",
    10: "Anjali"
}
# write your code here...

print("Original Dictionary:",student)
# write your code here...
k1=int(input())
v1=input()
student.setdefault(k1,v1)
print("After Insertion:",student)
k2=int(input())
v2=input()
if k2 in student:
	student[k2]=v2
print("After Update:",student)
k3=int(input())
if k3 in student:
	del student[k3]
print("After Deletion:",student)
print("Traversing Dictionary:")
for k,v in student.items():
	print(f"{k} : {v}")

