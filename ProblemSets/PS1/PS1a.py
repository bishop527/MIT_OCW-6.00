# MIT OpenCourseWare Introduction to 6.00
# Problem Set 1
# 10 March 2014

#Problem 1
min_monthly_payment = 0.0
cur_balance = 0.0
month = 0
total_interest = 0.0
total_paid = 0.0

start_balance = float(raw_input("What is the starting balance? "))
cur_balance = start_balance
interest_rate = float(raw_input("What is the annual interest rate? "))
min_payment_rate = float(raw_input("What is the minimum monthly payment rate? "))

while month < 12:
    month += 1
    min_monthly_payment = round(min_payment_rate * cur_balance, 2)
    total_paid += min_monthly_payment
    interest_paid = round(interest_rate / 12 * cur_balance, 2)
    total_interest += interest_paid
    principle_paid = round(min_monthly_payment - interest_paid, 2)
    cur_balance = cur_balance - principle_paid

    print "Month ", month
    print "    Min Monthly Payment = %.2f" % min_monthly_payment
#    print "    Interest Paid = ", interest_paid
    print "    Principle Paid = %.2f" % principle_paid
    print "    Remaining Balance = %.2f" % cur_balance

print "RESULT"
print "Total amount paid: %.2f" % total_paid
print "Remaining balance: %.2f" % cur_balance

