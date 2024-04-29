def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight / (height * height)

    print("BMI = {:.2f}".format(bmi))

    if bmi < 18.5:
        print("Underweight - your wang small coz u don't eat lmao")
        return -1
    elif bmi <= 25.0:
        print("Normal weight - eh not bad wang not bad")
        return 0
    else:
        print("Overweight - welcome to big wang gang")
        return 1

weight_classification = calculate_bmi(weight=60, height=1.8)
print("Weight Classification:", weight_classification)
