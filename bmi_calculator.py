def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)

# Example usage:
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))
bmi = calculate_bmi(weight, height)

print(f"Your BMI is: {bmi}")

if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")
