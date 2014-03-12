# MIT OpenCourseWare Introduction to 6.00
# Problem Set 1
# 10 March 2014

#Problem 3
min_monthly_payment = 0.0
cur_balance = 0.0
month = 0
total_interest = 0.0
total_paid = 0.0
success = False
tolerance = .01

start_balance = float(raw_input("What is the starting balance? "))
cur_balance = start_balance
annual_interest_rate = float(raw_input("What is the annual interest rate? "))
monthly_interest_rate = annual_interest_rate/12.0
payment_lower_bound = round((start_balance / 12.0), 2)
payment_upper_bound = round((start_balance*(1+(annual_interest_rate/12.0))**12.0/12.0),2)

min_monthly_payment = round(((payment_upper_bound + payment_lower_bound) / 2),2)
print "initial min_monthly_payment ", min_monthly_payment
print "lower bound = ", payment_lower_bound
print "upper bound = ", payment_upper_bound

while success == False:
    month = 0
    cur_balance = start_balance
    min_monthly_payment = round(((payment_lower_bound + payment_upper_bound)/2), 2)
    while month < 12 and success == False:
        month += 1
        interest_paid = round(monthly_interest_rate / 12 * cur_balance, 2)
        total_interest += interest_paid
        principle_paid = round(min_monthly_payment - interest_paid, 2)
        cur_balance = round((cur_balance + interest_paid - min_monthly_payment), 2)
        if cur_balance <= 0:
                break

    if payment_upper_bound - payment_lower_bound < tolerance:
        success = True
        print "RESULT"
        print "Monthly payment to pay off debt in 1 year: ", min_monthly_payment
        print "Number of months needed: ", month
        print "Remaining balance: %.2f" % cur_balance

    else:
        if cur_balance < 0:
            #decrease monthly payment
            payment_upper_bound = min_monthly_payment
        else:
            #increase monthly payment
            payment_lower_bound = min_monthly_payment

