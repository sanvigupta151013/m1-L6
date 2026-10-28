height = int(input("Enter your height in cm: "))
weight = int(input("Enter your weight in kg: "))

BMI = weight / (height/100) ** 2

if BMI < 18.5:
    print("You are underweight.")

elif 18.5 <= BMI < 24.9:
    print("You have a normal weight.")

elif 25 <= BMI < 29.9:
    print("You are overweight.")

elif BMI >= 30:
    print("You are obese.")

elif BMI >32.9:
    print("You are severely obese.")

else:
    print("you need treatment for your health.")