print('CTI-110')
print('P3HW1-List')
print('Reggie Jean Baptiste')
print('25OCT2023')

module1=float(input("Enter grade for module 1:  "))
module2=float(input("Enter grade for module 2:  "))
module3=float(input("Enter grade for module 3:  "))
module4=float(input("Enter grade for module 4:  "))
module5=float(input("Enter grade for module 5:  "))
module6=float(input("Enter grade for module 6:  "))

grades=[ ]

grades.append(module1)
grades.append(module2)
grades.append(module3)
grades.append(module4)
grades.append(module5)
grades.append(module6)


lowgrade=min(grades)
highgrade=max(grades)
sumgrade=sum(grades)
avg=sumgrade/6

print("---------------Results---------------")
print("Lowest grade:    ",lowgrade)
print("Highest grade:   ",highgrade)
print("Sum of grades:   ",sumgrade)
print("Average:         ",avg)

print("-------------------------------------")
A_Grade = 90
B_Grade = 80
C_Grade = 70
D_Grade = 60
F_Grade = 59
if avg >= A_Grade:
 print("Your grade is: A")
if avg>= B_Grade:
  print("Your grade is: B")
if avg >= C_Grade:
  print("Your grade is: C")
if avg >= D_Grade:
  print("Your grade is: D")
if avg <= F_Grade:
  print("Your grade is: F")