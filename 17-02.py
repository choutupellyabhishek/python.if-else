
total_price = float(input("Enter total purchase amount: "))

if total_price >= 1500:
    discount = total_price * 0.20  # 20% discount
    category = "Good quality"
elif total_price >= 700:
    discount = total_price * 0.15  # 15% discount
    category = "Average quality "
elif total_price >= 400:
    discount = total_price * 0.10  # 10% discount
    category = "Below Average quality"
else:
    discount = 0
    category = "No Discount"

final_price = total_price - discount

print(f"Category: {category}")
print(f"Discount Applied: ${discount:.2f}")
print(f"Final Price: ${final_price:.2f}")

'''
num_students = int(input("Enter the number of students: "))  
passing_marks = 50  # Minimum marks required to pass

for _ in range(num_students):  
    name = input("Enter student name: ")  
    marks = int(input(f"Enter marks for {name}: "))  

    if marks >= passing_marks:  
        result = "Passed "  
    else:  
        result = "Failed "  

    print(f"{name}: Marks = {marks}, Result = {result}\n")
'''