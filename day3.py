 ## string formating :: %s ,%d ,% .2f,%.1f

## fstring

name= input ('please enter your name: ')

weight =int(input("plesase enter your weight:"))

## fstring

print(f'my name is {name} and my weight is {weight}kgs')

## string formating 

print("my name is %s and my weight is %d" %(name,weight))
# f string

village_name = input('enter your village name:')
print(f'my village name is {village_name}')

#fstring
print(f"my name is {weight} and my weight is {name}kgs")

print('hi, my name is {} and my weight is {}'. format(name,weight))

print('hi, my name is {0} and my weight is {1}'. format(name,weight))

print('hi, my name is {1} and my weight is {0}'. format(name,weight))

## len and center funcation
name ='swamini'
name.center(20)
len(name.center(20))
len(name)

## count funcation

string = "yashvi is trainer"
substring = "i"
count = string.count(substring)
print(count)


num = "1234"
print(num.isdigit())


num = 12 345
print(num.isdgit())

## alphanumeric
## mnje number aani alphabet 1katra
num = "hi123"
num.isalnum()

num = "hi 123"
num.isalnum()


num = "pratik 07"
num.isalnum()

# alphabet

num = 'abcd'
num.isalpha()

num = 'abc d'
num.isalpha()







###swap case 
# sagale letter capital karnyasaathi
location = "pune"
location.swapcase()

## letter capital karnya sathi
location.upper()

## letter small karnyasathi
location.lower()

# letter capitalize karnyasathi
location.capitalize()


## replace funcation
string = "hi my name is pratik. what is your name??"
string.replace('is', 'was')

string.replace('is','was',1)
string.replace('is','was',2)
string.replace('is','was',3)


## split funcation
string = "hi my name is pratik . what is your name ???"
string.split()



#### list  ###
# list  represent in []
list1 = []

## element present in the order.
## mutable : we can update and changed
## indexing can appling
## positive index start in 0
## negative index start in -1
## slicing is applicable --->>> [start: stop: step]
## we can diffeante data type string, int , complex number etc

a = [1, 1.2, 'pune',20+3j]

type(a)



## +ve indexing start with 0

student_name = ['sarah','pratik','swamini','pratiksha','saniya']
student_name[1]
student_name[3]


## -ve indexing start with -1
student_name[-3]
student_name[-2]


## slicing [start: stop: step/jump]

student_name[0:5]
student_name[1:4:2]
student_name[: :2]
student_name[::]
student_name[::-1]



list1 = eval(input('enter the numbers:'))

list2 =list(list1)

print(list2)

j=eval(input("enter the num"))
k=list(j)
print(k)