"""Write a program that takes input the principal and the rate of interest. You have to calculate the simple interest for a period of 2 years

Example Input:

10000
3
Output:

600"""

p=int(input())
r=int(input())
t=2
simple_interest=(p*r*t)//100
print(simple_interest)
