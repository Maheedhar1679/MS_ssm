#Author: Mah
#date:
#Purpose: To practice on functions

def get_ticket_price(age):

    if age < 10:
        return "No ticket"
    elif 11 <= age <= 15:
        return 100
    elif age >= 16:
        return 200
    else:
        return "Invalid age"
