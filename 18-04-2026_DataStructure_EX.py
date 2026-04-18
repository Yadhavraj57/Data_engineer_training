customers = [101,102,103,101,104,102,105]
unique_Customer=set(customers)
print("Unique Customers",unique_Customer)
print("Total no of unique customers",len(unique_Customer))

numbers = [10,20,10,30,20,10,40]
freq={}
for i in numbers:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)

students = {
"Rahul":85,
"Sneha":92,
"Arjun":78,
"Priya":88
}
top=max(students,key=students.get)
print(top)

avg=sum(students.values())/len(students)
print(avg)

above_85=[name for name,marks in students.items() if marks>85]
print(above_85)

inventory = {
"laptop":10,
"mouse":25,
"keyboard":15
}
inventory["Monitor"]=8
print(inventory)
inventory["laptop"]-=2
print(inventory)
lq={item:qty for item,qty in inventory.items() if qty<10}
print(lq)

emails = [
"user1@gmail.com",
"user2@yahoo.com",
"user3@gmail.com",
"user4@outlook.com"
]

domain_count={}
for email in emails:
    domain=email.split("@")[1]
    domain_count[domain]=domain_count.get(domain,0)+1
print(domain_count)

classA = {"Rahul","Sneha","Amit","Neha"}
classB = {"Sneha","Amit","Karan","Riya"}

print("Common:", classA & classB)
print("Only A:", classA - classB)
print("All students:", classA | classB)

products = {
"Laptop":75000,
"Mobile":30000,
"Tablet":25000
}

for item in products:
    products[item] *= 1.10

print(products)

sentence = "python is easy and python is powerful"

words = sentence.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)

sales = [
    {"product":"Laptop","qty":5},
    {"product":"Mouse","qty":20},
    {"product":"Laptop","qty":3},
    {"product":"Keyboard","qty":10}
]

total_sales = {}

for item in sales:
    product = item["product"]
    qty = item["qty"]
    total_sales[product] = total_sales.get(product, 0) + qty


highest = max(total_sales, key=total_sales.get)

print("Total sales:", total_sales)
print("Highest selling:", highest)

logins = [
    ("Rahul","10:00"),
    ("Sneha","10:10"),
    ("Rahul","11:00"),
    ("Arjun","11:15"),
    ("Sneha","11:30")
]

login_count = {}

for user, time in logins:
    login_count[user] = login_count.get(user, 0) + 1

print(login_count)

orders = [
    {"order_id":1,"customer":"Rahul","amount":2500},
    {"order_id":2,"customer":"Sneha","amount":1800},
    {"order_id":3,"customer":"Rahul","amount":3200},
    {"order_id":4,"customer":"Amit","amount":1500}
]

spending = {}
order_count = {}

for order in orders:
    cust = order["customer"]
    amt = order["amount"]

    spending[cust] = spending.get(cust, 0) + amt
    order_count[cust] = order_count.get(cust, 0) + 1

# Highest spender
highest_spender = max(spending, key=spending.get)

print("Spending:", spending)
print("Highest spender:", highest_spender)
print("Order count:", order_count)
