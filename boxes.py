import math

#ask user for input

items = int(input("Enter the number of items: "))
items_per_box = int(input("Enter the number of items per box: "))

num_of_boxes = math.ceil(items / items_per_box)

print(f"For {items} items, packing {items_per_box} items in each box, you will need {num_of_boxes} boxes")

