"""
Sofi Vinas
CIS 313 Lab 0
Computing the nth Fibonacci Number
"""
import math
#for rounding

class FibSequence(object):


    def __init__(self):
        """
        return None
        """

    def compute(self, n):
        """
        Use the golden ratio or memoization
        n is the fibonacci we want
        return an int
        """
        #GOLDEN RATIO
        n -= 1
        result = ((1.61803399**n) - ((1-1.168083399)**n)) / (5**0.5)
        return round(result)


    def display(self, step, num):
        #step (integer n from compute) ORIGINAL NUMBER
        #num (calculated fibonacci number)
        """
        1st
        2nd
        3rd

        4th
        5th
        .
        .
        .
        13th
        14th
        .
        .
        23rd
        """
        num = self.compute(step)
        #use modulo arithmetic and boolean logic
        suffixDict = {1: 'st', 2: 'nd', 3: 'rd'}
        if 10 <= step % 100 <= 20: #if step if in the 'teens'
            suffix = 'th'
        else:
            suffix = suffixDict.get(step % 10, 'th')
        print('The '+str(step)+suffix + ' Fibonacci number is: '+str(num))



def main():
    #ask user for desired fibonacci number
    print("Enter a digit or 'q' to quit: ")
    stringFibDigit = input()
    if stringFibDigit == 'q':
        return #terminate here
    elif(int(stringFibDigit) <= 0):
        return
    else:
            fibDigit = int(stringFibDigit)
            fibSeq = FibSequence() #create FibSequence instance
            num = fibSeq.compute(fibDigit) #compute returns int
            fibSeq.display(fibDigit, num) #returns nothing

if __name__ == '__main__':
    main()
