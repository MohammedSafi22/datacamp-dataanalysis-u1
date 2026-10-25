name = "Ahmed" 
age = 25  
height = 1.75  
is_student = True 
print(name) 
print(age)
print(type(height)) 

# uodate var value
score = 10
score = score + 5
print(score)

print(7 / 2) 
print(7 // 2) 
print(7 % 2) 
print(2 ** 3) 

#strings
first = "Data"
second = "Science"
print(first + " " + second)  # data scince
print ("ha" * 4)  # hahahaha
print(len(first))  #no of charracters
print("   test    ".strip())  #delete spaces 
print("hello world".upper())    
print("I like cats".replace("cats", "dogs"))

# f stings
name = "Mohammed"
age = 28
print(f"My name is {name} and I am {age} years old")

#type conversion
x = "5"
y = 10
print(int(x) + y)
print(x + str(y))

#if elif else 
temp = 35
if temp > 30: 
  print("Hot")
elif temp > 20:
  print("Nice")
else:
  print("Cold")


# example 1 :BMI calc
wieght = 70
height = 1.75
bmi = wieght / height ** 2 
print(bmi)
print(round(bmi,2))
print(f"Your BMI is {bmi:.2f}")

# example 2: Tax and Compound Interest
price = 249.99
qty = 3   #quantity
tax_rate = 0.14
subtotal = price * qty
total = subtotal * (1 + tax_rate)
print(f"Subtotal: {subtotal:.2f}")
print(f"Total with tax: {total:.2f}")
# compound calc
principal = 1000
rate = 0.05
years = 10
future_value = principal * (1 + rate) ** years
print(f"After {years} years: {future_value:.2f}")