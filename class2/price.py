discount = 0
sales_tax = 0.1

def tax_func(price):
    taxes = price * sales_tax
    return taxes

def discount_func(price, discount_percent):
    discount_sum = price * (discount_percent / 100)
    return discount_sum

# Исправление input
price = float(input("Enter the price: "))

# Считаем налог
tax = tax_func(price)

# Применяем скидку по условиям
if price > 100 and price <= 200:
    discount = discount_func(price, 10)
elif price > 200: 
    discount = discount_func(price, 20)

# Вычисляем итоговую сумму
total_price = price + tax - discount

print("Total price after tax and discount:", total_price)