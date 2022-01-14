print('Q1')
number1=int(input('Please first number:'))
number2=int(input('Please second number:'))
number3=int(input('Please third number:'))
result=(number1+number2+number3)/3
print('the average of three numbers:',result)


print('Q2')
x=int(input('Gross income:'))
y=int(input('number of dependents:'))
I=x-10000-3000*y #Taxable Income
t=20/100*I #Tax
print('Tax:',t)


print('Q3')
A=int(input('SID:'))
B=str(input('Name:'))
C=str(input('Gender:'))
D=str(input('Course name:'))
E=float(input('CGPA:'))
x=[A,B,C,D,E]
print(x)


print('Q4')
x1=int(input('Marks of Student 1:'))
x2=int(input('Marks of Student 2:'))
x3=int(input('Marks of Student 3:'))
x4=int(input('Marks of Student 4:'))
x5=int(input('Marks of Student 5:'))
Sortedmarks=[x1,x2,x3,x4,x5]
Sortedmarks.sort()#sorting
print(Sortedmarks)


print('Q5a')
x=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
x.pop(3)#remove black
print(x)

print('Q5b')
x=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
del x[3:5]#remove black and pink
x.insert(3,'Purple')#add purple
print(x)

