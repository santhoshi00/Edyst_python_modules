"""Write a program that takes as input the length and breadth of a rectangle. You must print the area and the perimeter of the rectangle

Example Input

5
10
Output

Perimeter: 30
Area: 50
"""

length=int(input())
breadth=int(input())
perimeter=int(2)*(length + breadth)
area = length * breadth
print("Perimeter: " + str(perimeter))
print("Area: " + str(area))
