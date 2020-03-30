# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 21:27:46 2020

@author: pavk1


Now write a program that calculates the minimum fixed monthly payment needed 
in order pay off a credit card balance within 12 months. By a fixed monthly 
payment, we mean a single number which does not change each month, but 
instead is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:

    1. balance - the outstanding balance on the credit card

    2. annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment that will 
pay off all debt in under 1 year, for example:

Lowest Payment: 180 

Assume that the interest is compounded monthly according to the balance at 
the end of the month (after the payment for that month is made). The monthly 
payment must be a multiple of $10 and is the same for all months. Notice that 
it is possible for the balance to become negative using this payment scheme, 
which is okay. A summary of the required math is found below:

Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest 
rate x Monthly unpaid balance)

Test Cases to Test Your Code With. Be sure to test these on your own 
machine - and that you get the same output! - before running your code on 
this webpage!
"""

def payoffAmount(balance, annualInterestRate):
    monthlyFixedPayment = 0
    tempBalance = balance
    monthlyInterestRate = annualInterestRate / 12
        
    while balance > 0:
        for i in range(12):
            balance = balance - monthlyFixedPayment + ((balance - monthlyFixedPayment) * monthlyInterestRate)
            #what is important to note here is that it does the calculation all twelve times and then determines
            #if it is over the 0 balance, the if elif statement then works off that!!!
            #print(balance) #Just to show what happens
            #print(monthlyFixedPayment) #Just to show what happens
        if balance > 0:
            monthlyFixedPayment += .01
            balance = tempBalance
        elif balance <= 0:
            break
    print("Lowest Payment:", round(monthlyFixedPayment, 2))        
             
payoffAmount(5000, .26)     
