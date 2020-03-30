# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 21:27:07 2020

@author: pavk1

Write a program to calculate the credit card balance after one year if a 
person only pays the minimum monthly payment required by the credit card 
company each month.

The following variables contain values as described below:

   1.  balance - the outstanding balance on the credit card

   2.  annualInterestRate - annual interest rate as a decimal

   3.  monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining 
balance. At the end of 12 months, print out the remaining balance. Be sure to 
print out no more than two decimal digits of accuracy - so print

Remaining balance: 813.41

instead of

Remaining balance: 813.4141998135 

So your program only prints out one thing: the remaining balance at the 
end of the year in the format:

Remaining balance: 4784.0
A summary of the required math is found below:

Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest 
rate x Monthly unpaid balance)

We provide sample test cases below. We suggest you develop your code on your 
own machine, and make sure your code passes the sample test cases, before you 
paste it into the box below.
"""

def remainingBalance(balance, annualInterestRate, monthlyPaymentRate):
    initBalance = balance
    
    for i in range(12):
        monthlyInterestRate = (annualInterestRate) / 12
        minimumMonthlyPayment = (monthlyPaymentRate) * (balance)
        monthlyUnpaidBalance = (balance) - (minimumMonthlyPayment)
        balance = (monthlyUnpaidBalance) + (monthlyInterestRate * monthlyUnpaidBalance)
#        print("This is the monthly balance:", (round(balance, 2)))
    
#    return (round(balance, 2))
    print("Original Balance:", (round(initBalance, 2)))
    print("Total Amount paid this year:", (round(minimumMonthlyPayment * 12, 2)))
    print("Remaining balance:", (round(balance, 2)))
    overpaid = (initBalance - balance) - (minimumMonthlyPayment * 12)
    print("Overpaid:", (round(overpaid, 2)))

remainingBalance(1000, .27, .04)

