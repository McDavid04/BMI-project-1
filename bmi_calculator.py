def bmi_calc():
    weight = int(input("Enter your weight in pounds: "))
    height = int(input("Enter your height in inches: "))
    bmi = (weight * 703)/(height * height)
    if bmi < 18.5:
        print("Your BMI is ", bmi,".", "You are considered underweight and have mininal health risk associated with your condition")
    elif bmi >= 18.5 and bmi <= 24.9:
        print("Your BMI is ", bmi,".", "You are considered normal weight and have mininal health risk associated with your condition")
    elif bmi >= 25 and bmi <= 29.9:
        print("Your BMI is ", bmi,".", "You are considered overweight and have increased health risk associated with your condition")
    elif bmi >= 30 and bmi <= 34.9:
        print("Your BMI is ", bmi,".", "You are considered obese and have high health risk associated with your condition")
    elif bmi >= 35 and bmi <= 39.9:
        print("Your BMI is ", bmi,".", "You are considered severely obese and have very high health risk associated with your condition")
    else:
        print("Your BMI is ", bmi,".", "You are considered morbidly obese and have extremely high health risk associated with your condition")
    return True

bmi_calc()