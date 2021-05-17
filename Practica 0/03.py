
try:
    hour = int(input("Enter Hours: "))
    rate = int(input("Enter Rate: "))
    if(hour >= 40):
        Pay = (40 * rate) + ((rate * 1.5) * (hour - 40))
    else:
        Pay = hour * rate
    print("Pay: " + str(Pay))

except:
    print("Error, please enter numeric input")
    