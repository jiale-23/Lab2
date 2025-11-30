def cal_bmi(h, w):
    x = w/h**2
    if (x < 18.5):
        return "Underweight"
    elif (x <= 25):
        return "Normal"
    else:
        return "Overweight"


print(cal_bmi(h=1.74, w=76.4))