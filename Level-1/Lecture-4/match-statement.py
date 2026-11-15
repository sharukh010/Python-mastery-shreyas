"""
1. Monday 
2. Tuesday 
3. Wednesday 
4. Thursday 
5. Friday 
6. Saturday 
7. Sunday 
"""

day_number = int(input("Day number (1-7): "))
day = ""

match day_number:
    case 1: # value 1 # day_number == 1 
        day = "Monday"
    case 2: 
        day = "Tuesday"
    case 3: 
        day = "Wednesday"
    case 4: 
        day = "Thursday"
    case 5: 
        day = "Friday"
    case 6: 
        day = "Saturday"
    case 7: 
        day = "Sunday"
    case _: #default case 
        print("Invalid Day number. Day number should be between 1 to 7.")

print(day)