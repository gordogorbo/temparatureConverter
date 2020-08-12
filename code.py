def f_or_c():
    choice = "Wrong"
    while choice not in ['C','F','c','f']:
        choice = input("What temperature do you want to convert from, F or C?: ")
        
        if choice not in ['C','F','c','f']:
            print("Sorry, invalid choice!")
    
    if choice.lower() == 'f'
        f_to_c()
    else:
        c_to_f()
        
def f_to_c():
    valueF = input("Please input the temperature in Fahrenheit: ")
    valueF = int(valueF)

    conF = round((valueF - 32) * 5/9)
    print (f"The temparature in Celsius is: {conF}")

def c_to_f():
    valueC = input("Please input the temperature in Celsius: ")
    valueC = int(valueC)

    conC = round((valueC * 9/5) +32)
    print (f"The temparature in Fahrenheit is: {conC}")
