import json
import csv
#       1.EX1
# with open("logins.txt","r") as f:
#     users=[line.strip() for line in f]
#     print("All users: ",users)
#     print("total logins :",len(users))
#     login_count = {}
#     for user in users:
#         login_count[user] = login_count.get(user,0) + 1
#     print("Login count:",login_count)
#     most_active = max(login_count,key=login_count.get)
#     print("Most active user:",most_active)
#     print("Unique users: ",set(users))
# #
#      2.EX2
# with open("numbers.txt", "r") as file:
#      numbers = [int(line.strip()) for line in file]
#
#
# print("Numbers:", numbers)
# print("Sum:", sum(numbers))
# print("Max:", max(numbers))
# print("Min:", min(numbers))
# count = len([n for n in numbers if n > 50])
# print("Numbers > 50:", count)

#      3.EX3
#
# with open("students.json", "r") as file:
#     data = json.load(file)
# students = data["students"]
# print("Student names:", [s["name"] for s in students])
# python_students = [s["name"] for s in students if s["course"] == "Python"]
# print("Python students:", python_students)
# topper = max(students, key=lambda x: x["marks"])
# print("Topper:", topper["name"])
# avg = sum(s["marks"] for s in students) / len(students)
# print("Average marks:", avg)
# course_count = {}
# for s in students:
#     course = s["course"]
#     course_count[course] = course_count.get(course, 0) + 1
# print("Course count:", course_count)

#      4.EX4
# with open("orders.json", "r") as file:
#     data = json.load(file)
# orders = data["orders"]
# print("Orders:", orders)
# total_revenue = sum(o["amount"] for o in orders)
# print("Total revenue:", total_revenue)
# spending = {}
# for o in orders:
#     cust = o["customer"]
#     spending[cust] = spending.get(cust, 0) + o["amount"]
# print("Spending per customer:", spending)
# highest = max(spending, key=spending.get)
# print("Highest spender:", highest)
# order_count = {}
# for o in orders:
#     cust = o["customer"]
#     order_count[cust] = order_count.get(cust, 0) + 1
#
# print("Order count:", order_count)

#       EX 5

#
# with open("employees.csv", "r") as file:
#     reader = csv.DictReader(file)
#     employees = list(reader)
# print("Employee names:", [e["name"] for e in employees])
# it_employees = [e["name"] for e in employees if e["department"] == "IT"]
# print("IT employees:", it_employees)
# avg_salary = sum(int(e["salary"]) for e in employees) / len(employees)
# print("Average salary:", avg_salary)
# highest = max(employees, key=lambda x: int(x["salary"]))
# print("Highest salary employee:", highest["name"])
# dept_count = {}
# for e in employees:
#     dept = e["department"]
#     dept_count[dept] = dept_count.get(dept, 0) + 1
#
# print("Department count:", dept_count)

#   EX 6

# with open("sales.csv", "r") as file:
#     reader = csv.DictReader(file)
#     sales = list(reader)
# total_revenue = sum(int(s["quantity"]) * int(s["price"]) for s in sales)
# print("Total revenue:", total_revenue)
# qty_per_product = {}
# for s in sales:
#     product = s["product"]
#     qty = int(s["quantity"])
#     qty_per_product[product] = qty_per_product.get(product, 0) + qty
#
# print("Quantity per product:", qty_per_product)
# highest_product = max(qty_per_product, key=qty_per_product.get)
# print("Highest selling product:", highest_product)
#
# revenue_per_product = {}
# for s in sales:
#     product = s["product"]
#     revenue = int(s["quantity"]) * int(s["price"])
#     revenue_per_product[product] = revenue_per_product.get(product, 0) + revenue
#
# print("Revenue per product:", revenue_per_product)
#
# high_sales = [p for p, rev in revenue_per_product.items() if rev > 50000]
# print("High sales products:", high_sales)

#Bonus exercise
qty_per_product = {}
revenue_per_product = {}

with open("sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        qty = int(row["quantity"])
        price = int(row["price"])
        qty_per_product[product] = qty_per_product.get(product, 0) + qty
        revenue = qty * price
        revenue_per_product[product] = revenue_per_product.get(product, 0) + revenue
print("Product Sales Summary")
for product in qty_per_product:
    print(f"{product} → Qty: {qty_per_product[product]} Revenue: {revenue_per_product[product]}")
