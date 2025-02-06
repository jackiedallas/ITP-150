"""
pizza_truck.py
@author: Jackie Johnson-Dallas
Pizza Slice:
    Small, 1.50 per slice, Whole Pie 8.00
    Medium, 1.75 per slice, Whole Pie 10.00
    Large, 2.00 per slice, Whole Pie 12.00
    Ask the user to input the size, type and quantity
    They can only buy 1 pie at a time. They can buy 1-8 slices
    Later requirement Age >= 62 get 10% discount
"""
welcome_to_pizza_truck = """
Welcome to the Pizza Truck!
Menu:
    Small, 1.50 per slice, Whole Pie 8.00
    Medium, 1.75 per slice, Whole Pie 10.00
    Large, 2.00 per slice, Whole Pie 12.00
    You can buy only 1 pie at a time. You can buy 1-8 slices.\n
"""
print(welcome_to_pizza_truck)

s_price = 1.50
m_price = 1.75
l_price = 2.00
s_pie = 8.00
m_pie = 10.00
l_pie = 12.00
pizza_size = input("Please enter the size (S, M, L): ").upper()
pizza_type = input("Please enter the type (slice or pie): ").lower()
quantity = int(
    input("Please enter the quantity (1 for pie, 1-8 for slices.): "))
age = int(input("Please enter your age: "))

# set the price using a nested switch cases
match pizza_type:
    case 'slice':
        match pizza_size:
            case 'S':
                price = quantity * s_price
            case 'M':
                price = quantity * m_price
            case 'L':
                price = quantity * l_price
    case 'pie':
        match pizza_size:
            case 'S':
                price = quantity * s_pie
            case 'M':
                price = quantity * m_pie
            case 'L':
                price = quantity * l_pie

if age >= 62:
    age_discount = price * .10
    print("Hurray! You qualify for a senior citizen discount of 10%!")
else:
    age_discount = 0

price_after_discount = price - age_discount
print(f"""
Receipt:
    Size - {pizza_size}
    Type - {pizza_type.title()}
    Quantity - {quantity}
    Age: - {age}
    Price Before Discount: - ${price.__format__('.2f')}
    Price After Discount:  - ${price_after_discount.__format__('.2f')}
""")
