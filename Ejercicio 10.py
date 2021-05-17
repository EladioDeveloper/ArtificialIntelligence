def Check(speed):
    if(speed <= 70):
        return "Ok"
    elif(speed > 70):
        x = speed - 70
        y = x / 5
        if(y > 12):
            return "License suspended"
        return y

while True:
    speed = int(input("Input the speed Km/h: "))
    print(Check(speed))