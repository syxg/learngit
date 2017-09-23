#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# print(100+200+300)
# print(1+2)
# name=input()
# print(name)
# name=input("please enter your name:")
# print("hello",name)
# print("打开")

# l=[
# 	['Apple','Google','Microsoft'],
# 	['Java','Python','Ruby','PHP'],
# 	['Adam','Bart','Lisa']
# ]
# print(l[0])
# print(l[1])
# print(l[2])
# print(l)

# t=('a','b',['A','B'])
# print(t)

# age = 20
# if age >= 18:
# 	print('your age is',age)
# 	print('adult')

# s=input('birth:')
# birth=int(s)
# if birth < 2000:
# 	print('00前')
# else:
# 	print('00后')

# names = ['Michael','Bob','Tracy']
# for name in names:
# 	print(name)

# sum = 0
# for x in range(101):
# 	sum=sum+x
# print(sum)

# sum = 0
# n = 99
# while n > 0:
# 	sum=sum+n
# 	n=n-2
# print(sum)

# n=1
# while n <= 100:
# 	if n >10:
# 		break
# 	print(n)
# 	n=n+1
# print('END')

# n = 0
# while n < 10:
# 	n = n+1
# 	if n % 2 == 0:
# 		continue
# 	print(n)

# def fact(n):
# 	if n==1:
# 		return 1
# 	return n*fact(n-1)
# # print(fact(1000))
# print(fact(10))

# def fact(n):
# 	return fact_iter(n,1)
# def fact_iter(num,product):
# 	if num==1:
# 		return product
# 	return fact_iter(num-1, num*product)
# print(fact(5))fgitg
# 
# 利用递归函数移动汉诺塔:
# def move(n, a, b, c):
#     if n == 1:
#         print('move', a, '-->', c)
#     else:
#         move(n-1, a, c, b)
#         move(1, a, b, c)
#         move(n-1, b, a, c)

# move(4, 'A', 'B', 'C')

#List Comprehensions
# L=[x*x for x in range(1,11)]
# print(L)
# import os
# print([d for d in os.listdir('.')])

# L1=['Hello','World',18,'Apple',None]
# L2=[a.lower() for a in L1 if isinstance(a,str)]
# print(L2)

# generator
def triangles():
    l = [1]
    while True:
        yield l
        l = [1]+[l[n]+l[n+1] for n in range(len(l)-1)]+[1]
n=0
for t in triangles():
	print(t)
	n=n+1;
	if n==10:
		break