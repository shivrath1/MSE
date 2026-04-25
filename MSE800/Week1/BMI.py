# Body Mass Index (BMI) calculator

# user input
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# calculate BMI
bmi = weight / (height ** 2)

# show result
print(f"Your BMI is: {bmi:.2f}")