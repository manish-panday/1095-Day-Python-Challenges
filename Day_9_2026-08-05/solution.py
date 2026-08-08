customer_fullname = input("Enter your full name: ")
product_price = float(input("Enter product price: "))
quantity = int(input("Enter quantity that you want: "))

total_price = int(product_price * quantity)
discount_amount = 0 
discount = ""

if total_price >= 10000:
    discount_amount = int(total_price * 20 / 100)
    discount = "20%"
elif total_price >= 5000 and total_price <= 9999:
    discount_amount = int(total_price * 10 / 100)
    discount = "10%"  
elif total_price >= 2000 and total_price <= 4999:
    discount_amount = int(total_price * 5 / 100)
    discount = "5%"
elif total_price > 0 and total_price <= 2000:
    discount_amount = int(total_price * 0 / 100)
    discount = "0%"

final_price = int(total_price - discount_amount)

if discount == "20%":
    print("========== SHOPPING RECEIPT ==========")
    print()
    print(f"Customer: {customer_fullname}")
    print()
    print(f"Product Price: {product_price}")
    print(f"Quantity: {quantity}")
    print()
    print(f"Total Price: {total_price}")
    print(f"Discount: {discount}")
    print(f"Discount Amount: {discount_amount}")
    print()
    print(f"Final Price: {final_price}")
    print()
    print("======================================")
elif discount == "10%":
    print("========== SHOPPING RECEIPT ==========")
    print()
    print(f"Customer: {customer_fullname}")
    print()
    print(f"Product Price: {product_price}")
    print(f"Quantity: {quantity}")
    print()
    print(f"Total Price: {total_price}")
    print(f"Discount: {discount}")
    print(f"Discount Amount: {discount_amount}")
    print()
    print(f"Final Price: {final_price}")
    print()
    print("======================================")
elif discount == "5%":
    print("========== SHOPPING RECEIPT ==========")
    print()
    print(f"Customer: {customer_fullname}")
    print()
    print(f"Product Price: {product_price}")
    print(f"Quantity: {quantity}")
    print()
    print(f"Total Price: {total_price}")
    print(f"Discount: {discount}")
    print(f"Discount Amount: {discount_amount}")
    print()
    print(f"Final Price: {final_price}")
    print()
    print("======================================")
else:
    print("========== SHOPPING RECEIPT ==========")
    print()
    print(f"Customer: {customer_fullname}")
    print()
    print(f"Product Price: {product_price}")
    print(f"Quantity: {quantity}")
    print()
    print(f"Total Price: {total_price}")
    print(f"Discount: {discount}")
    print(f"Discount Amount: {discount_amount}")
    print()
    print(f"Final Price: {final_price}")
    print()
    print("======================================")

    #DONE!!!!!!!!!!!!
    #Updated
    