x = "ranvijay"

def animal():                             # here ranvijay is global variable
    x = "aziz"                            # aziz is local variable
    return x

print(x)

def animalpark():
    y = "aziz"                      #here there is no global variable defined
    return y
print(animalpark())

