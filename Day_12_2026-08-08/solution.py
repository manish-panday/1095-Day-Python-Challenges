customer_name = input("Enter your name: ")
product1_name = input("Enter product name: ")
product1_price = float(input("Enter product price: "))
product1_quantity = int(input("Enter product quantity: "))

product2_name = input("Enter product name: ")
product2_price = float(input("Enter product price: "))
product2_quantity = int(input("Enter product quantity: "))

product3_name = input("Enter product name: ")
product3_price = float(input("Enter product price: "))
product3_quantity = int(input("Enter product quantity: "))

product1_total = int(product1_price * product1_quantity)
product2_total = int(product2_price * product2_quantity)
product3_total = int(product3_price * product3_quantity)

sub_total = int(product1_total + product2_total + product3_total)

discount_amount = 0
discount = ""
if sub_total >= 10000:
    discount_amount = int(sub_total * 15 / 100)
    discount = "15%"
elif sub_total >= 5000 and sub_total < 10000:
    discount_amount = int(sub_total * 10 /100)
    discount = "10%"
elif sub_total >= 2000 and sub_total < 5000:
    discount_amount = int(sub_total * 5 / 100)
    discount = "5%"
elif sub_total < 2000:
    discount = "0%"
    discount_amount = int(sub_total * 0 / 100)

discounted_amount = sub_total - discount_amount

tax = int(discounted_amount * 13 / 100)

final_amount = discounted_amount + tax

print("========== SHOPPING BILL ==========")
print()
print(f"Customer Name: {customer_name}")
print()
print(f"Product 1: {product1_name}")
print(f"Price: Rs. {product1_price}")
print(f"Quantity: {product1_quantity}")
print(f"Total: Rs. {product1_total}")
print()
print(f"Product 2: {product2_name}")
print(f"Price: Rs. {product2_price}")
print(f"Quantity: {product2_quantity}")
print(f"Total: Rs. {product2_total}")
print()
print(f"Product 3: {product3_name}")
print(f"Price: Rs. {product3_price}")
print(f"Quantity: {product3_quantity}")
print(f"Total: Rs. {product3_total}")
print()
print("-----------------------------------")
print()
print(f"SubTotal: Rs. {sub_total}")
print(f"Discount: {discount}")
print(f"Discount Amount: Rs. {discount_amount}")
print()
print(f"Amount After Discount: Rs. {discounted_amount}")
print()
print(f"VAT: 13%")
print(f"VAT Amount: Rs. {tax}")
print()
print("-----------------------------------")
print()
print(f"Final Amount: Rs. {final_amount}")
print()
print("==================================")


#DONE!!!!