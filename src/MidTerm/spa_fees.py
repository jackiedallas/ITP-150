"""
baggage_fees.py
@author: Jackie Johnson-Dallas
"""

import textwrap

visitor_prompt = "Please enter the number of vacationers that will be processed today: "
name_prompt = "Please enter the vacationer's last name: "
hours_prompt = "By how many hours was the checkout late: "
print("\nExclusively Celebrity Spa Late Checkout Fee Calculator")

valid_visitors = False
while not valid_visitors:
    try:
        visitors = int(input(visitor_prompt))
        if visitors > 0:
            valid_visitors = True
        else:
            print("You must enter at least 1 visitor to be processed.")
    except ValueError:
        print("Invalid input! You must enter an integer.")
        
if valid_visitors:
    
    for i in range(visitors):
        visitor_name = input(name_prompt)
        valid_hours = False
        while not valid_hours:
            hours_late = None
            # late_fee = None
            
            while hours_late is None:
                
                try:
                    hours_late = int(input(hours_prompt))
                    if (hours_late <= 0) or (hours_late > 24):
                        print("Invalid Hours Late. Hours Late must be between 1 and 24. Please re-enter.")
                        hours_late = None
                except ValueError:
                    print("Must enter an integer.")
        
            valid_hours = True
            if valid_hours:
                match hours_late:
                    case h if h == 1:
                        late_fee = 0
                    case h if h >= 2 and h <= 8:
                        late_fee = 250
                    case h if h >= 9 and h <= 16:
                        late_fee = 500
                    case h if h >= 17 and h <= 24:
                        late_fee = 1000
                indent = 40
                report = textwrap.dedent(f"""
                {'Name:':<{indent}}{visitor_name.title()}
                {'Late Checkout Fee:':<{indent}}${late_fee.__format__('.2f')}
                {'Hours Late:':<{indent}}{hours_late}                        
                """)
                print(report)
                