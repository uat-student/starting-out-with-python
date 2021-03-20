


# CHAPTER 7: List and Tuples
"""
# print a tuple
the_tuple = (1,2,3,4,5)
print(the_tuple)

# assign random numbers to a two-dimensional list
import random

# constants for rows and columns
ROWS = 3
COLS = 4

def main():
    # create a 2D list
    values = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    # fill the list with random numbers
    for r in range(ROWS):
        for c in range(COLS):
            values[r][c] = random.randint(1, 100)

    print(values)

main()

# use "in" in a list
def main():
    product_numbers = ["V475", "F987", "Q143", "R688"]
    search = input("Enter a product number: ")
    if search in product_numbers:
        print(search, "was found in the list.")
    else:
        print(search, "was not found in the list.")

main()

# slice list
days = ["s", "m", "t", "w", "th", "f", "sat"]
print(days[2:5])

# sales list
NUMBER_DAYS = 5

def main():
    # create list to hold sales for each day
    sales = [0] * NUMBER_DAYS
    # create an index
    index = 0
    print("Enter the sales for each day.")
    # get the sales for each day
    while index < NUMBER_DAYS:
        print("Day #", index + 1, ": ", sep="", end="")
        sales[index] = float(input())
        index += 1
        # display values
    print("Here are the values you entered:")
    for value in sales:
        print(value)

# call main
main()
"""

# CHAPTER 6: Files and Exceptions
"""
# write sales amounts to a text file
def main():
    # ask for the number of days
    number_days = int(input("For how many days do you have sales?"))
    # open a new file
    sales_file = open("sales.txt", "w")
    # get the amount of sales
    for count in range(1, number_days + 1):
        # ask for the day's sales
        sales = float(input("Enter the sales for day #" + str(count) + ": "))
        # write the sales to the file
        sales_file.write(str(sales) + "\n")
    # close the file
    sales_file.close()
    print("Data has been written to sales.txt")

# call main
main()

# read from a file
def main():
    # open file
    infile = open("write_file.txt", "r")
    # read file's contents
    file_contents = infile.read()
    # close the file
    infile.close()
    # print file contents
    print(file_contents)

# call main
main()

# write to a file
def main():
    # open file
    outfile = open("write_file.txt", "w")
    # write names
    outfile.write("John Locke\n")
    outfile.write("David Hume\n")
    outfile.write("Edmund Burke\n")
    # close the file
    outfile.close()

# call main
main()
"""

# CHAPTER 5: Functions
"""
# demonstrate sqrt function
import math

def main():
    y = float(input("Enter a number: "))
    square_root = math.sqrt(y)
    print("The square root of", y, "is", square_root)

main()

# calculate a retail item's sail price
DISCOUNT_PERCENTAGE = 0.35

def main():
    reg_price = get_regular_price()
    sale_price = reg_price - discount(reg_price)
    print("The sale price is $", format(sale_price, ",.2f"), sep='')

def get_regular_price():
    price = float(input("Enter the item's regular price: "))
    return price

def discount(price):
    return price * DISCOUNT_PERCENTAGE

main()

# roll dice
# import statement
import random

# constants
MIN = 1
MAX = 6

def main():
    # loop control variable
    again = 'y'
    # simulate dice roll
    while again == 'y'.lower():
        print("Roll the dice ...")
        print("Their values are:")
        print(random.randint(MIN, MAX))
        print(random.randint(MIN, MAX))

        # roll again
        again = input("Roll the dice again? (y = yes): ")

# call main function
main()

# global constant
CONTRIBUTION_RATE = 0.10

def main():
    gross_pay = float(input("Enter the gross pay: "))
    bonus = float(input("Enter the amount of bonuses: "))
    display_pay_contribution(gross_pay)
    display_bonus_contribution(bonus)

# display retirement contribution using gross as an argument
def display_pay_contribution(gross):
    c = gross * CONTRIBUTION_RATE
    print("Contribution for gross pay: $", format(c, ",.2f"), sep='')

# display retirement contribution using bonus as an argument
def display_bonus_contribution(bonus):
    c = bonus * CONTRIBUTION_RATE
    print("Contribution for bonuses: $", format(c, ",.2f"), sep='')

# call main function
main()

# keyword arguments
def main():
    f_name = input("Enter your first name: ")
    l_name = input("Enter your last name: ")
    print("Your name reversed is")
    name_reversal(last=l_name, first=f_name)

def name_reversal(first, last):
    print(last, first)

# call main function
main()

# pass multiple arguments
def main():
    print("The sum of 2 and 4 is ")
    display_sum(2, 4)

# displays the sum of one and two
def display_sum(one, two):
    result = one + two
    print(result)

# call main function
main()

# pass an argument to a function
def main():
    number = 10
    display_triple(number)

# display the result of x times 3
def display_triple(x):
    result = x * 3
    print(result)

# call main function
main()

# demonstrate a function
def function():
    print("This is a function.")

# call the function
function()
"""

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
