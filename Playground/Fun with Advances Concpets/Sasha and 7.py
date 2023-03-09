"""Sasha just loves the number 7 and considers it lucky. She loves it so much that she has a formula to understand if a pair of numbers are lucky are not.

If any or both of the numbers are 7, then the pair is lucky
If the sum of the numbers is 7, then the pair is lucky
If the absolute difference of the 2 numbers is 7, then the pair is lucky
Complete the given function solve that takes as parameters 2 integers and prints Lucky! if the pair is lucky. Otherwise it prints Not Lucky!

Example Input: 1 6
Output: Lucky!
Example Input: -9 -16
Output: Lucky!
Example Input: 7 95
Output: Lucky!
Example Input: 28 57
Output: Not Lucky!"""

def solve(num1,num2):
    # write your code from here
    
    if num1 == 7 or num2 == 7:
        print("Lucky!")
    elif (num1+num2) == 7:
        print("Lucky!")
    elif abs(num1 - num2) == 7:
        print("Lucky!")
    else:
        print("Not Lucky!")
