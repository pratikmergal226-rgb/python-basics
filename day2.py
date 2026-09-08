name= "pratik"
print(name)
age=20
type(age)
a= 20
b= 15
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
a+=b
print(a)

# positive index 
# negative index

name ="pratik"
name[4]
name[-3]
name[-1]
name[0]

# membership operator / boolean values/ in ,not in 

print("MH" in "MAHARASTRA")
print("MA" in "MAHARASTRA")
print("mh" in "MAHARASTRA")
print("RAST" in "MAHARASTRA")
print("RA" not in "MAHARASTRA" )
print("maharastra" not in "MAHARASTRA")


# identity operators / is, is not 

print(1 is 1)
print(7 is 7)
print(3 is 9)
print(7 is not 7)
print(7 is not 8)
print(5 is not 10)
print(9 is not 9)

## comparicances operator

print(1==1) # equal to
print(1!=4) # not equal to
print(4 != 4) # not equal to

# symbol in 
# < greter than 
# > less than

print(5>5)
print(7==7)
print(5<12)
print(12> 8)
print(50<20)
print(0<1)
print(0> 1)
print(3 > -5)
print(-100<1)
print((10+5)>(8+6))
print((7+8)>(5*3))
print((40-20)<(7*3))

## slicing [start: stop : step/jump]
# positive index start with 0
# +ve index
# Character:  D  A  T  A     A  N  A  L  Y  T  I  C  S
# Index:      0  1  2  3  4  5  6  7  8  9 10 11 12 13
                 ↑

# -ve index
# negative index start with -1 
# Index:     -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1↑
# Character:   D  A   T   A       A  N  A  L  Y  T  I  C  S

name="DATA ANALYTICS"
name[0:13:1]
name[0:8:5]
name[4:8:3]
name[-4:-10:-3]
name[0:14]
name[-14:-1]
name[::-1]
