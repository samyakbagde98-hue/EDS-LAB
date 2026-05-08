import numpy as np

# 14. print Roll number who got minimum marks in Subject 2
min=np.argmin(a[:,2])
print("Roll no who got minimum marks in Subject 2", a[min,0])

# 15. print Roll number who got 24 marks in Subject 2
roll=a[np.where(a[:,2]==24),0:1]
print("Roll no who got 24 marks in Subject 2",  roll[0] )

# 16. print count of students who got marks in Subject 1 < 40
count_less_40=np.count_nonzero(a[:,1]<40)
print("Count of students who got marks in Subject 1 < 40",count_less_40  )

# 17. print count of students who got marks in Subject 2 > 90
print("Count of students who got marks in Subject 2 > 90:",np.count_nonzero(a[:,2]>90)              )

# 18. print count of students in each subject who got marks >= 90
all1=np.sum(a[:,1:4]>=90,axis=0)
print("Count of students in each subject who got marks >= 90:",all1 )

# 19. print count of subjects in which each student got marks >= 90
print("Roll no:",a[:,0])
sub_counts=np.sum(a[:,1:4]>=90,axis=1)
print("Count of subjects in which student got marks >= 90:",sub_counts )

# 20. Print S1 marks in ascending order
print(np.sort(a[:,1]))


# 21. Print S1 marks >= 50 and <= 90
mask=(a[:,1]>=50) & (a[:,1]<=90)
print(a[mask])
print(a)
# 22. Print the index position of marks 79
print(np.where(a[:,1]==79))
