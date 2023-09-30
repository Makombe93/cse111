"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""
age = int(input("Please enter your age: " ))

#Calculating maximum heart rate
max_heart_rate = 220 - age

#Calculating the slowest and fastest rate
slowest = max_heart_rate * 0.65
fastest = max_heart_rate * 0.85

#My output should be
print(f"When exercising to strengthern your heart, you should keep your heart rate between {int(slowest)} and {int(fastest)} beats per minute.")