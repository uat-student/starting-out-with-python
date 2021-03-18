
# CHAPTER 5: Functions



# CHAPTER 4: Repetition Structures
"""
# calculate sales commissions
# loop control variable
keep_going = "y"
# calculate a series of commissions
while keep_going == "y":
    # ask for salesperson's sales and commission rate
    sales = float(input("Enter the amount of sales: "))
    comm_rate = float(input("Enter the commission rate: "))
    # calculate the commission
    commission = sales * comm_rate
    # display the commission
    print("The commission is $", format(commission, ",.2f"), sep='')
    # ask user if they want calculate another one
    keep_going = input("Do you want to calculate another commission (Enter y for yes): ")

# check a substance's temperature

# maximum temperature variable
max_temp = 102.5
# ask for substance's temperature
temperature = float(input("Enter the substance's Celsius temperature: "))
# instruct user to adjust the thermostat
while temperature > max_temp:
    print("The temperature is too high.")
    print("Turn the thermostat down and wait")
    print("5 minutes. Take the temperature")
    print("again and enter it.")
    temperature = float(input("Enter the new Celsius temperature:"))

# ask user to check the temperature again in 15 minutes
print("The temperature is acceptable.")
print("Check it again in 15 minutes.")

# loop with the range function
for x in range(1, 10):
    print(str(x) + ": Hello World!")

# calculate the sum of a series of numbers entered by the user

max = 5  # the maximum number

# initialize the accumulator variable
total = 0.0
# explain the process
print("This program calculates the sum of")
print(max, "numbers you will enter.")
# get the numbers and accumulate them
for counter in range(max):
    number = int(input("Enter a number: "))
    total = total + number

# display the total of the numbers
print("The total is", total)

# calculate retail price
mark_up = 2.5  # the markup percentage
another = "y"  # control loop variable
ZER0 = 0
# process one or more items
while another == "y".lower():
    # ask for item's wholesale cost
    wholesale = float(input("Enter the item's wholesale cost: "))
    # validate the wholesale cost
    while wholesale < ZER0:
        print("ERROR: the cost cannot be negative.")
        wholesale = float(input("Enter the correct wholesale cost: "))
    # calculate the retail price
    retail = wholesale * mark_up
    # display the retail price
    print("Retail price: $", format(retail, ",.2f"))
    # do this again?
    another = input("Do you have another item? (Enter y for yes): ")
"""

# CHAPTER 3: Decision Structures and Boolean Logic
"""
# average three test scores and display their average
high_score = 95

# get three test scores
test1 = int(input("Enter your first test score:" ))
test2 = int(input("Enter your first test score:" ))
test3 = int(input("Enter your first test score:" ))

# calculate the average test score
average = (test1 + test2 + test3) / 3
# print the average score
print("The average score is", average)
# congratulate user if the average is a high score
if average >= high_score:
    print("Congratulations")
    print("That is a great average!")

# calculate auto repair payroll
base_hours = 40     # base hours per week
ot_multiplier = 1.5 # overtime multiplier

# ask for hours worked and hourly pay rate
hours = float(input("Enter the number of hours worked:"))
pay_rate = float(input("Enter the hourly pay rate:"))

# calculate and display gross pay
if hours > base_hours:
    # calculate gross pay with overtime
    # get the number of overtime hours worked
    overtime_hours = hours - base_hours

    # calculate the amount of overtime pay
    overtime_pay = overtime_hours * pay_rate * ot_multiplier

    # calculate the gross pay
    gross_pay = base_hours * pay_rate + overtime_pay
else:
    # calculate the gross pay without overtime
    gross_pay = hours * pay_rate

# display the gross pay
print("The gross pay is $", format(gross_pay, ",.2f"), sep='')

# determine if a bank customer qualifies for a loan
min_salary = 30000.0 # minimum annual salary
min_years = 2        # minimum years on the job

# ask for customer's annual salary
salary = float(input("Enter your annual salary:"))

# ask for number of years on the current job
years_on_job = int(input("Enter the number of years employed:"))

# determine if the customer qualifies
if salary >= min_salary or years_on_job >= min_years:
    print("You qualify for the loan.")
else:
    print("You do not qualify for this loan.")
"""

# CHAPTER 2: Input, Processing, and Output
"""
# variable demonstration
room = 100
print("My room number is", room)

# string variable
first_name = "Jane"
last_name = "Doe"
print(first_name, last_name)

# ask for user's name, age, income

name = input("What is your name? ")
age = int(input("What is your age? "))
income = float(input("What is your income? "))
# display the data
print("Name:", name)
print("Age:", age)
print("Income:", income)


# format a floating point number
amount_due = 6500.0
monthly_payment = (amount_due / 12)
print("The monthly payment is $", format(monthly_payment, ".2f"))
"""
