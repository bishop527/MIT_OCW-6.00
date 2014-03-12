# MIT OpenCourseWare Introduction to 6.00
# Problem Set 1
# 10 March 2014

#Problem 2
min_monthly_payment = 0.0
cur_balance = 0.0
month = 0
total_interest = 0.0
total_paid = 0.0
success = False

start_balance = float(raw_input("What is the starting balance? "))
cur_balance = start_balance
annual_interest_rate = float(raw_input("What is the annual interest rate? "))
monthly_interest_rate = annual_interest_rate/12.0

while success == False:
    min_monthly_payment += 10.0
    month = 0
    cur_balance = start_balance
    while month < 12 and success == False:
        month += 1
        interest_paid = round(monthly_interest_rate / 12 * cur_balance, 2)
        total_interest += interest_paid
        principle_paid = round(min_monthly_payment - interest_paid, 2)
        cur_balance = cur_balance*(1+monthly_interest_rate) - min_monthly_payment

        print "Month ", month
        print "    Min Monthly Payment = %.2f" % min_monthly_payment
    #    print "    Interest Paid = ", interest_paid
        print "    Principle Paid = %.2f" % principle_paid
        print "    Remaining Balance = %.2f" % cur_balance

        if cur_balance <= 0:
                success = True

    if cur_balance <= 0:
            success = True

print "RESULT"
print "Monthly payment to pay off debt in 1 year: ", min_monthly_payment
print "Number of months needed: ", month
print "Remaining balance: %.2f" % cur_balance


