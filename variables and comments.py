Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
num1,num2,num3=10,20,30
print(num1)
10
print(num2)
20
print(num3)
30
>>> print("num3")
num3
>>> num1=num2=num3=10
>>> print(num1)
10
>>> print(num2,num3)
10 10
>>> print(id(num1))
140724092265672
>>> print(id(num2))
140724092265672
>>> 
>>> a,b=20,30
>>> print(id(a),id(b))
140724092265992 140724092266312
>>> a,b=257,257
>>> print(id(a),id(b))
2594479135984 2594479135984
>>> 
>>> a,b=10,20
>>> a,b=b,a
>>> print(a,b)
20 10
>>> 
>>> a,b=10,20
>>> print(id(a),id(b))
140724092265672 140724092265992
>>> a,b=b,a
>>> print(id(a),id(b))
140724092265992 140724092265672
>>> print(a,b)
20 10
