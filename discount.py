import datetime

#Get current date from operating system

current_day = datetime.datetime.now()

#Ask user for subtotal

subtotal = float(input("Enter your subtotal: $ "))
discount_perc = 0.10
sales_tax_rate = 0.06

#Compute to see if subtotal is greater than $50 and to check whether the day is Tuesday or Wednesday
weekday = current_day.weekday()

# If the subtotal is greater than 50 and today is
# Tuesday or Wednesday, compute the discount amount.
if subtotal >= 50 and (weekday == 1 or weekday == 2):
    discount = subtotal * discount_perc
    subtotal -= discount
    print(f"Discount amount: {discount:.2f}")
    

#Compute sales_tax @6%
sales_tax = sales_tax_rate * subtotal
print(f"Sales tax amount: {sales_tax:.2f}")

#Calculate amount to be paid

total_amnt_due = subtotal + sales_tax 

print(f"Total amount due: ${total_amnt_due:.2f}")