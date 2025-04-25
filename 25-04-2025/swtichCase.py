# Match-case statement (switch): An alternative to using many "elif" statements
# Excute some code if a value matches a 'case'
# Benefits: cleaner and syntax is more readable

def dayOfWeek(day):
    if day == 1:
        return "It is sunday"
    elif day == 2:
        return "It is Monday"
    elif day == 3:
        return "It is Tuesday"
    elif day == 4:
        return "It is WednesDay"
    elif day == 5:
        return "It is Thursday"
    elif day == 6:
        return "It is Friday"
    elif day == 7:
        return "It is Saturday"
    else:
        return "Not a valid day"
    
print(dayOfWeek(1))
print(dayOfWeek(2))
print(dayOfWeek(3))
print(dayOfWeek(4))
print(dayOfWeek(5))
print(dayOfWeek(6))
print(dayOfWeek(7))

# def dayOfWeekCase(day):
#     match day:
#         case 1:
#             return "It is sunday"
#         case 2:
#             return "It is Monday"
#         case 3:
#             return "It is Tuesday"
#         case 4:
#             return "It is WednesDay"
#         case 5:
#             return "It is Thursday"
#         case 6:
#             return "It is Friday"
#         case 7:
#             return "It is Saturday"
#         case _:
#             return "Not a valid day"

def switch_case(day):
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "saturday",
        7: "sunday"
    }
    return days.get(day, " Invalid")

print(switch_case(3))
print(switch_case(7))
