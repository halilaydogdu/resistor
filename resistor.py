colors={
"black":0,
"brown":1,
"red":2,
"orange":3,
"yellow":4,
"green":5,
"blue":6,
"violet":7,
"grey":8,
"white":9
}
tolerance={
"brown":1,
"red":2,
"green":0.5,
"blue":0.25,
"violet":0.1,
"grey":0.05,
"gold":5,
"silver":10
}

bands=int(input("how many bands: "))

if bands==4:

    first=input("first color: ")
    second=input("second color: ")
    third=input("third color: ")
    fourth=input("fourth color: ")

    first_number=colors[first]
    second_number=colors[second]
    multiplier=colors[third]
    tol=tolerance[fourth]

    number=first_number*10
    number=number+second_number
    value=number*(10**multiplier)
    min_value=value-(value*tol/100)
    max_value=value+(value*tol/100)

    print("resistance:",value,"ohms")
    print("tolerance:",tol,"%")
    print("minimum:",min_value,"ohms")
    print("maximum:",max_value,"ohms")

elif bands==5:

    first=input("first color: ")
    second=input("second color: ")
    third=input("third color: ")
    fourth=input("fourth color: ")
    fifth=input("fifth color: ")

    first_number=colors[first]
    second_number=colors[second]
    third_number=colors[third]
    multiplier=colors[fourth]
    tol=tolerance[fifth]

    number=first_number*100
    number=number+second_number*10
    number=number+third_number
    value=number*(10**multiplier)
    min_value=value-(value*tol/100)
    max_value=value+(value*tol/100)

    print("resistance:",value,"ohms")
    print("tolerance:",tol,"%")
    print("minimum:",min_value,"ohms")
    print("maximum:",max_value,"ohms")

else:
    print("wrong number")