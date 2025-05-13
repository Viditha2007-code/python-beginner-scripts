def calculate_simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

# Example usage:
p = float(input("Enter the principal amount: "))
r = float(input("Enter the annual interest rate (in %): "))
t = float(input("Enter the time (in years): "))

si = calculate_simple_interest(p, r, t)
print(f"Simple Interest = ₹{si:.2f}")
